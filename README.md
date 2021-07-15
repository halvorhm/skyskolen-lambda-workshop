# AWS-workshop

## Lambda!
Her skal vi leke oss litt med lambda, et ypperlig Function As A Service (FaaS) miljø vi kan bruke til å kjøre koden vår.
Vi kommer også til å ta i bruk et rammeverk som heter serverless for å kjenne litt på deploy og håndtering av prosjektet vårt.

### Prereqs
Installer aws cli (MacOS: `brew install awscli`).
Kjør kommandoen `aws configure`. Legg inn verdiene:
- Access Key (fra epost)
- Secret (fra epost)
- Default region name: eu-west-1
- Default output format: json

Hvis du ønsker å gjøre endringer på dette seinere så finner du filen under `~/.aws/credentials`.

Installer [serverless](https://www.serverless.com/framework/docs/getting-started/).

### Oppgave 1
- Kjør kommandoen `serverless` i repoet. Dette burde initiere et nytt serverless prosjekt. 
  Når den spør om type repo, velg `starter` Node eller Python, litt etter hva du foretrekker. Jeg gikk for AWS - Python - Starter.
  Bruk ditt eget navn i navn på prosjektet.   
  Spør den om du vil lage en serverless konto kan du svare `nei`. 
  Spør den om du vil deploye prosjektet ditt svarer du `nei`. 
- I `serverless.yml` legg inn `region: eu-west-1` under `provider`.
- Endre `handler.js` til å ha en personlig melding.
- Deploy ved hjelp av kommandoen `serverless deploy --stage dev`.

🙌 Bra jobba! 🙌

### Oppgave 2
Nå skal vi ta å sjekke ut UIen og se hvordan koden kjører!
- Logg inn på https://console.aws.amazon.com/
- I menyen i toppen søk etter og velg "lambda". Under "Functions" finn din funksjon!
- Trykk på den oransje "TEST"-knappen. Får du opp et vindu som spør om _configure test event_ så bare skriv et navn, f.eks. "test" og trykk save.
- BAM! Du har nå kjørt funksjonen din! Woop!

### Oppgave 3
For å få litt mer ut av dette enn en hello world tenkte jeg vi gjøre om funksjonen vår til noe som administrer litt med S3-bøtter. 

Nå skal vi liste alle s3-bøttene våre fra lambdaen! Et grunnlag for å få til dette finner du [her for node](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-creating-buckets.html) og [her for python](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html).

Hvis du har lyst til å teste koden lokalt så kan vi "kjøre" en lambda-funksjon lokalt ved hjelp av en fin liten serverless-kommando. 
Vi bruker da `serverless invoke local --stage dev --function hello`. 
`stage` må her være det samme som du har brukt ellers og `function` viser til det funksjonen din er deklarert som under `functions`i serverless.yml.

Se om du får lista opp alle bøttene! Når koden fungerer, kjør en ny `serverless deploy --stage dev` for å dytte koden din ut.

Hvis du kjører denne i lambda vil du se at den feiler med et tilgangsproblem. Dette løser vi i oppgave 4!

### Oppgave 4. 
Som nevnt har ikke lambda-funksjonen tilgang til å lese s3-bøttene. Dette kan vi fikse! Og akkurat nå mens vi tester er vi litt frekke og putter på litt ekstra tilganger.
Legg inn biten `iamRoleStatements` i din `serverless.yml` fil som vist under. Dette gir lambdaen tilgang tilå gjøre _alle_ s3-kommandoer mot _alle_ s3-bøtter.  

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


### Oppgave 3
La oss se litt på triggers. Først kan vi endre koden vår til å liste innholdet i en gitt bøtte ved hjelp av lenkene i oppgave 2. 
Deretter skal vi se litt på eventer for å trigge funksjonen vår! https://www.serverless.com/framework/docs/providers/aws/events/s3/ 

### Oppgave 3.1
Lag en cron-trigger så lambdaen kjører hvert minutt. Test det!

### Oppgave 3.2
Lag en event som trigger når nye objekter blir lagt til å bøtta. Test it!