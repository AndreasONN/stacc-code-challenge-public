# Importer "requests"-biblioteket
import requests

def hoved_loekke():

    # Spoerre brukeren hva den vil gjoere
    while True:
        oppgave = input("Hva vil du gjoere (pep)? ")  # foreloepig bare PEP-funksjonalitet, kan utvides.
        
        # PEP-sjekk
        if oppgave == "pep":
            pep(input("Oppgi navn: "))
        
        else:
           print("Ugyldig kommando.") 

# PEP-sjekk metode
def pep(navn):
    navn_req = "https://code-challenge.stacc.dev/api/pep?name=" + navn
    pep_req = requests.get(navn_req).json()  # json() metoden konverterer i dette tilfellet svaret til et dict-objekt.
    # print(pep_request.content)

    # Skrive ut antall resultater
    print("Fant " + str(pep_req.get("numberOfHits")) + " resultater.")

    # TODO: skrive ut resultater paa nett maate.

# Kjoere hovedloekken
hoved_loekke()