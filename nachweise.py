from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Nachweis:
    _name: str
    # Liste der Personen, die im Nachweis benannt sind
    personen_namen: list[str] = field(default_factory=list)


@dataclass
class Mietvertrag(Nachweis):
    _name: str = "Mietvertrag"
    betrag: Optional[float] = None


@dataclass
class Rentenbescheid(Nachweis):
    _name: str = "Rentenbescheid"

