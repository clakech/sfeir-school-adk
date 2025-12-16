<!-- .slide: class="transition" -->

# State

## Contextualisation dynamique

##==##

<!-- .slide -->

# State : Vue d'ensemble

## Le bloc-notes de la session

<br>

Le **State** est un dictionnaire clé-valeur attaché à chaque session.
Il stocke des **métadonnées** qui ne sont pas des messages.

<br>

```python
session.state = {
    "user_name": "Alice",
    "current_step": "payment",
    "cart_total": 125.50
}
```

<br>

### Caractéristiques :
- 📝 Données structurées (pas du texte libre)
- 🔄 Accessible et modifiable par l'agent et le code
- 💉 Injecté automatiquement dans les prompts

Notes:
Pensez au State comme aux variables d'une application

##==##

<!-- .slide -->

# Quand utiliser le State ?

## Cas d'usage typiques

<br>

### 🎯 Workflows multi-étapes
```
Tracking : étape_courante = "paiement"
```

### 👤 Préférences utilisateur
```
Langue, thème, niveau d'expertise
```

### 🛒 Données transactionnelles
```
Panier d'achat, filtres actifs
```

<br>

Utilisez State pour toute donnée **structurée** qui influence le comportement de l'agent

<!-- .element: class="admonition important" -->

Notes:
Si c'est un booléen, un nombre ou un objet structuré → State
Si c'est du texte libre de conversation → Event/Message

##==##

<!-- .slide: class="with-code" -->

# Scopes : Les préfixes

## Contrôler la portée des données

<br>

ADK utilise des **préfixes** pour définir la portée et la persistance.

| Préfixe | Scope | Persistance | Exemple |
|---------|-------|-------------|---------|
| `Aucun` | Session | Oui (si DB) | `current_step` |
| `user:` | User (Cross-session) | Oui | `user:theme` |
| `app:` | App (Global) | Oui | `app:api_key` |
| `temp:` | Invocation | Non | `temp:debug` |

<br>

```python
# Préférence utilisateur (persistante entre sessions)
session.state["user:preferred_language"] = "fr"

# Donnée temporaire (perdue après l'invocation)
session.state["temp:raw_api_response"] = {...}
```

Notes:
user: est très puissant : même si l'utilisateur commence une nouvelle conversation, ses préférences sont conservées

##==##

<!-- .slide: class="with-code max-height" -->

# Injection dans les prompts

## Templating dynamique avec {key}

```python
from google.adk.agents import LlmAgent

# Définir l'agent avec des placeholders
agent = LlmAgent(
    name="PersonalAssistant",
    model="gemini-2.0-flash",
    instruction="""
Tu es un assistant personnel.
Le nom de l'utilisateur est : {user:name}.
Son niveau d'expertise est : {user:expertise}.
La langue préférée est : {user:language}.
"""
)

# Au runtime, ces valeurs sont injectées automatiquement
session.state["user:name"] = "Alice"
session.state["user:expertise"] = "Débutant"
session.state["user:language"] = "Français"

# L'agent reçoit l'instruction complète avec les valeurs
```

<div style="font-size: 0.8em;">
C'est la méthode recommandée pour personnaliser l'agent sans réécrire son prompt.
<!-- .element: class="admonition tip" -->
</div>

Notes:
ADK remplace automatiquement {user:name} par "Alice" avant d'appeler le LLM

##==##

<!-- .slide: class="with-code" -->

# Modification du State : Les pièges

## ❌ À éviter absolument


<div style="font-size: 1.3em;">

```python
# MAUVAISE PRATIQUE
session = await service.get_session("abc")
session.state["key"] = "value"  # ❌ Pas d'événement, pas de sauvegarde
```

</div>

<br>

### Pourquoi c'est dangereux :
- Aucun `Event` créé → Pas de traçabilité
- Pas de sauvegarde automatique → Données perdues
- `last_update_time` non mis à jour

##==##

<!-- .slide: class="with-code" -->

# Modification du State : Best Practice

## ✅ La bonne méthode


<div style="font-size: 1.2em;">

```python
from google.adk.tools import Tool

# Dans un Tool
class UpdatePreferenceTool(Tool):
    def run(self, ctx: ToolContext, language: str):
        # ✅ Modification via le contexte
        ctx.session.state["user:language"] = language
        return f"Langue mise à jour : {language}"

# Dans un Callback
async def my_callback(ctx: CallbackContext):
    # ✅ Modification via le contexte
    ctx.session.state["processed"] = True
```

</div>

<br>

<div style="font-size: 0.8em;">

Le contexte (`ToolContext`, `CallbackContext`) gère automatiquement la création d'événements et la persistance

</div>

<!-- .element: class="admonition tip" -->

Notes:
Toujours passer par un contexte pour modifier le State

##==##

<!-- .slide: class="with-code max-height" -->

# Exemple pratique : Wizard multi-étapes

## Gestion d'un processus séquentiel

<div style="font-size: 1.2em;">

```python
# Initialiser le wizard
session.state["wizard_step"] = 1
session.state["user_data"] = {}

# Étape 1 : Nom
if session.state["wizard_step"] == 1:
    session.state["user_data"]["name"] = user_input
    session.state["wizard_step"] = 2

# Étape 2 : Email
elif session.state["wizard_step"] == 2:
    session.state["user_data"]["email"] = user_input
    session.state["wizard_step"] = 3

# Étape 3 : Finalisation
elif session.state["wizard_step"] == 3:
    # Toutes les données collectées
    complete_data = session.state["user_data"]
    # Traitement final...
```

</div>

Notes:
Le State permet de tracker la progression sans polluer l'historique des messages
