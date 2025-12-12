<!-- .slide: class="transition"-->

# Agents IA

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

1. **🧠 LLM** : Le "cerveau" qui raisonne
2. **🔧 Outils (Tools)** : Les capacités d'action
3. **💾 Mémoire** : Le contexte et l'historique
4. **📋 Instructions (System Prompt)** : La personnalité et les règles

Notes:
- Détailler chaque composant
- Chacun est indispensable
- On va les explorer un par un

##==##

<!-- .slide -->

# 🧠 Le LLM : Le "cerveau"

**Modèles populaires pour les agents (Déc 2025) :**

<br>

| Modèle | Éditeur | Points forts |
|--------|---------|--------------|
| GPT-5.2 | OpenAI | Raisonnement avancé, plus conversationnel |
| Claude Opus 4.5 | Anthropic | Excellence en code, agents autonomes |
| Gemini 3 Pro | Google | Coding et tâches complexes, multi-modal |
| Gemini 2.5 Flash | Google | Performance rapide, usage quotidien |

<br>

Le choix du modèle impacte les capacités de l'agent
<!-- .element: class="admonition note"--> 

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

Le LLM décide quand et comment utiliser ces outils

Notes:
- Function calling = capacité native des LLMs modernes
- Le LLM choisit l'outil en fonction du contexte
- Format standard (OpenAI Functions, Anthropic Tools)

##==##

<!-- .slide -->

# 💾 La Mémoire

**Différents types de mémoire :**

<br>

| Type | Durée | Usage |
|------|-------|-------|
| **Court terme** | Une conversation | Context window du LLM |
| **Épisodique** | Session/Jour | Résumés, événements clés |
| **Long terme** | Permanent | Base de connaissances, RAG |

<br>

Notes:
- La mémoire permet la continuité
- Court terme = limité par le context window
- Long terme = nécessite des techniques comme RAG
- Les agents peuvent décider quoi retenir
