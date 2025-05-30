import abc
from dataclasses import dataclass

from antrag import WohngeldAntrag
from nachweise import Mietvertrag, Nachweis, Rentenbescheid


@dataclass
class HinweisSachbearbeitung(abc.ABC):
    titel: str
    beschreibung: str


@dataclass
class Anforderung(abc.ABC):
    # Liste der Gründe, warum diese Anforderung an den/die Bürger:in gestellt wurde
    gruende: list[str]
    # Name der Person, an die die Anforderung gestellt wurde
    person_name: str
    # Name der Anforderung
    name: str

    @abc.abstractmethod
    def ist_erfuellt(
        self, antrag: WohngeldAntrag, nachweise: list[Nachweis]
    ) -> tuple[bool, list[HinweisSachbearbeitung]]:
        pass


@dataclass
class Miethoehe(Anforderung):
    name: str = "Miethöhe"
    beschreibung: str = "Nachweis über die Miethöhe"

    def ist_erfuellt(
        self, antrag: WohngeldAntrag, nachweise: list[Nachweis]
    ) -> tuple[bool, list[HinweisSachbearbeitung]]:
        if mietvertraege := [
            nachweis for nachweis in nachweise if isinstance(nachweis, Mietvertrag)
        ]:
            if any(
                mietvertrag.betrag == antrag.miete.gesamtmiete
                for mietvertrag in mietvertraege
            ):
                return True, []
            else:
                return False, [
                    HinweisSachbearbeitung(
                        titel="Miethöhe weicht ab",
                        beschreibung="Ein Mietvertrag wurde eingereicht, aber die Miethöhe stimmt nicht mit der Angabe im Antrag überein",
                    )
                ]

        return False, []


@dataclass
class Rente(Anforderung):
    name: str = "Rente"
    beschreibung: str = "Nachweis über die Rente"

    def ist_erfuellt(
        self, antrag: WohngeldAntrag, nachweise: list[Nachweis]
    ) -> tuple[bool, list[HinweisSachbearbeitung]]:
        if any(
            isinstance(nachweis, Rentenbescheid)
            and self.person_name in nachweis.personen_namen
            for nachweis in nachweise
        ):
            return True, []

        return False, []
