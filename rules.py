import abc

import anforderungen as A
from nachweise import Nachweis
from antrag import EinnahmeArt, Erwerbsstatus, WohngeldAntrag


class Rule(abc.ABC):
    _beschreibung: str = ""

    @abc.abstractmethod
    def run(
        self, antrag: WohngeldAntrag, nachweise: list[Nachweis]
    ) -> list[A.Anforderung]:
        pass


class Miethoehe(Rule):
    _beschreibung: str = "Die Miethöhe muss immer nachgewiesen werden"

    def run(
        self, antrag: WohngeldAntrag, nachweise: list[Nachweis]
    ) -> list[A.Anforderung]:
        return [
            A.Miethoehe(
                gruende=["Erstantrag"], person_name=antrag.antragsteller.get_full_name()
            )
        ]


class Rente(Rule):
    _beschreibung = "Wenn der Erwerbsstatus Rentner ist oder Einkommen aus Rente vorliegt muss ein Nachweis eingereicht werden"

    def run(
        self, antrag: WohngeldAntrag, nachweise: list[Nachweis]
    ) -> list[A.Anforderung]:
        anforderungen = []

        for hm in [antrag.antragsteller] + antrag.haushaltsmitglieder:
            if hm.erwerbsstatus and hm.erwerbsstatus == Erwerbsstatus.RENTE:
                anforderungen.append(
                    A.Rente(
                        person_name=hm.get_full_name(),
                        gruende=[f"Erwerbsstatus von {hm.get_full_name()} ist Rentner"],
                    )
                )

            elif renten_einnahmen := [
                e for e in hm.einnahmen if e.art == EinnahmeArt.RENTEN_PENSIONEN
            ]:
                anforderungen.append(
                    A.Rente(
                        person_name=hm.get_full_name(),
                        gruende=[
                            f"Einnahmen aus Rente für {hm.get_full_name()} i. H. v. {', '.join([f'{e.betrag} €' for e in renten_einnahmen])}"
                        ],
                    )
                )

        return anforderungen
