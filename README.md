# AWS-workshop

### Lambda!
Her skal vi leke oss litt med lambda, et ypperlig Function As A Service (FaaS) miljø vi kan bruke til å kjøre koden vår.
Vi kommer også til å ta i bruk et rammeverk som heter serverless. Dette rammeverket skal hjelpe poss med å deploye og håndtere av prosjektet og koden vår.

<details>
  <summary>Hva var lambda igjen? 🤔</summary>
  En lambda er, generelt forklart, en kodesnutt eller funksjon som kjøres enten ved et bestemt tidspunkt eller ved at en bestemt hendelse trigger funksjonen. For eksempel så kan man ønske at en ny jobbsøknad i databasen skal trigge en epostutsendelse til søker. En fordel med Lambda er at man kun betaler for ressursene man bruker under kjøring, og ingenting ellers. Lambda er en Function as a Service, noe som betyr at man ikke trenger å sette opp noe konfigurere noe underliggende infrastruktur.
</details>

Målet med workshopen er ikke å bli ferdig; det er å teste ut og bli litt kjent med sky! Ta det i ditt tempo og spør om hjelp om du trenger det.

### Prereqs
1. Installer aws cli (MacOS: `brew install awscli`).
2. Kjør kommandoen `aws configure`. 

3. Du får beskjed om å legge inn følgende verdier én etter én:
- AWS Access Key ID [********************]:  `(fra epost)`
- AWS Secret Access Key [********************]: `(fra epost)`
- Default region name: `eu-west-1`
- Default output format: `json`

Hvis du ønsker å gjøre endringer på dette senere så finner du filen under `~/.aws/credentials`.

