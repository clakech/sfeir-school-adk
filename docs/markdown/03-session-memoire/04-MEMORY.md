<!-- .slide: class="transition" -->

# Memory

## Persistance et Recherche Sémantique

##==##

<!-- .slide -->

# Memory : Vue d'ensemble

## Au-delà de la session

<br>

La **Memory** permet à l'agent de se souvenir d'informations provenant de **sessions passées** ou de **documents externes**.

<br>

<div style="font-size: 1.6em;">

```markdown
Session 1 (Hier) : "J'adore le Park Hyatt Tokyo"
Session 2 (Aujourd'hui) : "Je veux retourner dans mon hôtel préféré."
                           ↓
Agent : "Vous parlez du Park Hyatt Tokyo ?"
```

</div>

<br>

### Caractéristiques :
- 🧠 Connaissances long-terme
- 🔍 Recherche sémantique (pas uniquement des mots-clés)
- 🔄 Cross-session : retrouver des infos d'autres conversations

Notes:
Memory = RAM de l'agent, State = Mémoire de travail de la session

##==##

<!-- .slide -->

# RAG : Comment ça marche ?

## Retrieval Augmented Generation

<br>

<div style="font-size: 1.1em;">


1. **Ingestion :** Sessions → Chunks → Embeddings → Vector DB

<br>
<br>

2. **Recherche :**   Query → Embedding → Similarité → Retrieval

<br>
<br>

3. **Augmentation :**   Context + Query → LLM → Response

</div>

<br>
<br>

### Pipeline simplifié par ADK :
1. **add_session_to_memory()** : Ingestion automatique
2. **search_memory()** : Recherche vectorielle
3. **PreloadMemoryTool** : Injection dans le contexte

Notes:
ADK abstrait toute la complexité du RAG

##==##

<!-- .slide -->

# Quand utiliser Memory ?

## Cas d'usage typiques

<br>

### 🔄 Continuité entre sessions

- Se souvenir des préférences d'une visite à l'autre

<br>
<br>

### 📚 Base de connaissances

- Documentation, FAQ, catalogue produits

<br>
<br>

### 🤝 Personnalisation long-terme

- Assistant qui apprend de chaque interaction


<br>
<br>

Utilisez Memory quand l'information doit **survivre à la session**

<!-- .element: class="admonition important" -->

Notes:
Si c'est important pour les prochaines conversations → Memory
Si c'est juste pour la conversation en cours → State

##==##

<!-- .slide: class="with-code max-height" -->

# MemoryService : Implémentation

## Code Python

<div style="font-size: 1.2em;">

```python
from google.adk.memory import InMemoryMemoryService

# Initialiser le service
memory_service = InMemoryMemoryService()

# Ingestion : Sauvegarder une session terminée
await memory_service.add_session_to_memory(
    session,
    include_state=True  # Indexer aussi le State
)

# Recherche : Retrouver des informations
results = await memory_service.search_memory(
    query="hôtel préféré Tokyo",
    limit=3
)

for result in results:
    print(f"{result.text} (Score: {result.score})")
```

</div>

Notes:
include_state=True permet de retrouver aussi les préférences stockées dans le State

##==##

<!-- .slide: class="with-code" -->

# Intégration via Tools

## PreloadMemoryTool : Le pattern automatique

<div style="font-size: 1.2em;">

```python
from google.adk.tools.preload_memory_tool import PreloadMemoryTool

# Cet outil s'exécute AVANT chaque tour
memory_tool = PreloadMemoryTool(
    memory_service=memory_service,
    max_results=2
)

agent = LlmAgent(
    name="TravelAgent",
    tools=[memory_tool],
    instruction="""
Tu es un agent de voyage.
Utilise le contexte fourni pour personnaliser les réponses.
"""
)
```

</div>


<div style="font-size: 0.75em;">

**Flow :** User Input → Memory Search → Context Injection → LLM → Response

</div>

<!-- .element: class="admonition tip" -->

Notes:
L'agent n'a même pas besoin de savoir qu'il utilise la mémoire

##==##

<!-- .slide -->

# Backends de MemoryService

## Du prototype à la production


| Backend | Recherche | Setup | Cas d'usage |
|---------|-----------|-------|-------------|
| **InMemory** | Mots-clés | Aucun | Dev, Tests |
| **VertexAI Memory Bank** | Vectorielle | GCP | Production |

<br>

<div style="font-size: 1.5em;">

```python
# Exemple avec Vertex AI
from google.adk.memory import VertexAiMemoryBankService

memory_service = VertexAiMemoryBankService(
    project_id="my-gcp-project",
    location="us-central1",
    memory_bank_id="customer-preferences"
)
```

</div>

<br>

<div style="font-size: 0.8em;">

Vertex AI Memory Bank gère automatiquement l'extraction de "souvenirs significatifs" depuis les sessions.
<!-- .element: class="admonition warning" -->

</div>

Notes:
Vertex AI est beaucoup plus intelligent qu'InMemory pour extraire ce qui est important

##==##

<!-- .slide: class="with-code max-height" -->

# Exemple pratique : Agent avec mémoire

## Cycle complet

```python
# 1. Setup des services
session_service = InMemorySessionService()
memory_service = InMemoryMemoryService()

# 2. Session 1 : Première conversation
session1 = await session_service.create_session(...)
# ... Conversation: "J'adore la cuisine japonaise" ...
await memory_service.add_session_to_memory(session1)

# 3. Session 2 : Nouvelle conversation (le lendemain)
session2 = await session_service.create_session(...)

# 4. L'agent recherche automatiquement (via PreloadMemoryTool)
# Query: "recommandations restaurant"
# Memory trouve: "User adore la cuisine japonaise"

# 5. L'agent répond intelligemment
# "Je vous recommande ces restaurants japonais..."
```

Notes:
Deux sessions différentes, mais l'agent se souvient grâce à Memory
