<!-- .slide: class="transition" -->

# Parallel Agent

##==##

<!-- .slide: class="with-code" -->

# Parallel Agent : Vue d'ensemble

## Exécution simultanée de tâches

<br>

Un **Parallel Agent** exécute **tous ses sous-agents en même temps** (concurrence).

<br>

```
       ┌─ Agent 1 ─┐
Start ─┼─ Agent 2 ─┼─ Agrégation ─ Résultat
       └─ Agent 3 ─┘
```

### Caractéristiques :
- ⚡ Exécution concurrente
- 📦 Agrégation des résultats
- 🎯 Idéal pour tâches indépendantes

Notes:
Comme un manager qui assigne des tâches à plusieurs employés simultanément

##==##

<!-- .slide -->

# Quand utiliser Parallel Agent ?

## Cas d'usage typiques

<br>

### 🌐 Appels API multiples
```
API Météo + API Actualités + API Bourse (simultanément)
```

### 🔍 Collecte de données multi-sources
```
Web Scraping + Base de données + API externe (en parallèle)
```

### 🏢 Analyse concurrentielle
```
Analyse Concurrent A + Concurrent B + Concurrent C
```

<br>

Utilisez Parallel Agent quand les tâches sont **indépendantes** et n'ont pas besoin des résultats des autres
<!-- .element: class="admonition important" -->

Notes:
Optimisation de performance : réduit le temps total d'exécution

##==##

<!-- .slide: class="with-code max-height" -->

# Parallel Agent : Implémentation

## Code Python

```python
from google.adk.agents import ParallelAgent, LlmAgent

# Définir des sous-agents indépendants
weather_agent = LlmAgent(
    name="WeatherAPI",
    system_instruction="Récupère les données météo"
)

news_agent = LlmAgent(
    name="NewsAPI",
    system_instruction="Récupère les actualités"
)

stock_agent = LlmAgent(
    name="StockAPI",
    system_instruction="Récupère les données boursières"
)

# Créer le workflow parallèle
parallel_fetcher = ParallelAgent(
    name="MultiSourceFetcher",
    sub_agents=[weather_agent, news_agent, stock_agent]
)
```

Notes:
Les trois agents s'exécutent simultanément, pas d'ordre garanti

##==##

<!-- .slide: class="with-code" -->

# Agrégation des résultats

## Gestion des résultats parallèles

<br>

### Points clés :

- ⏱️ **Timing** : Les agents peuvent terminer à des moments différents
- 🔄 **Collecte** : Les résultats sont collectés après que tous les agents ont terminé
- ❌ **Gestion d'erreurs** : Si un agent échoue, les autres continuent
- 📊 **Combinaison** : Les résultats sont disponibles dans `ctx.session.state`

<br>

```python
# Tous les résultats sont disponibles après l'exécution
all_data = {
    "weather": ctx.session.state.get("weather_data"),
    "news": ctx.session.state.get("news_data"),
    "stocks": ctx.session.state.get("stock_data")
}
```

Notes:
Le ParallelAgent attend que tous les sous-agents se terminent avant de continuer

##==##

<!-- .slide: class="with-code max-height" -->

# Exemple pratique : Analyse concurrentielle

## Recherche sur plusieurs concurrents simultanément

```python
competitor1_agent = LlmAgent(
    name="Competitor1Analyzer",
    system_instruction="Analyse le concurrent 1 : stratégie, prix, produits"
)

competitor2_agent = LlmAgent(
    name="Competitor2Analyzer",
    system_instruction="Analyse le concurrent 2 : stratégie, prix, produits"
)

competitor3_agent = LlmAgent(
    name="Competitor3Analyzer",
    system_instruction="Analyse le concurrent 3 : stratégie, prix, produits"
)

competitive_analysis = ParallelAgent(
    name="CompetitiveAnalysis",
    sub_agents=[competitor1_agent, competitor2_agent, competitor3_agent]
)

# Résultat : rapport complet sur tous les concurrents
```

Notes:
Gain de temps : 3x plus rapide que l'approche séquentielle
