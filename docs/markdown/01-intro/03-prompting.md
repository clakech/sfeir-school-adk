<!-- .slide: class="transition" -->

# Prompting

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

Le prompt système est votre "contrat" avec l'agent

<!-- .element: class="admonition note"-->

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
