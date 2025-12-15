<!-- .slide: class="transition" -->

# Custom Agents

##==##

<!-- .slide -->

# Custom Agent : Concept

## Au-delà des workflows prédéfinis

Un **Custom Agent** hérite de `BaseAgent` et implémente sa propre logique d'orchestration via `_run_async_impl`.

### Caractéristiques :
- 🎨 **Contrôle total** sur la logique d'exécution
- 🔀 **Logique conditionnelle** personnalisée
- 🧩 **Patterns uniques** non couverts par Sequential/Parallel/Loop
- 🔧 **Intégrations externes** (APIs, DB, etc.)

Maîtrisez d'abord LLMAgent et WorkflowAgent
<!-- .element: class="admonition warning" -->

Utilisez Custom Agent quand Sequential, Parallel, Loop ne suffisent pas
<!-- .element: class="admonition note" -->

##==##

<!-- .slide -->

# Quand utiliser Custom Agent ?

## Situations nécessitant un contrôle personnalisé

<br>

### 🔀 **Logique conditionnelle**
Différents chemins selon les conditions runtime

### 📊 **Gestion d'état complexe**
Logique de state management sophistiquée

### 🎯 **Sélection dynamique d'agents**
Choisir les sous-agents à la volée

En bref : à utiliser lorsque les workflows prédéfinis ne suffisent pas
<!-- .element: class="admonition note" -->

##==##

<!-- .slide: class="with-code max-height" -->

# Structure d'un Custom Agent

## Héritage de BaseAgent

```python
from google.adk.agents import BaseAgent, LlmAgent
from google.adk.types import SessionContext

class StoryFlowAgent(BaseAgent):
    def __init__(self, name: str):
        # Initialisation de l'agent
        super().__init__(name=name)
        self.planner = LlmAgent(name="Planner", ...)
        self.writer = LlmAgent(name="Writer", ...)
        self.editor = LlmAgent(name="Editor", ...)
    
    async def _run_async_impl(self, ctx: SessionContext):
        plan = await self.planner.run_async(ctx) # 1. Planification
        # 2. Logique conditionnelle
        if ctx.session.state.get("complexity") > 5:
            # Logique multi-chapitres
            ...
        else:
            # Logique simple
            ...
        # 3. Édition finale
        return await self.editor.run_async(ctx)
```

_run_async_impl est la méthode où vous implémentez votre logique custom
<!-- .element: class="admonition note" -->

##==##

<!-- .slide: class="with-code" -->

# Implémentation de logique custom

## Opérations courantes

<br>

### Accéder au contexte et à l'état
```python
async def _run_async_impl(self, ctx: SessionContext):
    # Lire l'état
    user_level = ctx.session.state.get("user_level", "beginner")
    # Écrire dans l'état
    ctx.session.state["processed"] = True
```

### Appeler des sous-agents
```python
# Exécution d'un sous-agent
result = await self.sub_agent.run_async(ctx)
```

### Prendre des décisions
```python
# Logique conditionnelle
if condition:
    await self.agent_a.run_async(ctx)
else:
    await self.agent_b.run_async(ctx)
```

##==##

<!-- .slide -->

# Gestion de l'état

## State management dans Custom Agents

<br>

### Lecture de l'état
```python
value = ctx.session.state.get("key")
value_with_default = ctx.session.state.get("key", "default_value")
```

### Écriture dans l'état
```python
ctx.session.state["result"] = computed_value
ctx.session.state["step_completed"] = True
```

### Partage avec sous-agents
```python
# L'état est automatiquement partagé
ctx.session.state["shared_data"] = data
await self.sub_agent.run_async(ctx)  # Peut accéder à shared_data
```

<br>

L'état persiste pendant toute la durée de la session
<!-- .element: class="admonition note" -->


##==##

<!-- .slide: class="with-code max-height" -->

# Exemple pratique : Agent d'apprentissage adaptatif

## Adaptation dynamique au niveau de l'utilisateur

```python
class AdaptiveTutorAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.assessor = LlmAgent(name="LevelAssessor", ...)
        self.beginner_tutor = LlmAgent(name="BeginnerTutor", ...)
        self.intermediate_tutor = LlmAgent(name="IntermediateTutor", ...)
        self.advanced_tutor = LlmAgent(name="AdvancedTutor", ...)
    
    async def _run_async_impl(self, ctx: SessionContext):
        # 1. Évaluer le niveau
        await self.assessor.run_async(ctx)
        level = ctx.session.state.get("user_level")
        
        # 2. Router vers le tuteur approprié
        if level == "beginner":
            return await self.beginner_tutor.run_async(ctx)
        elif level == "intermediate":
            return await self.intermediate_tutor.run_async(ctx)
        else:
            return await self.advanced_tutor.run_async(ctx)
```

Notes:
Sélection dynamique du sous-agent basée sur l'évaluation
