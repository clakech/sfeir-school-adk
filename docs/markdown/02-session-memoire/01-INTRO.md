<!-- .slide: class="transition" -->

# Contexte Conversationnel

## Session, État et Mémoire

##==##

<!-- .slide -->

# Pourquoi le contexte est-il crucial ?

## Transformer des interactions uniques en conversation

<br>

Les LLMs sont par nature **stateless** (sans état). Chaque appel est indépendant.
Pour créer une expérience conversationnelle, il est nécessaire de gérer le contexte.

<br>
<br>
<br>

### Les 3 niveaux de persistance ADK :

1. **Session** 🧵 : Le fil de discussion immédiat (Court terme)
2. **State** 📝 : Les données structurées de la session (Court terme)
3. **Memory** 🧠 : La base de connaissance vectorielle (Long terme)

Notes:
- Analogie :
  - Session = La mémoire de travail (RAM)
  - State = Le bloc-notes sur le bureau
  - Memory = La bibliothèque d'archives

##==##

<!-- .slide -->

# Architecture du Contexte

## Vue d'ensemble des services

<div class="col">

### Composants Clés

- **SessionService** : Gère le cycle de vie des conversations.
- **MemoryService** : Gère l'indexation et la recherche sémantique.
- **Agent** : Orchestre les appels aux services via des Tools ou le Runtime.

<br>
<br>

![full-center](./assets/images/LongTermShortTerm.svg)

</div>


Notes:
- Distinction claire entre le stockage "Session" (souvent SQL/NoSQL rapide) et "Memory" (Vector DB pour la recherche sémantique).

##==##

<!-- .slide -->

# Du Prototype à la Production

## Choisir la bonne implémentation

ADK offre des implémentations interchangeables pour chaque service.

<br>

| Environnement | SessionService | MemoryService | Caractéristiques |
|---------------|----------------|---------------|------------------|
| **Dev / Test** | `InMemorySession` | `InMemoryMemory` | Rapide, **non persistant** |
| **Production** | `Firestore` | `VertexAI MemoryBank` | Scalable, **persistant** |

<br>
<br>

Ne jamais utiliser les services `InMemory` en production, car toutes les données sont perdues au redémarrage de l'application.
<!-- .element: class="admonition important" -->

Notes:
- Cette flexibilité permet de coder l'agent une fois et de changer l'infra par simple configuration.
