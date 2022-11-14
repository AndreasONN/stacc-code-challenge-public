# Importere noedvendige biblioteker
import requests
import pprint

# METODE: aapner hovedmenyen og kjoerer den i loekke helt til brukeren velger aa avslutte programmet.
def hovedloekke():
    print("\n*** Velkommen til 'PEPperkverna' PEP-sjekk!*** \n")

    while True:
        hovedmeny()

# METODE: lar brukeren velge funksjon
def hovedmeny():
    oppgave = input(
        "> Vil du soeke informasjon om en person eller et foretak? ('person'/'foretak'/'avslutt')?:  ").lower()
    oppgitt_soekestreng = ""

    if oppgave == "person":
        oppgitt_soekestreng = input("> Oppgi navn for personsjekk:  ").lower() # Per naa gir denne sjekken alltid true. Men greit aa avgjoere det i metoden og ikke her.
        if gyldig_soekestreng(oppgitt_soekestreng, oppgave):
            pep_soek(oppgitt_soekestreng, oppgave)

    elif oppgave == "foretak":
        oppgitt_soekestreng = input(
            "> Oppgi orgnr. for foretakssjekk:  ").lower()
        if gyldig_soekestreng(oppgitt_soekestreng, oppgave):
            pep_soek(oppgitt_soekestreng, oppgave)

    elif oppgave == "avslutt":
        quit()

    else:
        print("Ugyldig kommando, proev igjen.")

# METODE: utfoerer PEP-soek paa personer eller foretak. Kaller saa andre metoder som skriver ut resultatene.
def pep_soek(soekestreng, type_soek):

    # Bygger opp riktig adresse for forespoerselen.
    if type_soek == "person":
        pep_forespoersel = "https://code-challenge.stacc.dev/api/pep?name=" + soekestreng

    elif type_soek == "foretak":
        pep_forespoersel = "https://code-challenge.stacc.dev/api/enheter?orgNr=" + soekestreng

    # Sender forespoerselen, og gir resultatet videre til riktig metode.
    try:
        print("Soeker - vennligst vent...")
        pep_svar = requests.get(pep_forespoersel).json() # json() metoden konverterer i dette tilfellet svaret til en ordbok (dict).
    except requests.ConnectionError:  # "Catcher" ev. koblingsfeil.
        print("FEIL: kunne ikke koble til tjener. Sjekk forbindelsen din og proev igjen senere.")
    else:
        if type_soek == "person":
            pep_person(pep_svar)
        elif type_soek == "foretak":
            pep_foretak(pep_svar)

# HJELPEMETODE: sjekker om oppgitt soekestreng er gyldig
def gyldig_soekestreng(soekestreng, oppgave):
    if oppgave == "person":
        return True

    # Orgnr. skal kun bestaa av tall og vaere 9 siffer lange. Modulus 11 sjekk utfoeres ikke.
    elif oppgave == "foretak":
        if soekestreng.isnumeric() and (len(soekestreng) == 9):
            return True
        else:
            print(
                "Oppgitt orgnr. er ugyldig. Sjekk at det bestaar kun av tall, 9 siffer.")
            return False

    # Dette burde aldri skje, med mindre programmet senere utvides med nye typer oppgaver, uten at de implementeres riktig.
    else:
        print("INTERN FEIL: forespurt oppgave er ugyldig.")
        return False

# METODE: viser en liste over personer funnet og gir informasjon om hver enkelte etter forespoersel.
def pep_person(pep_svar):
    antall_resultater = pep_svar.get("numberOfHits")
    print("\nFant " + str(antall_resultater) + " resultater.")

    # Gitt at vi fant resultater...
    if antall_resultater > 0:

        # Hente ut resultatene
        pep_resultatliste = pep_svar.get("hits")

        # Skrive ut en nummerert resultatliste (med navn)
        for i in range(len(pep_resultatliste)):
            print(str(i + 1) + ": " + pep_resultatliste[i].get("name"))

        # Spoerre helt til brukeren oppgir et gyldig nummer.
        sjekk_nr = 0
        while not (0 < sjekk_nr <= antall_resultater):
            sjekk_nr = int(input(
                "\n> Velg personen du vil se opplysninger om (1 - " + str(antall_resultater) + "):  "))
        pep_person_print(pep_resultatliste[sjekk_nr - 1])

