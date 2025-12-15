<!-- .slide: class="transition" -->

# Session

## Le fil de conversation

##==##

<!-- .slide -->

# Session : Vue d'ensemble

## L'unité atomique de conversation

<br>

Une **Session** représente une conversation unique et continue entre un utilisateur et votre agent.

<br>

```
User:  "Bonjour"
Agent: "Bonjour ! Comment puis-je vous aider ?"
User:  "Quel temps fait-il ?"
Agent: "Je vérifie pour vous..."
```

<br>

### Caractéristiques :
- 🆔 Identifiant unique pour reprendre la conversation
- 📝 Historique chronologique complet (Events)
- 💾 Données contextuelles (State)

Notes:
Sans Session, l'agent ne se souviendrait pas que vous venez de dire bonjour

##==##

<!-- .slide -->

# Quand utiliser les Sessions ?

## Cas d'usage typiques

<br>

### 💬 Chatbots conversationnels
```
Support client, assistants personnels
```

<br>

### 🛒 Applications transactionnelles
```
E-commerce : maintenir le panier pendant la navigation
```

<br>

### 🎓 Applications pédagogiques
```
Tuteurs adaptatifs qui se souviennent de la progression
```

<br>

Utilisez Sessions dès que vous avez besoin de **continuité conversationnelle**

<!-- .element: class="admonition important" -->

Notes:
Toute application avec plus d'un échange utilisateur bénéficie des Sessions

##==##

<!-- .slide: class="with-code max-height" -->

# SessionService : Implémentation


## Code Python

<br>

<div style="font-size: 1.2em;">

```python
from google.adk.sessions import InMemorySessionService

# Initialiser le service
session_service = InMemorySessionService()

# Créer une nouvelle session
session = await session_service.create_session(
    app_name="travel_assistant",
    user_id="user_123"
)

print(f"Session créée : {session.id}")
# Output: Session créée : 550e8400-e29b-41d4-a716-446655440000
```

</div>

Notes:
L'ID est auto-généré (UUID) si vous ne le spécifiez pas

##==##

<!-- .slide: class="with-code" -->

# Cycle de vie d'une Session

## Ajout d'événements

<br>

### Enregistrer les interactions

<div style="font-size: 1.1em;">

```python
from google.adk.types import UserMessage, ModelResponse

# L'utilisateur envoie un message
user_event = UserMessage(text="Je veux aller à Tokyo")
await session_service.append_event(session, user_event)

# L'agent répond
model_event = ModelResponse(text="Pour quelles dates ?")
await session_service.append_event(session, model_event)

# Récupérer la session avec l'historique
loaded = await session_service.get_session(session.id)
print(f"Nombre d'événements : {len(loaded.events)}")
# Output: Nombre d'événements : 2
```

</div>


`append_event` met à jour automatiquement `last_update_time`

<!-- .element: class="admonition tip" -->

Notes:
Chaque interaction est stockée comme un Event typé

##==##

<!-- .slide -->

# Backends de SessionService

## Du développement à la production

<br>

| Backend | Persistance | Setup | Cas d'usage |
|---------|-------------|-------|-------------|
| **InMemory** | ❌ Non | Aucun | Dev, Tests |
| **Firestore** | ✅ Oui | GCP Project | Production |
| **SQLAlchemy** | ✅ Oui | Database | Production |

<br>

```python
# Production avec Firestore
from google.adk.sessions import FirestoreSessionService

session_service = FirestoreSessionService(
    project_id="my-gcp-project"
)
```


Ne jamais utiliser `InMemory` en production : toutes les conversations sont perdues au redémarrage.
<!-- .element: class="admonition warning" -->

Notes:
Le choix du backend ne change pas le code de votre agent

##==##

<!-- .slide: class="with-code max-height" -->

# Exemple pratique : Chat multi-tours

## Conversation complète

<div style="font-size: 1.1em;">

```python
# 1. Créer la session
session = await session_service.create_session(
    app_name="travel_bot", user_id="alice"
)

# 2. Premier tour
await session_service.append_event(
    session, UserMessage(text="Je veux voyager")
)
# ... L'Agent répond ...

# 3. Deuxième tour (même session)
await session_service.append_event(
    session, UserMessage(text="Je préfère l'Asie")
)
# L'agent a accès à tout l'historique via session.events

# 4. Plus tard, reprendre la conversation
session = await session_service.get_session(session.id)
# Tous les messages précédents sont accessibles
```

</div>

Notes:
C'est grâce à session.id qu'on reprend la conversation exacte
