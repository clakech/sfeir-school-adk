<!-- .slide: class="transition" -->

# Outils Gemini natifs

##==##

<!-- .slide: class="with-code" -->

# Google Search Tool

```python[2,9-10]
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="basic_search_agent",
    model="gemini-2.0-flash",
    description="Agent to answer questions using Google Search.",
    instruction="I can answer your questions by searching the internet. Just ask me anything!",
    # google_search is a pre-built tool which allows the agent to perform Google searches.
    tools=[google_search]
)
```

| ✅ **Bons cas d'usage** | ❌ **À éviter** |
|------------------------|-----------------|
| Recherche d'actualités récentes | Données privées d'entreprise |
| Vérification de faits et données | Informations hautement spécialisées |
| Exploration d'informations publiques | Calculs ou analyses complexes |
| Recherche de documentation technique | Données nécessitant une fraîcheur < 1 minute |
| Comparaison de produits/services |  |

Notes:
- Google Search = données publiques du web
- Limité par ce qui est indexé par Google
- Pas de contrôle sur les sources exactes
- Pour données privées → utiliser RAG ou databases
- Complémentaire aux autres tools

##==##

<!-- .slide: class="with-code" -->

# Code Execution Tool

```python[2,7,9]
from google.adk.agents import LlmAgent
from google.adk.code_executors import BuiltInCodeExecutor

code_agent = LlmAgent(
    name="calculator_agent",
    model="gemini-2.0-flash",
    code_executor=BuiltInCodeExecutor(),
    instruction="""You are a calculator agent.
    When given a mathematical expression, write and execute Python code to calculate the result.
    Return only the final numerical result as plain text, without markdown or code blocks.
    """,
    description="Executes Python code to perform calculations.",
)
```

Notes:
- Gemini génère le code ET l'exécute
- Environnement isolé côté Google
- Permet calculs précis et visualisations
- Librairies Python disponibles : numpy, pandas, matplotlib, etc.
- Pas d'accès réseau ou filesystem

##==##

<!-- .slide -->

# Code Execution : Capacités

**Ce que Code Execution peut faire :**

| Catégorie | Exemples |
|-----------|----------|
| **Calculs** | Mathématiques complexes, statistiques |
| **Data science** | Analyse de datasets, transformations |
| **Visualisation** | Graphiques avec matplotlib/seaborn |
| **Traitement de données** | Parsing, nettoyage, agrégation |
| **Simulations** | Monte Carlo, modèles numériques |


Notes:
- Très puissant pour tâches analytiques
- Évite les erreurs de calcul du LLM
- Peut générer des visualisations complexes
- Librairies scientifiques pré-installées
- Résultats déterministes et vérifiables

##==##

<!-- .slide -->

# Code Execution : Limites et sécurité

❌ **Non disponible :**
- Accès réseau (pas d'appels HTTP/API)
- Accès au système de fichiers
- Installation de packages tiers
- Exécution de commandes système
- Opérations longues (timeout ~30s)

<br>

✅ **Sécurité :**
- Pas d'accès aux données de l'utilisateur
- Pas de persistance entre exécutions
- Chaque exécution est isolée

Notes:
- Les limites sont pour la sécurité
- Pas de risque d'injection ou d'exfiltration
- L'environnement est éphémère
- Pour des besoins avancés → GKE Code Executor
- Timeout court = éviter les boucles infinies

##==##

<!-- .slide -->

# GKE Code Executor

Exécution du code déportée dans un Pod spécifique et non sur l'infra de l'agent ADK

Meilleure sécuritée, mais quelques pré-requis:

- L'agent ADK doit être déployé dans un cluster GKE avec un node pool utilisant gVisor
- Le compte de service associé à l'agent doit pouvoir
  - Créer, surveiller, supprimer des jobs dans le cluster
  - Créer des configmaps pour injecter le code à exécuter
  - Récupérer la liste des pods et accéder aux logs des pods
- L'application doit aussi avoir la librairie adk avec l'add-on GKE `pip install google-adk[gke]`
##==##

<!-- .slide: class="with-code" -->

# Utilisation du GKE Code Executor

```python
from google.adk.agents import LlmAgent
from google.adk.code_executors import GkeCodeExecutor

gke_executor = GkeCodeExecutor(
    namespace="agent-sandbox",
    timeout_seconds=600,
    cpu_limit="1000m",  # 1 CPU core
    mem_limit="1Gi",
)

gke_agent = LlmAgent(
    name="gke_coding_agent",
    model="gemini-2.0-flash",
    instruction="You are a helpful AI agent that writes and executes Python code.",
    code_executor=gke_executor,
)
```

Attention aux droits d'accès au compte de service dans le namespace configuré

<!-- .element: class="admonition warning" -->

##==##

<!-- .slide -->

# Google Cloud Tools

Les Google Cloud Tools permettent de connecter facilement vos agents ADK aux services Google Cloud et à de nombreux systèmes d'entreprise (Salesforce, SAP, etc.).

**Cas d'usage principaux :**
- Appeler des APIs custom hébergées sur Apigee
- Utiliser des connecteurs pré-construits (Salesforce, Workday, etc.)
- Orchestrer des workflows d'automatisation (Application Integration)
- Accéder à des bases de données (Spanner, AlloyDB, Postgres...)

Ces outils s'intègrent nativement dans ADK et facilitent l'accès sécurisé à vos ressources cloud.

##==##

<!-- .slide -->

# Apigee API Hub Tools

Permet de transformer n'importe quelle API documentée dans Apigee API Hub en outil utilisable par un agent.

**Étapes clés :**
1. Générer un access token avec `gcloud auth print-access-token`
2. Vérifier les permissions IAM (ex : `roles/apihub.viewer`)
3. Créer un outil avec `APIHubToolset` en fournissant le token et le nom de ressource API
4. Ajouter l'outil à votre agent ADK

**Exemple d'intégration :**
```python
from google.adk.tools.apihub_tool.apihub_toolset import APIHubToolset
sample_toolset = APIHubToolset(
  name="apihub-sample-tool",
  description="Sample Tool",
  access_token="...",
  apihub_resource_name="..."
)
```

##==##

<!-- .slide -->

# Application Integration Tools

Donne accès à plus de 100 connecteurs d'entreprise (Salesforce, ServiceNow, JIRA, SAP...) et permet d'orchestrer des workflows complexes.

**Fonctionnalités :**
- Supporte les applications SaaS et on-premise
- Permet la fédération de recherche sur plusieurs systèmes
- S'appuie sur les rôles IAM pour la sécurité

**Exemple de création d'un outil :**
```python
from google.adk.tools.application_integration_tool.application_integration_toolset import ApplicationIntegrationToolset
connector_tool = ApplicationIntegrationToolset(
  project="my-project",
  location="us-central1",
  connection="my-connection",
  entity_operations={"Account": ["LIST"]},
  actions=["action1"],
  service_account_json='{...}'
)
```

##==##

<!-- .slide -->

# Sécurité et Authentification

Les Google Cloud Tools s'appuient sur les mécanismes d'authentification Google Cloud :
- Access token (pour développement)
- Service Account (recommandé en production)
- Support de l'OAuth2 pour les connecteurs dynamiques

**Bonnes pratiques :**
- Toujours limiter les permissions IAM au strict nécessaire
- Privilégier les comptes de service pour la production
- Les credentials ne doivent jamais être exposés dans le code source
