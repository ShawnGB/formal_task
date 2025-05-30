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

#die Anforderung ist dass entwder der Antragsteller im Mietvertarg steht oder der offizielle Mieter mit im Hashalt eingettagen ist
@dataclass
class MieterIdentPruefung (Anforderung):
    name: str = "Pruefung der Mieteridentitaet"
    beschreibung: str = "Wer ist Mieter im Mietvertrag"

    #funktion zum extrahieren aller offiziellen Mieter aus dem Mietvertrag und sie in eine Liste packen
    def _parse_mieter_namen(self, mietvertrag: Mietvertrag) -> list[str]:
        alle_mieter: list[str] = []
        if not hasattr(mietvertrag, 'personen_namen') or not mietvertrag.personen_namen:
            return alle_mieter

        for name_eintrag in mietvertrag.personen_namen:
            if isinstance(name_eintrag, str):
                namen_gesplittet = [name.strip() for name in name_eintrag.split(',')]
                alle_mieter.extend(n for n in namen_gesplittet if n) 
        return alle_mieter

    # pruefen ob die Anforderung erfuellt wird
    def ist_erfuellt(
        self, antrag: WohngeldAntrag, nachweise: list[Nachweis]
    ) -> tuple[bool, list[HinweisSachbearbeitung]]:
        
        mietvertrag_gefunden: Mietvertrag | None = None

        #den Mietvertrag aus den Nachweisen raus suchen, falls keiner vorhanden kann die Anforderung nicht geprueft werdem, Hinweis geben
        for nachweis_obj in nachweise:
            if isinstance(nachweis_obj, Mietvertrag):
                mietvertrag_gefunden = nachweis_obj
                break

        if not mietvertrag_gefunden:
            return False, [
                HinweisSachbearbeitung(
                    titel="Prüfung Mietvertrag: Kein Mietvertrag",
                    beschreibung="Es wurde kein Mietvertrag zur Prüfung der Mieteridentität eingereicht."
                )
            ]

        #Mieter extrahieren
        mieter_im_vertrag = self._parse_mieter_namen(mietvertrag_gefunden)

        #namen des antragstellers und der Haushaltsmitglieder zum abgleichen
        antragsteller_name = antrag.antragsteller.get_full_name()
        haushaltsmitglieder_namen = [hm.get_full_name() for hm in antrag.haushaltsmitglieder]

        #idealfall mieter ist antragsteller
        if antragsteller_name in mieter_im_vertrag:
            return True, [] 

        #wenn nicht dann checken ob mieter haushaltsmitglied ist
        if any(hm_name in mieter_im_vertrag for hm_name in haushaltsmitglieder_namen):
            return True, [] 

        #weder antragsteller noch haushaltsmitglied ist mieter, hinwies an die Sachbearbeitung
        finaler_hinweis = HinweisSachbearbeitung(
            titel="Prüfung Mietvertrag: Mieter nicht im Haushalt", 
            beschreibung=(
                f"Weder der Antragsteller ('{antragsteller_name}') noch ein Haushaltsmitglied ist im Mietvertrag als Mieter aufgeführt. "
                f"Im Mietvertrag genannte Mieter ({', '.join(mieter_im_vertrag)}) gehören nicht zum Haushalt. " 
                "Bitte klären, ob z.B. eine Untermiete oder WG-Konstellation vorliegt und die Antragsberechtigung gegeben ist."
            )
        )
        
        return False, [finaler_hinweis]
