# Lærlingoppgave: Jira DataCenter

**Mål:** Målet med denne oppgaven er å sette opp en Jira DataCenter-installasjon med to servere i et kluster og bli kjent med automatisering og dokumentasjon av prosessen.

## Trinn for trinn:

### Forberedende:

1. Installer **GIT** og **VS Code**
2. Lær grunnleggende programmering i **Python**
3. Opprette et Github repo for dokumentasjon

### Grunnoppgave:

#### Serverforberedelse:

1. Bestill to servere via **Basta** (vår interne serverbestillingsapp).
2. Verifiser at du har tilstrekkelig maskinvare- og nettverksressurser for serverne (sjekk minimum hardware requirements hos Atlassian).
3. Bestill et dns-oppslag (f.eks `jira-dev.adeo.no`)

#### Enkel Jira-installasjon:

1. Installer Jira på den første serveren ved hjelp av den innebygde databasen.
2. Utfør grunnleggende konfigurasjon av Jira for å sikre at det fungerer som forventet.
3. Bestill server-sertifikat (`gimmicert` kan brukes)

#### Clusteroppsett:

1. Bestill nødvendige ressurser (database og NFS-område)
2. Endre config for Jira til å fungere i et cluster.
3. Konfigurer den andre serveren for å bli med i Jira-clusteret.
4. Sett opp et delt filområde (NFS) for Jira DataCenter-installasjonen slik at begge serverne kan aksessere det.
5. Start begge servere og sjekk at de både kommuniserer og fungerer

#### Dokumentasjon:

1. Dokumenter hele oppsetts- og konfigurasjonsprosessen trinnvis på en GitHub-repo.
2. Inkluder skjermbilder, kodeeksempler og eventuelle feilsøkingstips.

### Utfordring (Strekk-mål):

#### Automatisering via Ansible:

1. Bruk Ansible til å automatisere installasjons- og konfigurasjonsprosessen for Jira DataCenter.
2. Verifiser at Ansible-oppsettet fungerer som forventet ved å utføre en testinstallasjon.

#### Jira API-utforskning:

1. Bli kjent med **JIRA API**.
2. Skriv et enkelt script for å opprette og søke etter saker i Jira ved hjelp av API-et.
