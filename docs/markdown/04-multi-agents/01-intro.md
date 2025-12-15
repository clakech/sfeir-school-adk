<!-- .slide: class="transition" -->

# Qu'est-ce qu'un système multi-agents ?

##==##

<!-- .slide -->

# Systèmes Multi-Agents : Définition

## Un système de collaboration autonome

<br>

Un **système multi-agents** est une collection d'agents individuels et autonomes qui collaborent pour atteindre un objectif commun.

<br>

### Trois principes fondamentaux :

- **Contrôle décentralisé** : Aucun agent "chef" ne contrôle tout
- **Vues locales** : Chaque agent n'a qu'une vue partielle du système
- **Comportement émergent** : Des comportements complexes émergent de simples interactions

Notes:
Analogie : Une volée d'oiseaux - pas de leader, mais des motifs coordonnés

##==##

<!-- .slide -->

# Pourquoi les systèmes multi-agents ?

## Avantages de l'approche collaborative

<br>

- 🎯 **Robustesse** : Si un agent échoue, les autres continuent
- 📈 **Scalabilité** : Ajoutez des agents spécialisés selon les besoins
- 🔄 **Flexibilité** : Adaptez l'architecture aux problèmes complexes
- 🧩 **Spécialisation** : Chaque agent excelle dans son domaine

<br>

Les agents travaillant ensemble peuvent résoudre des tâches qu'aucun agent seul ne pourrait accomplir facilement.

<!-- .element: class="admonition note" -->

Notes:
Exemple : Système de support client avec agents spécialisés (facturation, technique, retours)

##==##

<!-- .slide -->

# Les types d'agents ADK

## ADK fournit trois types d'agents principaux

<br>

| Type | Rôle | Utilisation |
|------|------|-------------|
| **LLM Agents** | Le "cerveau" 🧠 | Raisonnement avec LLM |
| **Workflow Agents** | Le "manager" 📋 | Orchestration du flux d'exécution |
| **Custom Agents** | Le "spécialiste" 🔧 | Logique personnalisée complexe |

<br>

Notes:
- LLM Agents : Utilisent des modèles de langage pour comprendre et raisonner
- Workflow Agents : Sequential, Parallel, Loop - ne font pas le travail mais dirigent
- Custom Agents : Quand vous avez besoin de contrôle total sur la logique

##==##

<!-- .slide -->

# Hiérarchie des agents

## Organisation structurée des agents

<br>

### Deux règles simples :

1. **Parent & Sous-agents** : Un agent parent peut gérer un ou plusieurs sous-agents
2. **Règle du parent unique** : Chaque agent ne peut avoir qu'un seul parent

<br>

```
    RootAgent (CEO)
    ├── Agent A (VP)
    │   ├── Agent A1 (Director)
    │   └── Agent A2 (Director)
    └── Agent B (VP)
        └── Agent B1 (Manager)
```

Notes:
Analogie : Organigramme d'entreprise - ligne de commande et flux de données clairs

##==##

<!-- .slide -->

# Communication entre agents

## Trois mécanismes principaux

<br>

### 1. **État de session partagé** 📝
État commun accessible par tous les agents de la hiérarchie

### 2. **Délégation pilotée par LLM** 🤖
L'agent parent décide intelligemment quel sous-agent appeler

### 3. **Invocation explicite (AgentTool)** 🔧
Un agent appelle un autre agent comme un outil/fonction

<br>

Notes:
- État partagé : Comme un tableau blanc commun
- Délégation LLM : Routage intelligent basé sur le contexte
- AgentTool : Consultation d'experts à la demande
