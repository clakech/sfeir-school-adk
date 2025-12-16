# 05-workshop-advanced instructions

Dans ce lab vous allez créer un agent de planification de voyage qui démontre les fonctionnalités avancées de l'ADK : structured output, callbacks/plugins, et optimisation du contexte.

## How to run?

```Bash
cd ./steps/05-workshop-advanced
```

# TP

## Création de l'agent

Dans ce TP nous allons créer un agent de voyage avec des fonctionnalités avancées, pour cela lancer la commande suivante:

```Bash
adk create travel_agent
```

La commande va vous demander de choisir un model et un backend, choisissez:
- `1. gemini-2.5-flash`
- `2. Google AI`

Ensuite générez une clef d'API depuis AI Studio (https://aistudio.google.com/apikey) ou demandez une clef d'api au formateur.

## Partie 1: Structured Output (15 min)

### 1.0 Installation de Pydantic

Assurez-vous que Pydantic est installé dans votre environnement:

```Bash
pip install pydantic
```

### 1.1 Définir les schémas Pydantic

Créez un fichier `schemas.py` dans le dossier `travel_agent/`.

Dans ce fichier, importez Pydantic et complétez les deux schémas pour refléter:

**Schéma d'entrée `TravelRequest`** doit contenir:
- `destination` (str) - La ville ou pays de destination
- `budget` (float) - Budget en euros (≥ 0)
- `days` (int) - Nombre de jours (≥ 1)
- `interests` (list[str]) - Liste des centres d'intérêt (culture, nature, gastronomie, etc.)

**Schéma de sortie `TravelResponse`** doit contenir:
- `destination` (str)
- `daily_budget` (float)
- `activities` (list[str])
- `accommodation_type` (str)
- `estimated_total_cost` (float)

### 1.2 Créer un agent avec input/output schemas

Dans le fichier `agent.py`, importez vos schémas et configurez l'agent:

```python
from google.adk.agents.llm_agent import Agent
from .schemas import TravelRequest, TravelResponse

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Travel planning agent with structured inputs and outputs',
    instruction="""
        You are a travel planning assistant. Based on the user's destination, budget, days, and interests,
        create a detailed travel plan including daily activities, accommodation recommendations, and cost estimates.
        Ensure your response follows the exact structure required.
    """,
    input_schema=TravelRequest,
    output_schema=TravelResponse
)
```

### 1.3 Tester l'agent

Lancez `adk web` et testez avec une requête structurée JSON. Vous devriez recevoir une réponse JSON structurée.

Exemple de requête:

```json
{
  "destination": "Paris",
  "budget": 1500,
  "days": 5,
  "interests": ["culture", "gastronomie"]
}
```

## Partie 2: Callbacks & Plugins (20 min)

### 2.1 Créer un callback de validation

Créez un fichier `callbacks.py` dans le dossier `travel_agent/`.

Les callbacks dans l'ADK utilisent un objet `CallbackContext` pour accéder aux informations de l'invocation.

**Structure d'un callback avant agent:**

```python
from google.adk.agents.callback_context import CallbackContext
from .schemas import TravelRequest

def validate_and_log(callback_context: CallbackContext):
    """Callback exécuté avant l'agent"""
    # Extraire le message utilisateur du contexte
    input_data = callback_context._invocation_context.user_content.parts[0].text
    # Parser le JSON avec votre schéma Pydantic
    input_data = TravelRequest.model_validate_json(input_data)

    # TODO: Ajouter votre logique de validation ici
```

**Votre callback doit:**
- Afficher un warning si le `budget` est inférieur à 200€
- Afficher un warning si le budget journalier (`budget / days`) est inférieur à 50€
- Lever une `ValueError` avec un message approprié si le budget total est inférieur à 100€

### 2.2 Intégrer le callback à l'agent

Modifiez votre `agent.py` pour importer et utiliser le callback:

```python
from google.adk.agents.llm_agent import Agent
from .schemas import TravelRequest, TravelResponse
from .callbacks import validate_and_log  # Ajouter cet import

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Travel planning agent with monitoring',
    instruction="""...""",
    input_schema=TravelRequest,
    output_schema=TravelResponse,
    before_agent_callback=validate_and_log,  # Ajouter cette ligne
)
```

**Testez:** Relancez `adk web` et essayez avec un petit budget (ex: 150€) - vous devriez voir vos warnings dans le terminal.

### 2.3 Créer un plugin d'audit

Les plugins permettent d'appliquer des callbacks à **tous** les agents d'une application.

Créez un fichier `plugins.py` dans le dossier `travel_agent/`.

**Structure d'un plugin:**

```python
from google.adk.plugins import BasePlugin
from google.adk.agents import InvocationContext
from google.genai import types
from .schemas import TravelRequest

class TravelAuditPlugin(BasePlugin):
    """Plugin pour auditer toutes les interactions du système de voyage"""

    def __init__(self):
        super().__init__(name="TravelAuditPlugin")
        self.request_count = 0

    async def on_user_message_callback(
        self, invocation_context: InvocationContext, user_message: types.Content
    ) -> None:
        """Callback exécuté à chaque message utilisateur"""
        # TODO: Implémenter votre logique d'audit
        pass
```