# HJELPEMETODE: skriver ut PEP-info om en person i ryddig format
def pep_person_print(person_dict):
    if person_dict.get("name") is not None:
        print("\nNavn: " + person_dict.get("name") +
              "\nAliaser: " + person_dict.get("aliases") +
              "\nFoedselsdato: " + person_dict.get("birth_date") +
              "\nLand: " + person_dict.get("countries") +
              "\nIdentifikatorer: " + person_dict.get("identifiers") +
              "\nSanksjoner: " + person_dict.get("sanctions") +
              "\nTelefonnummer: " + person_dict.get("phones") +
              "\nE-postadresser: " + person_dict.get("emails") +
              "\nFunnet i database: " + person_dict.get("dataset") +
              "\nFoerst sett: " + person_dict.get("first_seen") +
              "\nSist sett: " + person_dict.get("last_seen") +
              "\n")

    else:
        print("INTERN FEIL: Ugyldig persondata mottatt.")

# METODE: skriver ut informasjon om et foretak.
def pep_foretak(foretak_dict):

    if foretak_dict.get("navn") is not None:
        print("\nNavn: " + str(foretak_dict.get("navn")) +
              "\nOrganisasjonsform: " + foretak_dict.get("organisasjonsform").get("beskrivelse") +
              "\n\nStiftelsesdato: " + foretak_dict.get("stiftelsesdato") +
              "\nReg. dato i Enhetsregisteret: " + foretak_dict.get("registreringsdatoEnhetsregisteret") +
              "\nReg. i MVA-registeret?: " + str(foretak_dict.get("registrertIMvaregisteret")) +
              "\nReg. i Foretaksregisteret?: " + str(foretak_dict.get("registrertIForetaksregisteret")) +
              "\nReg. i Stiftelsesregisteret?: " + str(foretak_dict.get("registrertIStiftelsesregisteret")) +
              "\nReg. i Frivillighetsregisteret?: " + str(foretak_dict.get("registrertIFrivillighetsregisteret")) +
              "\n\nNaeringskode: " + foretak_dict.get("naeringskode1").get("kode") + " - " + foretak_dict.get("naeringskode1").get("beskrivelse") +
              "\nInstitusjonell sektorkode: " + foretak_dict.get("institusjonellSektorkode").get("kode") + " - " + foretak_dict.get("institusjonellSektorkode").get("beskrivelse") +
              "\nAntall ansatte: " + str(foretak_dict.get("antallAnsatte")) +
              "\n\nForretningsadresse: " + foretak_dict.get("forretningsadresse").get("adresse")[0] + ", " + foretak_dict.get("forretningsadresse").get("postnummer") +
              ", " + foretak_dict.get("forretningsadresse").get("poststed") + ", " + foretak_dict.get("forretningsadresse").get("land") +
              "\nKommune: " + foretak_dict.get("forretningsadresse").get("kommune") + " - komunnenr. " + foretak_dict.get("forretningsadresse").get("kommunenummer") +
              "\n\nSiste innsendte aarsregnskap: " + foretak_dict.get("sisteInnsendteAarsregnskap") +
              "\nKonkurs?: " + str(foretak_dict.get("konkurs")) +
              "\nUnder avvikling?: " + str(foretak_dict.get("underAvvikling")) +
              "\nUnder tvangsavvikling eller -opploesning: " + str(foretak_dict.get("underTvangsavviklingEllerTvangsopplosning")) +
              "\n\nInfo om foretaket i brreg: " + foretak_dict.get("_links").get("self").get("href") + "\n")
    else:
        print("FEIL: oppgitt orgnr. er ugyldig, eller mottatt data er feil formatert. Vennligst sjekk om orgnr. stemmer.")


# Kjoere hovedloekken
hovedloekke()
