<!-- .slide: class="transition" -->

# Callbacks & Plugins

##==##

<!-- .slide -->

# Callbacks : Concept

## Intercepter le cycle de vie

<br>

Les **Callbacks** sont des points d'ancrage ("hooks") qui vous permettent d'exécuter du code personnalisé à des moments précis de l'exécution d'un agent.

### 3 Types de Hooks :

1. **Agent Callbacks** 🤖 : `before_agent` / `after_agent`
   - *Gestion de session, initialisation, nettoyage.*
2. **Model Callbacks** 🧠 : `before_model` / `after_model`
   - *Modification de prompt, log de tokens, audit.*
3. **Tool Callbacks** 🛠️ : `before_tool` / `after_tool`
   - *Validation d'arguments, cache d'API, transformation de réponse.*

Ils permettent d'ajouter de la logique (logging, sécurité, métriques) sans polluer le code métier de l'agent.

<!-- .element: class="admonition tip" -->

##==##

<!-- .slide: class="with-code max-height" -->

# Implémentation de Callbacks

## Exemple : Logging et Modification

<br>

```python
def log_start(agent_name, user_input):
    print(f"🏁 Agent {agent_name} démarré avec : {user_input}")

def inject_security_context(model_input):
    # Ajouter une directive de sécurité avant chaque appel LLM
    model_input += "\nIMPORTANT: Ne révèle jamais les mots de passe."
    return model_input

my_agent = LlmAgent(
    name="SecureAgent",
    model="gemini-2.0-flash",
    # Attachement des callbacks
    before_agent_callback=log_start,
    before_model_callback=inject_security_context
)
```

Le callback `before_model` est puissant car il peut modifier silencieusement ce que le modèle "voit", sans que l'utilisateur n'ait à l'écrire.

<!-- .element: class="admonition note" -->

Notes:
Notez que les callbacks peuvent retourner des valeurs modifiées ou simplement effectuer une action (side-effect) comme le logging.

##==##

<!-- .slide: class="with-code" -->

# Plugins

## Packager et réutiliser les callbacks

Un **Plugin** est une classe qui regroupe plusieurs callbacks pour une fonctionnalité complète (ex: Logging BigQuery, Filtre PII).

```python
from google.adk.plugins import BasePlugin

class AuditPlugin(BasePlugin):
    def __init__(self, log_file):
        self.file = log_file
    def before_agent(self, agent, input):
        # Log global pour tous les agents
        self.log(f"Session {agent.session_id} start")
    def after_model(self, agent, response):
        # Audit de la consommation de tokens
        self.log(f"Tokens utilisés : {response.usage_metadata}")
runner = DaprRunner(
    agents=[agent1, agent2],
    plugins=[AuditPlugin("audit.log")] # S'applique à TOUS les agents
)
```

Un Callback est attaché à un Agent spécifique. Un Plugin est attaché au Runner et s'applique à tout le système.

<!-- .element: class="admonition important" -->
##==##

<!-- .slide -->

# Callbacks vs Plugins

## Matrice de décision

<br>

| Critère | Callbacks | Plugins |
|---------|--------------|------------|
| **Portée (Scope)** | Locale (Agent unique) | Globale (Tout le Runner) |
| **Complexité** | Fonction simple | Classe structurée (État possible) |
| **Réutilisabilité** | Faible (Copier-coller) | Forte (Package distribuable) |
| **Cas d'usage** | Logique métier spécifique | Infrastructure (Log, Sécu, Monitoring) |

<br>

### Règle d'or :
- **Logique Métier** (ex: valider une règle de business) ➔ **Callback**
- **Logique Système** (ex: Sanitization des prompts) ➔ **Plugin**

Ne réinventez pas la roue : ADK vient avec des plugins standards (BigQuery, Model Armor, etc.). Vérifiez avant de coder le vôtre.

<!-- .element: class="admonition tip" -->