**Votre plugin doit:**
- Incrémenter un compteur de requêtes
- Parser le message utilisateur avec `TravelRequest`
- Afficher un log formaté avec:
  - Le numéro de la requête
  - Le nom de l'agent (`invocation_context.agent.name`)
  - La destination
  - Le budget

### 2.4 Intégrer le plugin avec App

Pour utiliser un plugin, vous devez créer une `App` qui englobe votre agent.

Modifiez votre `agent.py` pour ajouter la configuration de l'App:

```python
from google.adk.agents.llm_agent import Agent
from google.adk.apps import App
from .schemas import TravelRequest, TravelResponse
from .callbacks import validate_and_log
from .plugins import TravelAuditPlugin

# Votre agent
root_agent = Agent(
    # ... configuration existante
)

# Configuration de l'application avec le plugin
app = App(
    name="travel_agent",
    root_agent=root_agent,
    plugins=[TravelAuditPlugin()],  # Le plugin s'applique à tous les agents
)
```

**Testez:** Relancez et vous devriez voir les logs du plugin en plus du callback.

## Partie 3: Context Optimization (15 min)

### 3.1 Ajouter un guide de voyage

Pour démontrer l'optimisation du contexte, ajoutez un guide de voyage statique dans vos instructions.

Dans `agent.py`, créez une constante `TRAVEL_GUIDE` contenant des informations détaillées sur plusieurs villes européennes (Paris, Londres, Rome, Barcelone, etc.) avec:
- Prix des monuments
- Coûts des restaurants
- Tarifs des transports
- Prix des hébergements

Puis intégrez ce guide dans les instructions de votre agent:

```python
TRAVEL_GUIDE = """
# Guide de Voyage Détaillé

## Paris
- Monuments: Tour Eiffel (25€), Louvre (17€), Arc de Triomphe (13€)
- Restaurants: Budget 15-80€/repas selon standing
- Transport: Navigo semaine 30€, ticket unique 2.10€
- Hébergement: Auberge 25-40€, Hôtel 2* 60-100€, Hôtel 4* 150-300€

# ... Ajoutez d'autres villes
"""

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    instruction=f"""
        You are an expert travel planning assistant with access to detailed city guides.

        {TRAVEL_GUIDE}

        Based on the user's destination, budget, days, and interests:
        1. Use the guide data to provide accurate pricing
        2. Calculate realistic daily budgets
        3. Suggest activities that match their interests and budget
        4. Recommend appropriate accommodation
        5. Provide a total cost estimate

        Always stay within the user's budget and be creative with free/low-cost activities if needed.
    """,
    input_schema=TravelRequest,
    output_schema=TravelResponse,
    before_agent_callback=validate_and_log,
)
```

### 3.2 Activer le Context Caching

Le context caching permet de réutiliser les parties statiques du contexte (comme le `TRAVEL_GUIDE`) sans les renvoyer à chaque requête.

Ajoutez la configuration de cache à votre App:

```python
from google.adk.agents.context_cache_config import ContextCacheConfig
from google.adk.apps import App

# ... votre agent ...

context_cache_config = ContextCacheConfig(
    min_tokens=2048,     # Cache si > 2048 tokens
    ttl_seconds=3600,    # Cache valide 1h
    cache_intervals=5,   # Mise à jour tous les 5 appels
)

app = App(
    name="travel_agent",
    root_agent=root_agent,
    plugins=[TravelAuditPlugin()],
    context_cache_config=context_cache_config,  # Ajouter le cache
)
```

**Ce que cela fait:**
- Le `TRAVEL_GUIDE` (statique) est mis en cache par Gemini
- Les requêtes suivantes sont plus rapides et moins chères
- Le cache est valide pendant 1 heure

### 3.3 Activer la compression d'événements (Bonus)

Pour les conversations longues, la compression résume automatiquement l'historique ancien.

```python
from google.adk.apps.app import EventsCompactionConfig

event_compaction_config = EventsCompactionConfig(
    compaction_interval=3,  # Compacter après chaque 3 invocations
    overlap_size=1,         # Chevauchement de 1 invocation
)

app = App(
    name="travel_agent",
    root_agent=root_agent,
    plugins=[TravelAuditPlugin()],
    context_cache_config=context_cache_config,
    events_compaction_config=event_compaction_config,  # Ajouter la compression
)
```

**Ce que cela fait:**
- Les anciens messages sont résumés automatiquement
- La conversation peut continuer indéfiniment
- Le contexte reste gérable même après 50+ échanges

## Test Final

1. Lancez `adk web`
2. Testez avec différentes destinations et budgets
3. Observez les logs de callbacks et du plugin dans le terminal
4. Vérifiez que les réponses respectent le schéma JSON

### Scénarios de test recommandés:

**Test 1 - Budget confortable:**
```json
{
  "destination": "Paris",
  "budget": 1500,
  "days": 5,
  "interests": ["culture", "gastronomie"]
}
```

**Test 2 - Petit budget (doit déclencher warnings):**
```json
{
  "destination": "Rome",
  "budget": 150,
  "days": 7,
  "interests": ["histoire", "architecture"]
}
```

**Test 3 - Budget trop bas (doit lever une erreur):**
```json
{
  "destination": "Barcelone",
  "budget": 80,
  "days": 4,
  "interests": ["plage", "tapas"]
}
```
