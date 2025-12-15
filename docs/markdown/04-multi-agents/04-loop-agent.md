<!-- .slide: class="transition" -->

# Loop Agent

##==##

<!-- .slide -->

# Loop Agent : Vue d'ensemble

## Exécution itérative avec condition

Un **Loop Agent** exécute **répétitivement** ses sous-agents jusqu'à ce qu'une condition soit remplie.

<br>

```
┌──────────────────┐
│  Exécute agents  │
└────────┬─────────┘
         │
    Condition ? ────── Non ──┐
         │                   │
        Oui                  │
         │                   │
     Termine  ←──────────────┘
```

<br>

### Caractéristiques :
- 🔄 Comme une boucle `while` en programmation
- ⏹️ Conditions d'arrêt configurables
- 🛡️ Limite maximale d'itérations

Notes:
Utile pour le raffinement itératif et les tentatives avec retry

##==##

<!-- .slide -->

# Quand utiliser Loop Agent ?

## Cas d'usage typiques

<br>

### 🔄 Mécanismes de retry
```
Tenter API call → Si échec, réessayer avec backoff
```

### 📈 Raffinement itératif
```
Générer → Évaluer → Si qualité insuffisante, améliorer
```

### 🎯 Amélioration progressive
```
Code → Tests → Si tests échouent, corriger le code
```

<br>

Utilisez Loop Agent pour les tâches qui nécessitent **plusieurs tentatives** ou **amélioration progressive**

<!-- .element: class="admonition important" -->

Notes:
Toujours définir une condition d'arrêt pour éviter les boucles infinies

##==##

<!-- .slide: class="with-code max-height" -->

# Loop Agent : Implémentation

## Code Python

```python
from google.adk.agents import LoopAgent, LlmAgent

# Définir les agents pour la boucle
generator = LlmAgent(
    name="CodeGenerator",
    system_instruction="Génère du code Python"
)

validator = LlmAgent(
    name="CodeValidator",
    system_instruction="Valide la qualité du code et suggère améliorations"
)

# Créer la boucle avec condition d'arrêt
refinement_loop = LoopAgent(
    name="CodeRefinementLoop",
    sub_agents=[generator, validator],
    max_iterations=5,
    stop_condition=lambda ctx: ctx.session.state.get("validation_passed")
)
```

Notes:
La boucle s'arrête quand validation_passed est True OU après 5 itérations max

##==##

<!-- .slide -->

# Conditions d'arrêt

## Stratégies de terminaison de boucle

<br>

### 1. **Nombre maximum d'itérations**
```python
max_iterations=10  # Arrêt après 10 tours max
```

### 2. **Condition basée sur l'état**
```python
stop_condition=lambda ctx: ctx.session.state.get("quality_score") > 8
```

### 3. **Condition de succès/échec**
```python
stop_condition=lambda ctx: ctx.session.state.get("task_completed") == True
```

<br>

Toujours définir `max_iterations` pour éviter les boucles infinies
<!-- .element: class="admonition warning" -->

Notes:
Combinez plusieurs conditions pour plus de contrôle

##==##

<!-- .slide: class="with-code max-height" -->

# Exemple pratique : Raffinement de contenu

## Amélioration itérative jusqu'à qualité acceptable

<br>

```python
content_generator = LlmAgent(
    name="ContentGenerator",
    system_instruction="Génère du contenu marketing"
)

quality_checker = LlmAgent(
    name="QualityChecker",
    system_instruction="""Évalue la qualité (1-10) sur:
    - Clarté, Engagement, SEO
    - Passe 'quality_passed' à True si score >= 8"""
)

content_refinement = LoopAgent(
    name="ContentRefinement",
    sub_agents=[content_generator, quality_checker],
    max_iterations=5,
    stop_condition=lambda ctx: ctx.session.state.get("quality_passed")
)

# Résultat : Contenu de haute qualité ou 5 tentatives
```

Notes:
La boucle continue jusqu'à obtenir un contenu de qualité >= 8 ou 5 essais max
