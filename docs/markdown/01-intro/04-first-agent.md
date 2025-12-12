<!-- .slide: class="transition" -->

# Mon premier agent

##==##

<!-- .slide -->

# Du Chat à l'Agent : Exemple

<br>

**❓ Question : "Quel temps fait-il à Paris et dois-je prendre un parapluie ?"**

<br>

| 💬 Chat simple | 🤖 Agent |
|---------------|---------|
| "Je ne peux pas accéder aux données météo en temps réel..." | 1. 🔍 Cherche la météo actuelle |
| (Hallucine potentiellement) | 2. 📊 Analyse les données (pluie ?) |
| | 3. ✅ Répond avec certitude : "18°C, pas de pluie prévue, pas besoin de parapluie" |

<br>

### L'agent peut **vérifier** et **agir** sur des données réelles

Notes:
- Différence fondamentale : connexion au monde réel
- L'agent ne devine pas, il vérifie
- Réduit les hallucinations sur les faits
- Augmente la fiabilité

##==##

<!-- .slide -->

# Types d'agents courants

<br>

| Type | Description | Use Case |
|------|-------------|----------|
| **Conversationnel** | Dialogue naturel + actions | Assistant personnel, support client |
| **Task-based** | Exécute une tâche spécifique | Automation, workflows |
| **Multi-agent** | Plusieurs agents collaborent | Systèmes complexes, simulation |
| **Autonome** | Fonctionne sans supervision | Monitoring, alertes |

<br>

On commence simple : agent conversationnel avec quelques outils

<!-- .element class="admonition note"-->

Notes:
- Différents types pour différents besoins
- On va commencer par le plus simple
- La complexité vient progressivement
- Multi-agent = niveau avancé (plus tard dans la formation)

##==##

<!-- .slide -->

# Quand NE PAS utiliser un agent ?

<br>

| ❌ Éviter les agents | ✅ Préférer |
|---------------------|-------------|
| Tâches simples et déterministes | Script classique, règles métier |
| Besoin de résultats 100% prévisibles | Algorithmes traditionnels |
| Latence critique (< 100ms) | API directe, cache |
| Budget tokens très limité | Modèle plus petit, fine-tuning |
| Données hautement sensibles | Traitement local, règles fixes |

<br>

Un agent ajoute de la complexité - l'utiliser quand ça apporte de la valeur

<!-- .element class="admonition note"-->

Notes:
- Les agents ne sont pas toujours la solution
- Coût en latence : chaque appel LLM prend du temps
- Coût en tokens : raisonnement = tokens supplémentaires
- Imprévisibilité : le LLM peut varier ses réponses
- Sécurité : plus de surface d'attaque avec les outils
- Règle : si un if/else suffit, pas besoin d'agent

##==##

<!-- .slide -->

# Les frameworks d'agents

<br>

**Les plus populaires en 2025 :**

| Framework | Étoiles GitHub | Forces principales |
|-----------|----------------|-------------------|
| **LangChain** | 120k+ ⭐ | Plateforme complète (LangGraph + LangSmith) |
| **CrewAI** | 40k+ ⭐ | Multi-agents, déploiement production |
| **Google ADK** | 15k+ ⭐ | Toolkit Python code-first, intégration simplifiée à GCP |

<br>

Cette formation : concepts applicables à tous les frameworks

<!-- .element class="admonition note"-->

Notes:
- LangChain : écosystème le plus complet (120k+ stars, plateforme + observabilité)
- CrewAI : spécialisé orchestration multi-agents avec UI de déploiement
- Google ADK : nouveau toolkit officiel Google, code-first
- On enseigne les concepts fondamentaux, pas un framework spécifique

##==##

<!-- .slide -->

# Cas d'usage réels

<br>

**Où les agents excellent :**

<br>

- 🔍 **Recherche augmentée** : Agents qui cherchent et synthétisent
- 📊 **Analyse de données** : Query databases, génère des rapports
- 🤖 **Automatisation** : Workflows intelligents avec décisions
- 💬 **Support client** : Résolution autonome de tickets
- 👨‍💻 **Dev assistants** : Review code, génère tests, debug
- 📝 **Content creation** : Recherche + rédaction + fact-checking

Notes:
- Applications concrètes dès aujourd'hui
- ROI mesurable dans ces domaines
- On va en construire plusieurs pendant la formation
- Penser à vos propres cas d'usage
- Exemple ROI concret : Klarna (2024) - leur agent IA gère 2/3 des conversations support client, équivalent à 700 agents temps plein, résolution en 2min vs 11min avant (source: Klarna press release, Feb 2024)
- Autre exemple : GitHub Copilot - développeurs 55% plus rapides sur les tâches de coding (étude GitHub 2022)

##==##

<!-- .slide -->

# Prêts à construire votre premier agent ?

<br>

### 🎯 Ce que vous allez apprendre :

<br>

1. ✅ Configurer et utiliser les bons outils
2. ✅ Créer des agents avec mémoire et outils
3. ✅ Orchestrer plusieurs agents ensemble
4. ✅ Gérer les fonctionnalités avancées (streaming, erreurs, sécurité)

<br>

### 🚀 Let's build!

Notes:
- Roadmap de la formation
- Approche progressive et pratique
- Beaucoup de labs pour pratiquer
- À la fin, vous saurez construire des agents production-ready
