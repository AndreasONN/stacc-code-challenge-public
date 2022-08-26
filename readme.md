# Stacc Challenge 📝

Årets oppgave er en åpen oppgave relatert til KYC. Det er opp til dere hvilken teknologi dere bruker til oppgaven og hvordan den løses. Det er dermed mulig å løse den uavhengig av om du foretrekker backend, frontend, UX eller hele stacken.
Det viktigste er at dere lager en applikasjon, API eller design som gjør det mulig å utføre KYC sjekker av enkelt individer og/eller personer i et selskap.

_Se avsnittet som omtaler 'krav til innlevering' for **minimumskravet**._

## Know Your Customer

KYC eller “know your customer” er virkemidler som sikrer at et finansforetak vet nok om sine kunder til å forhindre og avdekke om det finansielle systemet brukes til ulovlig virksomhet, som hvitvasking, korrupsjon og terrorfinansiering. Et av disse virkemidlene er å utføre en PEP-sjekk (Politically Exposed Person) av kunder. En politisk eksponert person har generelt sett større risiko for korrupsjon og bestikkelser knyttet til seg, og vil dermed være flagget for manuell behandling i f.eks en lånesøknad hos en bank.

## Forslag til oppgaver:

**a) Lag en enkel webapp som lar brukeren utføre en KYC-sjekk av én person.**

**b) Implementer ditt eget KYC API som returnerer treff på enkeltpersoner og/eller selskap.**

**c) Skisser hvordan en KYC sjekk kunne sett ut. Kanskje i kontekst av en lånesøknad eller via en nettbank.**

- _Du velger fritt hvilken oppgave du vil gjøre, men du kan fint prøve deg på alle om du ønsker det._

**Mulige Utvidelser**

- Publiser webappen og/eller APIet slik at de er tilgjengelig via HTTP
  - Kan f.eks publiseres til azure, google cloud, heroku, surge eller kanskje din egen server?
- Utvide KYC/PEP sjekken til å sjekke alle personer i et foretak istedenfor bare én person.
  - Visualisere sjekken på en kreativ og oversiktelig måte?
- Utvid skissen din til å være en interaktiv prototype.

#

Vi presiserer at kandidater står fritt til å utforske problemstillingen slik de selv ønsker (etter minimumskravet)

- Hvis du er tryggest på front-end og ikke ønsker å knote med et eget API så er dette ikke noe problem.
- Kanskje back-end er mer din greie? Bruk heller mesteparten av tiden din her.
- Foretrekker du heller design og har lite erfaring med koding? Bruk da tiden på å skissere og finpusse på disse.

# Stacc KYC API / Data

I forbindelse med kodeoppgaven har vi laget et enkelt API (express.js), med noen få endepunkter som kan hjelpe deg med å komme i gang med oppgaven:

- Her kan du hente data fra [brønnøysundregisteret](https://www.brreg.no/) og [open sanctions](http://opensanctions.org/) som du kan benytte deg av for å utføre en PEP sjekk av personer og selskap.
- Du velger helt selv om du vil konsumere vårt API, eller benytte deg av vedlagt test data ([pep.csv](https://raw.githubusercontent.com/hpl002/stacc-code-challenge-public/master/pep.csv)) i repo for å utføre PEP sjekken.
- Hvis du designer eller bare mocker data selv, kan du ta utgangspunkt i ([pep_small.json](https://raw.githubusercontent.com/hpl002/stacc-code-challenge-public/master/pep_small.json))

API'et er tilgjengelig på: https://code-challenge.stacc.dev/

- Merk at alle requests går via `/api`
- `/docs` ruter tilbake til dette repoet
- Alle API spørringer er dokumentert i [postman](https://www.postman.com/).

#

**Eksempel Spørringer / Postman Collection**: Vi har laget en postman-collection, med oversikt over ulike API endepunkter som kan benyttes for å løse ulike oppgaver. Vi anbefaler deg å "forke" samlingen slik at du kan teste ut API'et og hente ut ulike data.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/16040688-74d4dc53-b65b-457c-8865-b5c4d6d4fdc5?action=collection%2Ffork&collection-url=entityId%3D16040688-74d4dc53-b65b-457c-8865-b5c4d6d4fdc5%26entityType%3Dcollection%26workspaceId%3Df408e47c-588c-4301-ba9f-6838a7f3b57a)

#

## Krav til design innlevering:

1. Oppgaven må i det minste vise hvordan en PEP sjekk kan utføres av én person.
   - Vi oppfordrer deg til å utvide på oppgaven slik du vil, og være kreativ i din besvarelse.
2. Du kan levere skissene dine som bilder eller lenke til skissene og prototypen din i designprogrammet ditt (f.eks figma).
   - Viktig at du gir alle med linken mulighet til å se skissene dine (Dette settes når du skal dele linken i figma).
3. Legg ved en beskrivelse av oppgaven eller kommentarer i skissen som begrunner design beslutninger og hva du har tenkt på.

4. **Innleveringer sendes [her](mailto:challenge@stacc.com).**

#

## Krav til kode innlevering:

1. Oppgaven må i det minste kunne utføre en enkel PEP sjekk av én person (enten via en app eller API).
   - Vi oppfordrer deg til å utvide på oppgaven slik du vil, og være kreativ i din besvarelse.
2. Oppgaven må publiseres på github (gjerne i et _public_ repositorium)
   - Vi oppfordrer kandidater til å bruke **git** slik at vi sammen kan se igjennom commits og historikk.
   - Om du ønsker å holde denne privat så må du sende zip.
3. Alle oppgaver må inneholde en _readme.md_ fil som beskriver prosjektet i korte trekk. Følg [denne linken for mal.](https://github.com/hpl002/stacc-code-challenge-public/blob/master/readmeTemplate.md)
   - Her dokumenterer og kommenterer du smått underveis. Spesielt viktig at det medfølger gode instrukser som beskriver hvordan prosjektet kjøres lokalt.
     _Husk at dette ikke bare skal kjøre på din egen maskin!_
4. **Innleveringer sendes [her](mailto:challenge@stacc.com).**

   **Enten link til offentlig repo eller .zip**

- Vi foretrekker og anbefaler link til offentlig repo

# Lykke til! ✌️

Vi har opprettet en egen Discord kanal for spørsmål relatert til oppgaven, ikke nøl med å skrive til oss skulle noe være uklart eller om det oppstår problemer underveis i forbindelse med oppgaven. Alternativt kan dere sende oss en mail (litt tregere responstid over e-post, vi foretrekker discord 👍🙂)

## Discord Kanal

[![Joing us on Discord](https://assets-global.website-files.com/6257adef93867e50d84d30e2/62594fddd654fc29fcc07359_cb48d2a8d4991281d7a6a95d2f58195e.svg)](https://discord.gg/s2RyPJvBqQ)

## E-post 📬

Spørsmål om oppgaven sendes hit:
- challenge@stacc.com
