![[Joing us on Slack](https://99designs-blog.imgix.net/blog/wp-content/uploads/2018/07/add-to-slack-button.png?auto=format&q=60&fit=max&w=930)](https://media-exp1.licdn.com/dms/image/C4D0BAQEJziJobYtFyQ/company-logo_200_200/0/1625126662709?e=2159024400&v=beta&t=yAgccdM6O3UYZg-Eoqux-e2t_D8_kRCMj4oeUkr9-qc)


# Stacc Code Challenge: Know Your Customer
KYC eller “know your customer” er virkemidler som sikrer at et finansforetak vet nok om sine kunder til å forhindre og avdekke om det finansielle systemet brukes til ulovlig virksomhet, som hvitvasking, korrupsjon og terrorfinansiering. Et av disse virkemidlene er å utføre en PEP-sjekk (Politically Exposed Person) av kunder. En politisk eksponert person har generelt sett større risiko for korrupsjon og bestikkelser knyttet til seg, og vil dermed være flagget for manuell behandling i f.eks en lånesøknad hos en bank.


## Kodeoppgave 📝
Årets kodeoppgave er en åpen oppgave relatert til KYC. Det er opp til dere hvilken teknologi dere bruker til oppgaven og hvordan den løses. Det er dermed mulig å løse den uavhengig av om du foretrekker backend, frontend eller hele stacken.
Det viktigste er at dere lager en applikasjon eller et API som gjør det mulig å utføre KYC sjekker av enkelt individer og/eller personer i et selskap.

*Se avsnittet som omtaler 'krav til innlevering' for **minimumskravet**.*


## Forslag til oppgaver:
**a) Lag en enkel webapp som lar brukeren utføre en KYC-sjekk av én person.**

**b) Implementer ditt eget KYC API som returnerer treff på enkeltpersoner og/eller selskap.**
* *Du velger fritt hvilken oppgave du vil gjøre. men oppfordres til å gi et forsøk på begge.*


**Mulige Utvidelser av a) og b)**
 - Publiser webappen og/eller APIet slik at de er tilgjengelig via HTTP
   - Kan f.eks publiseres til azure, google cloud, heroku, surge eller kanskje din egen server?
 - Utvide KYC/PEP sjekken til å sjekke alle personer i et foretak istedenfor bare én person.
   - Visualisere sjekken på en kreativ og oversiktelig måte?
#
Vi presiserer at kandidater står fritt til å utforske problemstillingen slik de selv ønsker (etter minimumskravet)
* Hvis du er tryggest på front-end og ikke ønsker å knote med et eget API så er dette ikke noe problem.
*  Kanskje back-end er mer din greie? Bruk heller mesteparten av tiden din her.

# Stacc KYC API / Data
I forbindelse med kodeoppgaven har vi laget et enkelt API (express.js), med noen få endepunkter som kan hjelpe deg med å komme i gang med oppgaven:
* Her kan du hente data fra [brønnøysundregisteret](https://www.brreg.no/) og [open sanctions](http://opensanctions.org/) som du kan benytte deg av for å utføre en PEP sjekk av personer og selskap.
* Du velger helt selv om du vil konsumere vårt API, eller benytte deg av vedlagt test data ([pep.csv](https://raw.githubusercontent.com/hpl002/stacc-code-challenge-public/master/pep.csv)) i repo for å utføre PEP sjekken.

API'et er tilgjengelig på: https://code-challenge.stacc.dev/
  * Merk at alle requests går via `/api`
  * `/docs` ruter tilbake til dette repoet
  *  Alle API spørringer er dokumentert i [postman](https://www.postman.com/).
#


**Eksempel Spørringer / Postman Collection**: Vi har laget en postman-collection, med oversikt over ulike API endepunkter som kan benyttes for å løse ulike oppgaver. Vi anbefaler deg å "forke" samlingen slik at du kan teste ut API'et og hente ut ulike data.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/16040688-74d4dc53-b65b-457c-8865-b5c4d6d4fdc5?action=collection%2Ffork&collection-url=entityId%3D16040688-74d4dc53-b65b-457c-8865-b5c4d6d4fdc5%26entityType%3Dcollection%26workspaceId%3Df408e47c-588c-4301-ba9f-6838a7f3b57a)

#
## Krav til innlevering:
1. Oppgaven må i det minste kunne utføre en enkel PEP sjekk av én person (enten via en app eller et API).
   *  Vi oppfordrer deg til å utvide på oppgaven slik du vil, og være kreativ i din besvarelse.
2. Oppgaven må publiseres på github (gjerne i et *public* repositorium)
   * Vi oppfordrer kandidater til å bruke **git** slik at vi sammen kan se igjennom commits og historikk.
   * Om du ønsker å holde denne privat så må du sende zip.
3. Alle oppgaver må inneholde en *readme.md* fil som beskriver prosjektet i korte trekk. Følg [denne linken for mal.](https://github.com/hpl002/stacc-code-challenge-public/blob/master/readmeTemplate.md)
   * Her dokumenterer og kommenterer du smått underveis. Spesielt viktig at det medfølger gode instrukser som beskriver hvordan prosjektet kjøres lokalt.
*Husk at dette ikke bare skal kjøre på din egen maskin!*
4. **Innleveringer sendes inn til samme person som sendte deg oppgaven**  
   **Enten link til offentlig repo eller .zip**
 - Vi foretrekker og anbefaler link til offentlig repo


# Lykke til! ✌️

Vi har opprettet en egen Slack kanal for spørsmål relatert til oppgaven, ikke nøl med å skrive til oss skulle noe være uklart eller om det oppstår problemer underveis i forbindelse med oppgaven. Alternativt kan dere sende oss en mail (litt tregere responstid over e-post, vi foretrekker slack 👍🙂)

## Slack Kanal

[![Joing us on Slack](https://99designs-blog.imgix.net/blog/wp-content/uploads/2018/07/add-to-slack-button.png?auto=format&q=60&fit=max&w=930)](https://join.slack.com/share/enQtMzc1NzExNTI5NTgxMi0wNmRkMWQyNDU5ZDk0YzIzOTliZmZlYWIwNmE0M2FkYTczN2E4NmQ4MTQwMmRmMDAxY2ViYWZiNjg0OTRjYmYy)

## E-post 📬 
Spørsmål om oppgaven sendes hit:
* ariens@stacc.com
* hermanp@stacc.com