4. Installer [serverless](https://www.serverless.com/framework/docs/getting-started/).

## Oppgave 1
1. I terminalen din, naviger til repoet hvor denne READMEen kjører (hvis du har klonet repoet), eller en annen mappe du vil bruke for denne workshoppen. 
2. Kjør kommandoen `serverless` der. Dette initierer et nytt serverless prosjekt. 
- Du får nå valg om type repo du vil lage. Du kan bevege deg opp eller ned i CLIet ved hjelp av piltastene. Man velger ved å trykke enter. Velg `starter` Python, . Jeg gikk for AWS - Python - Starter.
- Gi prosjektet et navn - velg noe unikt som inneholder navnet ditt. Hvis ikke kan det bli vanskelig å finne det igjen blandt alle andre sine.   
  Spør den om du vil lage en serverless konto kan du svare `nei`. 
  Spør den om å logge inn på et dashboard kan du svare `nei`.
  Spør den om du vil deploye prosjektet ditt svarer du `nei`. 
3. I `serverless.yml` legg inn `region: eu-west-1` under `provider`.
4. Endre `handler.js` til å ha en personlig melding.
5. Deploy ved hjelp av kommandoen `serverless deploy`.

🙌 Bra jobba! 🙌 

Du har nettopp laget en funksjon (det du finner i handler.py), laget et oppsett for å kunne håndtere og deploye filene dine opp i skyen (serverless.yml filen) og lastet filene dine opp i Lambda (serverless deploy kommandoen)! I neste oppgave skal vi se litt på hva vi egentlig har dytta opp dit.

<details>
<summary> <h3>🚨 Feilmelding på deploy? 🚨</h3></summary>

#### `Error: This command can only be run in a Serverless service directory.`

```Environment: darwin, node 18.2.0, framework 3.14.0, plugin 6.2.1, SDK 4.3.2
Docs:        docs.serverless.com
Support:     forum.serverless.com
Bugs:        github.com/serverless/serverless/issues

Error:
This command can only be run in a Serverless service directory. Make sure to reference a valid config file in the current working directory if you're using a custom config file
```
💡 Løsning: pass på at du er inne i riktig mappe når du kjøerer `serverlss deploy`
<br>
<br>
#### `Error: The security token included in the request is invalid.`
```
Deploying testingTasks to stage dev (eu-west-1)

✖ Stack testingTasks-dev failed to deploy (0s)
Environment: darwin, node 18.2.0, framework 3.14.0, plugin 6.2.1, SDK 4.3.2
Credentials: Local, "default" profile
Docs:        docs.serverless.com
Support:     forum.serverless.com
Bugs:        github.com/serverless/serverless/issues

Error:
The security token included in the request is invalid.
```

💡 Løsning: Du har trolig feil `Access key` og `Access Secret`. Kjør `aws configure` om igjen og pass på å lime inn riktige verdier fra e-posten. 
  Fortsatt trøbbel? Ta kontakt med en av kursholderne så de kan hjelpe deg å generere en ny key + secret.

</details>


## Oppgave 2
Nå skal vi ta å sjekke ut UIen og se hvordan koden kjører!
1. Logg inn på https://console.aws.amazon.com/
  - Velg IAM user
  - account-id er `bekk-skyskolen`
  - brukernavn er bekk-eposten din
  - passord ser du på tavla. 
2. I menyen i toppen søk etter og velg "lambda". Under "Functions" finn din funksjon!
3. Trykk på den oransje "TEST"-knappen. Får du opp et vindu som spør om _configure test event_ så bare skriv et navn, f.eks. "test" og trykk save.
4. 💥 BAM! Du har nå kjørt funksjonen din! Woop! 🥳🎉

<details>
  <summary>Hvor kan jeg se outputen fra lambdaen min?</summary>
</details>

<details>
<summary> <h3>🚨 Troubleshooting 🚨</h3></summary>
💡 Oppe til høyre ved siden av brukernavnet ditt står det en "region". AWS har en tendens til å sende en til feil region. Vi henger i eu-west-1. 

Se [bildene i losningsforslag2-mappen](https://github.com/halvorhm/skyskolen-lambda-workshop/tree/main/losningsforslag/oppgave2) for hvor du skal trykke.
</details>


## Oppgave 3
I denne oppgaven skal vi bli kjent med S3-bøtter! 

<details>
  <summary>Hva er en S3-bøtte? 🤔</summary>
  S3 står for Simple Storage Service og brukes til å holde data. Tenk på det som en litt fancy delt disk - slik som Google Drive eller Dropbox.
</details>

1. Først skal vi opprette en bøtte. Bøtter er unike i verden og må ha et helt unikt navn. Brukt derfor en kombinasjon av navnet ditt e.l.
For å opprette en bøtte bruker du kommandoen `aws s3 mb s3://<mitt navn på min bøtte>`.

2. La oss deretter skrive om funksjonen vår i handler.js/handler.py til å liste alle s3-bøttene som eksisterer i regionen vi jobber i på AWS! Et grunnlag for å få til dette finner du [her for python](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html#list-existing-buckets). 

_OBS_ Hvis du endrer på funksjonsnavnet eller lager en ny funksjon må du vite at en Lambda-function må ta inn parameterne `(event, context)` eks: `def hello(event, context)`. Du trenger ikke bruke event eller context i funksjonen din, men en lamda-funksjon må ta disse inn for å kjøre (i hvertfall i python).

*Dersom du allerede deployer koden din og tester lambdaen på nett så feiler den - det er meningen. Det skal løses i neste oppgave, men vi skal kjøre lokalt nå først.*

3. For å teste koden så kan vi "kjøre" en lambda-funksjon lokalt ved hjelp av en fin liten serverless-kommando. 
Vi bruker da `serverless invoke local --stage dev --function hello`. 
`stage` viser til hvilket miljø vi ønsker å gjøre dette i. Under utvikling er det vanlig å ha utviklingsmiljø og produksjonsmiljø. Under workshopen bruker vi `dev` som står for development. `function` viser til funksjonsnavnet ditt i serverless.yml (DOBBELTSJEKK DENNE). 

4. Når koden fungerer og du får lista ut alle bøttene, kjør en ny `serverless deploy --stage dev` for å dytte koden din ut.

Hvis du kjører denne i lambdaen vil du se at den feiler med et tilgangsproblem. Dette løser vi i oppgave 4!

<details>
<summary> <h3>🚨 Troubleshooting 🚨</h3></summary>

💡 Hvis du kjører python og prøver å kjøre lambdaen lokalt kan det hende du må installere boto3. 
For å løse følgende feilmelding ``` ModuleNotFoundError: No module named 'boto3' ```  kjør ``` pip3 install boto3 ``` i terminalen.

<br>

💡 Har du endret funksjonen din og får nå feilmeldingen: ``` TypeError: printBuckets() takes 0 positional arguments but 2 were given ```? Løsning: funksjonen din må ta inn parameterne `(event, context)` eks: `def hello(event, context)`. Du trenger ikke bruke event eller context i funksjonen din, men en lamda-funksjon må ta disse inn for å kjøre.
</details>

## Oppgave 4. 
Som nevnt har ikke lambda-funksjonen tilgang til å lese s3-bøttene. 
Dette kan vi fikse! Og akkurat nå mens vi tester er vi litt frekke og putter på litt ekstra tilganger.

Legg inn biten `iamRoleStatements` i `serverless.yml` fil som vist under. Dette gir lambdaen tilgang tilå gjøre _alle_ s3-kommandoer mot _alle_ s3-bøtter.  

```yaml
provider:
  name: aws
  runtime: python3.8
  lambdaHashingVersion: 20201221
  region: eu-west-1
  iamRoleStatements:
    - Effect: 'Allow'
      Action:
        - 's3:*'
      Resource:
        - 'arn:aws:s3:::*'
```
Deploy på nytt! Nå burde ting funke!

<details>
<summary> Hvordan deployer man? </summary>

Kjør kommandoen `serverless deploy --stage dev`

</details>


## Oppgave 5
Nå prøver vi oss på litt løsere oppgaver, hvor vi må sjekke dokumentasjonen til serverless og sjekke events/triggers. 

Du finner dokumentasjon på hvordan du gjør ting mot s3 i boto3 biblioteket hvis du bruker python. 
Alle metoder tilgjengelig på boto3 klienten: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#id205

For serverless kan du se lenken under til deres dokumentasjon.
https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#listObjectsV2-property

### Oppgave 5.0
Start med å laste opp noe i bøtta di som du lagde i oppgave 3! Kanskje et bilde eller et word-dokument. Ikke velg noe sensitivt!

Dette kan du gjøre ved hjelp av ClickOps eller ved hjelp av en kommando i terminalen. 

Dersom du vil gjøre det i terminalen, så kan dette være en nyttig lenke: https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html
PS! Bla ned til avsnittet med tittelen "Example" 

### Oppgave 5.1
List innholdet i bøtten din! Bruk det vi gjorde i oppgave 3 (og lenkene der) som utgangspunkt og modifiser funksjonen din ved hjelp av dokumentasjonen. 

Nyttig lenke:
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_objects_v2

### Oppgave 5.2
Lag en event som trigger når nye objekter blir lagt til å bøtta. Test it!

Nyttig lenke: 
https://www.serverless.com/framework/docs/providers/aws/events/s3

### Oppgave 5.3 
Legg til noe om kron jobb??


