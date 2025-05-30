from anforderungen import Anforderung
from antrag import WohngeldAntrag
import beispiel_antrag
from nachweise import Nachweis
from rules import Rule


def main(antrag: WohngeldAntrag, nachweise: list[Nachweis]):
    print(f"Verarbeite Antrag {antrag.wohngeld_nr} vom {antrag.antrag_datum}\n")

    # Generiere alle Anforderungen für diesen Antrag
    anforderungen: list[Anforderung] = []
    for rule in Rule.__subclasses__():
        anforderungen.extend(rule().run(antrag, nachweise))

    # Überprüfe, ob die Anforderungen durch die Nachweise erfüllt sind
    anforderungen_erfuellt = []
    anforderungen_nicht_erfuellt = []
    hinweise_sachbearbeitung = []
    for anforderung in anforderungen:
        erfuellt, hinweise = anforderung.ist_erfuellt(antrag, nachweise)
        hinweise_sachbearbeitung.extend(hinweise)

        if erfuellt:
            anforderungen_erfuellt.append(anforderung)
        else:
            anforderungen_nicht_erfuellt.append(anforderung)

    print("Erfüllte Anforderungen:\n")
    print("".join([f'- {anforderung.beschreibung}. Gründe: {", ".join(anforderung.gruende)}\n' for anforderung in anforderungen_erfuellt]))

    print("\nNicht erfüllte Anforderungen:\n")
    print("".join([f'- {anforderung.beschreibung}. Gründe: {", ".join(anforderung.gruende)}\n' for anforderung in anforderungen_nicht_erfuellt]))

    print("\nHinweise für die Sachbearbeitung:\n")
    print("".join([f'- {hinweis.titel}: {hinweis.beschreibung}\n' for hinweis in hinweise_sachbearbeitung]))


if __name__ == "__main__":
    main(beispiel_antrag.wohngeld_antrag_rentnerin, [beispiel_antrag.mietvertrag, beispiel_antrag.rentenbescheid])
    print("--------------------------------\n")
    main(beispiel_antrag.wohngeld_antrag_student, [beispiel_antrag.mietvertrag_student])