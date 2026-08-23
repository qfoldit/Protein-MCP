"""FASTA parsing, validation, normalization and export utilities for qFoldIT."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


PROTEIN_ALPHABET = frozenset("ACDEFGHIKLMNPQRSTVWYBXZJUO*-?")
DNA_ALPHABET = frozenset("ACGTNRYKMSWBDHV")
RNA_ALPHABET = frozenset("ACGUNRYKMSWBDHV")


@dataclass(frozen=True)
class FastaRecord:
    """A single FASTA record."""

    identifier: str
    description: str
    sequence: str

    @property
    def header(self) -> str:
        return self.identifier if not self.description else f"{self.identifier} {self.description}"


def _clean_sequence(lines: Iterable[str]) -> str:
    return "".join("".join(lines).split()).upper()


def parse_fasta(text: str, *, require_header: bool = True) -> list[FastaRecord]:
    """Parse FASTA text into records without requiring external dependencies."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("FASTA input is empty")

    records: list[FastaRecord] = []
    header: str | None = None
    sequence_lines: list[str] = []

    def flush() -> None:
        nonlocal header, sequence_lines
        if header is None:
            return
        sequence = _clean_sequence(sequence_lines)
        if not sequence:
            raise ValueError(f"FASTA record '{header}' has an empty sequence")
        parts = header.split(maxsplit=1)
        records.append(FastaRecord(parts[0], parts[1] if len(parts) > 1 else "", sequence))
        sequence_lines = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith(";"):
            continue
        if line.startswith(">"):
            flush()
            header = line[1:].strip()
            if not header:
                raise ValueError("FASTA header cannot be empty")
        else:
            if header is None and require_header:
                raise ValueError("FASTA sequence encountered before the first header")
            if header is None:
                header = "sequence_1"
            sequence_lines.append(line)

    flush()
    if not records:
        raise ValueError("No FASTA records found")
    return records


def validate_sequence(sequence: str, *, molecule: str = "protein", allow_gaps: bool = True) -> dict:
    """Validate a normalized sequence and return structured diagnostics."""
    normalized = _clean_sequence([sequence])
    molecule = molecule.lower()
    alphabet = {
        "protein": PROTEIN_ALPHABET,
        "dna": DNA_ALPHABET,
        "rna": RNA_ALPHABET,
    }.get(molecule)
    if alphabet is None:
        raise ValueError("molecule must be one of: protein, dna, rna")

    allowed = set(alphabet)
    if not allow_gaps:
        allowed.discard("-")
        allowed.discard("*")
    invalid = sorted(set(normalized) - allowed)
    return {
        "valid": not invalid and bool(normalized),
        "molecule": molecule,
        "length": len(normalized),
        "invalid_symbols": invalid,
        "sequence": normalized,
    }


def to_fasta(records: Iterable[FastaRecord], *, line_width: int = 80) -> str:
    """Serialize records as canonical FASTA."""
    if line_width < 1:
        raise ValueError("line_width must be positive")
    output: list[str] = []
    for record in records:
        if not record.identifier:
            raise ValueError("FASTA record identifier cannot be empty")
        output.append(f">{record.header}")
        sequence = _clean_sequence([record.sequence])
        output.extend(sequence[i:i + line_width] for i in range(0, len(sequence), line_width))
    return "\n".join(output) + ("\n" if output else "")


def summarize_fasta(text: str, *, molecule: str = "protein") -> dict:
    """Return validation and length metadata for every FASTA record."""
    records = parse_fasta(text)
    items = []
    for record in records:
        validation = validate_sequence(record.sequence, molecule=molecule)
        items.append({
            "id": record.identifier,
            "description": record.description,
            **validation,
        })
    return {
        "record_count": len(items),
        "molecule": molecule,
        "records": items,
    }
