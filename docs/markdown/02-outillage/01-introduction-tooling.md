<!-- .slide -->

# Pourquoi les outils sont essentiels ?

### Un agent sans outil = Un cerveau sans mains

| ❌ **LLM seul**           | ✅ **Agent avec outils**        |
|---------------------------|---------------------------------|
| Génère du texte           | Cherche sur le web              |
| Raisonne                  | Accède aux données              |
| Répond                    | Exécute du code                 |
|                           | Appelle des APIs                |
|                           | Agit dans le monde réel         |


Les outils transforment les mots en actions

<!-- .element: class="admonition note" -->

Notes:
- Sans outils, l'agent ne peut que parler
- Les outils sont l'interface entre l'IA et le monde réel
- C'est la différence fondamentale entre un chatbot et un agent
- Les outils permettent la vérification factuelle

##==##

<!-- .slide: class="with-code" -->

# Qu'est-ce qu'un Tool ?

Un outil (tool) => du code que l'agent va pouvoir appeler

```python
def get_weather(city: str, unit: str):
    """
    Retrieves the weather for a city in the specified unit.

    Args:
        city (str): The city name.
        unit (str): The temperature unit, either 'Celsius' or 'Fahrenheit'.
    """
    # ... function logic ...
    return {"status": "success", "report": f"Weather for {city} is sunny."}
```

Le LLM n'appelle pas les outils directement, il demande à l'agent de le faire

<!-- .element: class="admonition warning" -->

Notes:
- Un tool a un nom, une description et des paramètres
- La description est cruciale : elle guide le LLM
- Le LLM utilise le tool calling natif pour appeler la fonction
- L'agent reçoit le résultat et peut l'utiliser dans sa réponse

##==##

<!-- .slide -->

# Comment l'agent exécute les outils ?

Pattern ReAct

- Reasoning -> Le LLM analyse la demande de l'utilisateur, et détecte le besoin d'un outil
- Action -> L'agent appelle l'outil et refait un appel au LLM avec le résultat dans le contexte
- Observation -> Le LLM analyse le besoin de l'utilisation + le résultat du tool pour générer la réponse

Example:

```text
1. 👤 User: "Quel temps fait-il à Paris ?"
         ↓
2. 🧠 LLM: Analyse → Besoin d'appeler get_weather("Paris")
         ↓
3. 🤖 Agent: Exécute l'appel API → Retourne {"temp": 18, "sky": "clear"}
         ↓
4. 🧠 LLM: Reçoit le résultat + demande initiale → Formule la réponse
         ↓
5. 💬 Response: "Il fait 18°C à Paris avec un ciel dégagé"
```

Notes:
- Le cycle peut se répéter plusieurs fois
- L'agent peut appeler plusieurs outils avant de répondre
- Chaque appel enrichit le contexte
- L'orchestration est gérée automatiquement par le framework

##==##

<!-- .slide -->

# Comment l'agent choisit ?

Le LLM analyse 3 éléments pour choisir le bon outil :
<br>

1. **La requête utilisateur** : Intention et contexte
2. **Description de l'outil** : Nom + description + paramètres
3. **Historique de conversation** : Résultats précédents

<br>

```python
# ❌ Mauvaise description
name="tool1"
description="Fait des choses"

# ✅ Bonne description
name="search_company_database"
description="Recherche des employés dans la base de données de l'entreprise par nom, département ou email"
```

La qualité des descriptions impacte directement la qualité de la sélection

<!-- .element: class="admonition note" -->

Notes:
- Le LLM n'a pas accès au code, seulement aux métadonnées
- Une bonne description = meilleure sélection
- Être spécifique et clair sur le but de l'outil
- Inclure des exemples dans la description si nécessaire
- Éviter l'ambiguïté entre plusieurs outils similaires

##==##

<!-- .slide -->

# Best Practices : Nommage des outils

| ✅ **BON : Verbe + Objet + Contexte** | ❌ **MAUVAIS : Trop vague ou générique** |
|--------------------------------------|-----------------------------------------|
| get_weather_forecast                 | weather                                 |
| search_customer_orders               | search                                  |
| create_support_ticket                | data                                    |
| update_user_profile                  | function1                               |

<br>

**Règles d'or :**
- Commencer par un verbe d'action (`get`, `search`, `create`, `update`, `delete`)
- Être explicite sur l'objet manipulé
- Utiliser le snake_case
- Éviter les abréviations obscures

Notes:
- Le nom est le premier indicateur pour le LLM
- Un bon nom = moins d'ambiguïté
- Suivre une convention cohérente dans votre codebase
- Le nom doit être auto-explicatif

##==##

<!-- .slide -->

# Tools vs Prompting : Quand utiliser quoi ?

| Situation | Solution | Pourquoi |
|-----------|----------|----------|
| Génération de texte | **Prompting** | Le LLM excelle naturellement |
| Raisonnement logique | **Prompting** | Capacité native du LLM |
| Récupération de données | **Tool** | Données factuelles, à jour |
| Calculs complexes | **Tool** | Précision garantie |
| Appels d'APIs externes | **Tool** | Interaction système |
| Modification d'état | **Tool** | Action sécurisée et traçable |


Notes:
- Ne pas sur-utiliser les tools
- Le LLM peut déjà faire beaucoup nativement
- Tools = pour l'interaction avec le monde réel
- Overhead de tool calling vs génération directe
- Trouver le bon équilibre

##==##

<!-- .slide -->

# Les 3 catégories d'outils ADK

<br>

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 20px 0;">
  <div style="border: 3px solid #4285f4; border-radius: 10px; padding: 20px; background: rgba(66, 133, 244, 0.1);">
    <div style="font-size: 2em; margin-bottom: 10px;">🔷</div>
    <strong>Outils Gemini/Google</strong>
    <div style="font-size: 0.9em; margin-top: 10px;">
      Natifs au modèle
      <br>• Google Search
      <br>• Code Execution
      <br>• Bigquery
      <br>• ...
    </div>
  </div>
  <div style="border: 3px solid #fbbc04; border-radius: 10px; padding: 20px; background: rgba(251, 188, 4, 0.1);">
    <div style="font-size: 2em; margin-bottom: 10px;">🔌</div>
    <strong>Third-party</strong>
    <div style="font-size: 0.9em; margin-top: 10px;">
      Intégrations externes
      <br>• GitHub
      <br>• Notion
      <br>• Gitlab
      <br>• ...
    </div>
  </div>
  <div style="border: 3px solid #34a853; border-radius: 10px; padding: 20px; background: rgba(52, 168, 83, 0.1);">
    <div style="font-size: 2em; margin-bottom: 10px;">☁️</div>
    <strong>Custom</strong>
    <div style="font-size: 0.9em; margin-top: 10px;">
      Fonctions de code
      <br>• Librairie externes
      <br>• Code custom
    </div>
  </div>
</div>

Notes:
- 3 grandes familles d'outils dans ADK
- Gemini tools = natifs, pas de config externe
- Google Cloud = nécessite des crédentials GCP
- Third-party = souvent nécessite des API keys
- Custom tools = pour vos besoins spécifiques
