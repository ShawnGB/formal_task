from datetime import date

import antrag as ANT
import nachweise as NW

wohngeld_antrag_rentnerin = ANT.WohngeldAntrag(
    antrag_datum=date.today(),
    wohngeld_nr="WG-2024-12345",
    antragsteller=ANT.Antragsteller(
        vorname="Henriette",
        nachname="Muster",
        geburtsdatum=date(1955, 5, 15),
        geschlecht="weiblich",
        einnahmen=[
            ANT.Einnahme(betrag=1200.00, art=ANT.EinnahmeArt.RENTEN_PENSIONEN),
            ANT.Einnahme(betrag=150.00, art=ANT.EinnahmeArt.SONSTIGE),
        ],
        erwerbsstatus=ANT.Erwerbsstatus.RENTE,
    ),
    haushaltsmitglieder=[
        ANT.Haushaltsmitglied(
            vorname="Sigfried",
            nachname="Muster",
            geburtsdatum=date(1950, 1, 1),
            geschlecht="männlich",
            einnahmen=[
                ANT.Einnahme(betrag=1100.00, art=ANT.EinnahmeArt.RENTEN_PENSIONEN),
            ],
        ),
    ],
    wohnung=ANT.Wohnung(
        wohnort="Berlin",
        plz="10115",
        strasse="Musterstraße",
        hausnummer="1A",
        quadratmeter=60,
    ),
    miete=ANT.Miete(
        gesamtmiete=650.00,
        kaltmiete=500.00,
        nebenkosten=150.00,
        mietvertrag_beginn=date(2010, 1, 1),
        unbefristeter_mietvertrag=True,
    ),
)

mietvertrag = NW.Mietvertrag(
    personen_namen=["Henriette Muster", "Peter Vermieter"],
    betrag=600.00,
)

rentenbescheid = NW.Rentenbescheid(personen_namen=["Henriette Muster"])

# ------------------------------------------------------------

wohngeld_antrag_student = ANT.WohngeldAntrag(
    antrag_datum=date.today(),
    wohngeld_nr="WG-2024-67890",
    antragsteller=ANT.Antragsteller(
        vorname="Jonas",
        nachname="Meyer",
        geburtsdatum=date(2000, 1, 1),
        geschlecht="männlich",
        einnahmen=[
            ANT.Einnahme(betrag=600.00, art=ANT.EinnahmeArt.SONSTIGE),
        ],
        erwerbsstatus=ANT.Erwerbsstatus.AZUBI_STUDIERENDE,
    ),
    haushaltsmitglieder=[],
    wohnung=ANT.Wohnung(
        wohnort="München",
        plz="80331",
        strasse="Hauptstraße",
        hausnummer="123",
        quadratmeter=40,
    ),
    miete=ANT.Miete(
        gesamtmiete=400.00,
        kaltmiete=300.00,
        nebenkosten=100.00,
        mietvertrag_beginn=date(2024, 1, 1),
        unbefristeter_mietvertrag=True,
    ),
)

mietvertrag_student = NW.Mietvertrag(
    personen_namen=["Manfred Meyer, Peter Vermieter"],
    betrag=400.00,
)
