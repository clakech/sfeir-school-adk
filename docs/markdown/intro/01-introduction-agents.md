<!-- .slide -->

# De ChatGPT aux Agents IA

<br>

## Vous avez déjà utilisé ChatGPT, Claude, Gemini...

<br>

### Mais qu'est-ce qu'un **Agent IA** exactement ?

Notes:
- Le public connaît déjà les interactions chat
- Transition naturelle vers les agents
- Poser la question fondamentale

##==##

<!-- .slide -->

# Rappel : Qu'est-ce qu'un LLM ?

<br>

**Large Language Model** = Modèle de langage de grande taille

<br>

```text
Entrée (Prompt)          LLM          Sortie (Completion)
     "Bonjour" ────────> [🤖] ────────> "Bonjour ! Comment..."
```

<br>

- Entraîné sur des milliards de textes
- Prédit le prochain token le plus probable
- Comprend le contexte et génère du texte cohérent

Notes:
- Rappel des bases pour bien partir
- Le LLM est stateless par défaut
- La génération est probabiliste

##==##

<!-- .slide -->

# Les limites du Chat simple

<br>

| ✅ Ce que ChatGPT fait bien | ❌ Ce qu'il ne fait pas |
|---------------------------|------------------------|
| Répondre à des questions | Exécuter des actions |
| Générer du texte | Accéder à vos données |
| Expliquer des concepts | Se souvenir entre sessions |
| Traduire, résumer | Utiliser des outils externes |

<br>

### 💡 Les agents comblent ces lacunes

Notes:
- Identifier les frustrations communes
- Poser les bases de la valeur des agents
- Préparer la définition d'un agent

##==##

<!-- .slide -->

# Qu'est-ce qu'un Agent IA ?

<br>

### Un agent = LLM + Capacités d'action

<br>

<div style="display: flex; justify-content: center; align-items: center; gap: 40px; font-size: 1.2em;">
  <div style="text-align: center;">
    <div style="border: 3px solid #00c7ff; border-radius: 10px; padding: 30px 40px; background: rgba(0, 199, 255, 0.1);">
      🧠<br><strong>LLM</strong><br>(Cerveau)
    </div>
  </div>
  <div style="font-size: 2em; color: #00c7ff;">↔</div>
  <div style="text-align: center;">
    <div style="border: 3px solid #00c7ff; border-radius: 10px; padding: 30px 40px; background: rgba(0, 199, 255, 0.1);">
      🔧<br><strong>Outils</strong><br>(Actions)
    </div>
  </div>
</div>

<div style="text-align: center; margin-top: 20px; font-size: 1.2em; color: #00c7ff;">
  ↕<br>
  💾 <strong>Mémoire</strong>
</div>

<br>

**Un agent peut raisonner, décider et agir de manière autonome**

Notes:
- Définition claire et visuelle
- Les 3 composants clés : LLM + Outils + Mémoire
- Autonomie = capacité à enchaîner plusieurs actions

##==##

<!-- .slide -->

# Anatomie d'un Agent

<br>

### Les 4 composants essentiels

<br>

1. **🧠 LLM** : Le cerveau qui raisonne
2. **🔧 Outils (Tools)** : Les capacités d'action
3. **💾 Mémoire** : Le contexte et l'historique
4. **📋 Instructions (System Prompt)** : La personnalité et les règles

Notes:
- Détailler chaque composant
- Chacun est indispensable
- On va les explorer un par un

##==##

<!-- .slide -->

# 🧠 Le LLM : Le cerveau

<br>

**Modèles populaires pour les agents (Nov 2025) :**

<br>

| Modèle | Éditeur | Points forts |
|--------|---------|--------------|
| GPT-5.1 | OpenAI | Raisonnement avancé, plus conversationnel |
| Claude Sonnet 4.5 | Anthropic | Excellence en code, agents autonomes |
| Gemini 2.5 Pro | Google | Coding et tâches complexes |
| Gemini 2.5 Flash | Google | Performance rapide, usage quotidien |

<br>

### 💡 Le choix du modèle impacte les capacités de l'agent

Notes:
- GPT-5.1 : nov 2025, pensée adaptative et personnalisation avancée
- Claude 4.5 : modèle optimisé pour agents et développeurs
- Gemini 2.5 : famille récente avec Pro (tâches complexes) et Flash (rapide)
- Gemini 2.5 Flash Image : génération et édition d'images natives
- Grok 4 : juillet 2025, par xAI (Elon Musk), intégré à Twitter/X
- Grok 4 Fast : sept 2025, version optimisée pour la vitesse

##==##

<!-- .slide -->

# 🔧 Les Outils (Tools/Functions)

