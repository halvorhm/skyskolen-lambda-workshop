# aws-testing

## Prereqs
Installer aws cli og legg inn credentials. Installer `serverless`.

## Lambda

### Oppgave 1
- Kjør kommandoen `serverless` i repoet. Dette burde initiere et nytt serverless prosjekt. Bruk ditt eget navn i navn på prosjektet. Når den spør om type repo, velg Node eller Python, litt etter hva du foretrekker. Når den spør om du vil lage en serverless konto kan du svare `nei`. 
- I `serverless.yml` legg inn `region: eu-west-1` under `provider`.
- Endre `handler.js` til å ha en personlig melding.
- Deploy ved hjelp av kommandoen `serverless deploy --stage dev`. 
- Gå til UIen og testkjør lambda-funksjonen din. Sjekk loggen for å se om meldingen din er skrevet.

## Oppgave 2
Nå skal vi liste alle s3-bøttene våre fra lambdaen! Et grunnlag for å få til dette finner du [her for node](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-creating-buckets.html) og [her for python](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html).


## Oppgave 3
La oss se litt på triggers. Først kan vi endre koden vår til å liste innholdet i en gitt bøtte ved hjelp av lenkene i oppgave 2. 
Deretter skal vi se litt på eventer for å trigge funksjonen vår! https://www.serverless.com/framework/docs/providers/aws/events/s3/ 

### Oppgave 3.1
Lag en cron-trigger så lambdaen kjører hvert minutt. Test det!

### Oppgave 3.2
Lag en event som trigger når nye objekter blir lagt til å bøtta. Test it!