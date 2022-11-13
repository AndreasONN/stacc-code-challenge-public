# Importere noedvendige biblioteker
import requests
import pprint

# METODE: velger funksjon
def hoved_loekke():

    # Spoerre brukeren hva den vil gjoere
    while True:
        oppgave = input("Hva vil du gjoere ('pep'/'avslutt')?:  ").lower()  # foreloepig bare PEP-funksjonalitet, kan utvides.
        
        # PEP-sjekk
        if oppgave == "pep":

            while True:
                pep_input = input("Oppgi navn (eller 'tilbake'/'avslutt'):  ").lower()

                if pep_input == "tilbake":
                    break

                elif pep_input == "avslutt":
                    quit()
                
                pep(pep_input)

        elif oppgave == "avslutt":
            quit()
        
        else:
           print("Ugyldig kommando.") 

# METODE: PEP-sjekk
def pep(navn):
    # TODO: gi error hvis det oppstaar en koblingsfeil
    navn_req = "https://code-challenge.stacc.dev/api/pep?name=" + navn
    pep_req = requests.get(navn_req).json()  # json() metoden konverterer i dette tilfellet svaret til et dict-objekt.

    # Skrive ut antall resultater
    print("\nFant " + str(pep_req.get("numberOfHits")) + " resultater.")

    # TODO: skrive ut resultater paa nett maate.
    # pprint.pprint(pep_req)
    # Hente ut resultatene
    pep_hits = pep_req.get("hits")

    # Skrive ut en nummerert resultatliste (med navn)
    for i in range(len(pep_hits)):
        print(str(i + 1) + ": " + pep_hits[i].get("name"))

    sjekk_nr = int(input("\nVelg personen du vil sjekke opplysninger for (velg nummer):  "))
    # pprint.pprint(pep_hits[sjekk_nr - 1])
    pep_dict_print(pep_hits[sjekk_nr - 1])
    # TODO unngaa ugyldig input

# HJELPEMETODE: skriver ut PEP-sjekk resultater pent
def pep_dict_print(dict):
    # for egenskap, verdi in dict.items():
    #    print("{}: {}".format(egenskap, verdi))
    print("\nNavn: " + dict.get("name") +
    "\nAliaser: " + dict.get("aliases") +
    "\nFoedselsdato: " + dict.get("birth_date") +
    "\nLand: " + dict.get("countries") +
    "\nIdentifikatorer: " + dict.get("identifiers") +
    "\nSanksjoner: " + dict.get("sanctions") +
    "\nTelefonnummer: " + dict.get("phones") +
    "\nE-postadresser: " + dict.get("emails") +
    "\nFunnet i database: " + dict.get("dataset") +
    "\nFoerst sett: " + dict.get("first_seen") +
    "\nSist sett: " + dict.get("last_seen") +
    "\n")

# Kjoere hovedloekken
hoved_loekke()