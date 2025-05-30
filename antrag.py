from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional


class Erwerbsstatus(Enum):
    ARBEITNEHMER = "Arbeitnehmer"
    RENTE = "Rentner"
    SELBSTSTAENDIG = "Selbstständig"
    AZUBI_STUDIERENDE = "Azubi/Studierende"
    ARBEITSLOS = "Arbeitslos"


class EinnahmeArt(Enum):
    GEHALT = "Gehalt"
    RENTEN_PENSIONEN = "Rente"
    SONSTIGE = "Sonstige"


@dataclass
class Einnahme:
    betrag: float
    art: Optional[EinnahmeArt] = None


@dataclass
class Person:
    vorname: str
    nachname: str
    geburtsdatum: date
    geschlecht: str
    einnahmen: list[Einnahme]
    erwerbsstatus: Optional[Erwerbsstatus] = None

    def get_full_name(self) -> str:
        return f"{self.vorname} {self.nachname}"


@dataclass
class Antragsteller(Person):
    pass


@dataclass
class Haushaltsmitglied(Person):
    pass


@dataclass
class Wohnung:
    wohnort: str
    plz: str
    strasse: str
    hausnummer: str
    quadratmeter: int


@dataclass
class Miete:
    gesamtmiete: float
    kaltmiete: Optional[float] = None
    nebenkosten: Optional[float] = None
    mietvertrag_beginn: Optional[date] = None
    mietvertrag_ende: Optional[date] = None
    unbefristeter_mietvertrag: Optional[bool] = None


@dataclass
class WohngeldAntrag:
    antrag_datum: date
    wohngeld_nr: str
    antragsteller: Antragsteller
    haushaltsmitglieder: list[Haushaltsmitglied]
    wohnung: Optional[Wohnung] = None
    miete: Optional[Miete] = None