<br>

**Les outils permettent aux agents d'agir dans le monde réel**

<br>

```python
tools = [
    {
        "name": "search_web",
        "description": "Recherche sur internet",
        "parameters": {"query": "string"}
    },
    {
        "name": "send_email",
        "description": "Envoie un email",
        "parameters": {"to": "string", "subject": "string", "body": "string"}
    }
]
```

<br>

### Le LLM décide quand et comment utiliser ces outils

Notes:
- Function calling = capacité native des LLMs modernes
- Le LLM choisit l'outil en fonction du contexte
- Format standard (OpenAI Functions, Anthropic Tools)

##==##

<!-- .slide -->

# 💾 La Mémoire

<br>

**Différents types de mémoire :**

<br>

| Type | Durée | Usage |
|------|-------|-------|
| **Court terme** | Une conversation | Context window du LLM |
| **Épisodique** | Session/Jour | Résumés, événements clés |
| **Long terme** | Permanent | Base de connaissances, RAG |

<br>

```text
Conversation → Résumé → Base vectorielle → Récupération
```

Notes:
- La mémoire permet la continuité
- Court terme = limité par le context window
- Long terme = nécessite des techniques comme RAG
- Les agents peuvent décider quoi retenir

##==##

<!-- .slide -->

# 📋 Le System Prompt

<br>

**Les instructions qui définissent votre agent :**

<br>

```text
Tu es un assistant développeur expert en Python.
Tu aides les développeurs à débugger leur code.

Règles :
- Toujours expliquer ton raisonnement
- Proposer du code testé et commenté
- Demander des clarifications si nécessaire
- Utilise l'outil "run_code" pour tester
- Ne jamais exécuter de code destructif (DROP, DELETE)
- Ne pas accéder aux fichiers système sensibles

Ton style : professionnel mais accessible
```

<br>

### 💡 Le prompt système est votre "contrat" avec l'agent

Notes:
- C'est l'identité et les règles de l'agent
- Bien définir le comportement attendu
- Inclure des exemples si besoin
- Peut contenir des contraintes de sécurité

##==##

<!-- .slide -->

# Pattern fondamental : ReAct

<br>

**Re**asoning + **Act**ing = Cycle pensée/action

<br>

<div style="font-size: 0.95em;">

**1. 💭 Pensée (Reasoning)** → L'agent analyse et planifie

**2. 🎬 Action** → Appel d'un outil (API, recherche, calcul...)

**3. 👀 Observation** → Réception et analyse du résultat

**4. 💭 Nouvelle pensée** → Continuer ou répondre ?

</div>

<br>

### ↻ Boucle jusqu'à résolution complète

Notes:
- ReAct = Papier de recherche Google/Princeton 2022
- Pattern le plus utilisé dans les agents modernes
- Chaque étape est explicite et traçable
- L'agent peut faire plusieurs cycles avant de répondre
- Évite les hallucinations en vérifiant via des actions

##==##

<!-- .slide -->

# ReAct : Exemple détaillé

<br>

**❓ Question : "Quel temps fait-il à Paris et dois-je prendre un parapluie ?"**

<br>

```text
💭 Pensée 1: "Je dois chercher la météo actuelle à Paris"
🎬 Action 1: search_web("météo Paris temps réel")
👀 Observation 1: "18°C, ciel dégagé, vent 10 km/h"

💭 Pensée 2: "Je dois vérifier les prévisions de pluie"
🎬 Action 2: get_weather_forecast("Paris", hours=6)
👀 Observation 2: "0% de précipitations prévues dans les 6h"

💭 Pensée 3: "J'ai toutes les infos, je peux répondre"
✅ Réponse: "Il fait 18°C à Paris avec un ciel dégagé. 
   Pas de pluie prévue, vous n'avez pas besoin de parapluie !"
```

Notes:
- L'agent fait 2 cycles avant de répondre
- Chaque action apporte une information complémentaire
- Le raisonnement est transparent et vérifiable
- Réponse factuelle basée sur des données réelles

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

### 💡 On commence simple : agent conversationnel avec quelques outils

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

### 💡 Un agent ajoute de la complexité - l'utiliser quand ça apporte de la valeur

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

<br>

| Framework | Étoiles GitHub | Forces principales |
|-----------|----------------|-------------------|
| **LangChain** | 120k+ ⭐ | Plateforme complète (LangGraph + LangSmith) |
| **CrewAI** | 40k+ ⭐ | Multi-agents, déploiement production |
| **Google ADK** | 15k+ ⭐ | Toolkit Python code-first, intégration simplifiée à GCP |

<br>

### 💡 Cette formation : concepts applicables à tous les frameworks

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
