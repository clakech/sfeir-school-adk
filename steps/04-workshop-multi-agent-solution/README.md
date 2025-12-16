# 04-workshop-multi-agent instructions

Objectif : construire un workflow multi-agents qui génère un post LinkedIn à partir d'un sujet.

Le workflow attendu est le suivant :

1. Recherche web d'actualités sur le sujet (tool `google_search`) → stocké dans `state['news']`
2. Résumé des résultats → stocké dans `state['summary']`
3. Rédaction du post LinkedIn → stocké dans `state['linkedin_post']`

Le résultat final doit être fonctionnel et correspondre à l'architecture présente dans `steps/04-workshop-multi-agent-solution`.

## Prérequis

- Avoir `adk` installé et fonctionnel
- Avoir une clé API Google AI Studio : [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)

## How to run?

```bash
cd ./steps/04-workshop-multi-agent
```

## TP

### 1) Création de l'agent racine

Créez un agent nommé `linkedin_writer_agent` :

```bash
adk create linkedin_writer_agent
```

Lors du prompt, choisissez :

- `1. gemini-2.0-flash-001`
- `2. Google AI`

Ensuite générez une clef d'API depuis AI Studio (https://aistudio.google.com/apikey) ou demandez une clef d'api au formateur.


### 2) Implémenter le root agent (orchestrateur)

Dans `linkedin_writer_agent/agent.py`, créez un `LlmAgent` qui orchestre le workflow via un sous-agent.

Contraintes :

- Le root agent s'appelle `root_agent`
- Il a un `sub_agents=[post_generator_agent]`
- Son `instruction` indique qu'il doit déléguer aux sous-agents pour : rechercher, résumer, écrire le post.

Indice : vous importerez `post_generator_agent` depuis `linkedin_writer_agent/post_generator_agent/agent.py`.

### 3) Créer un agent séquentiel `post_generator_agent`

Créez le dossier `linkedin_writer_agent/post_generator_agent/` et un fichier `agent.py`.

Cet agent doit être un `SequentialAgent` qui enchaîne 3 sous-agents dans cet ordre :

1. `news_search_agent`
2. `news_summarizer`
3. `linkedin_ghost_writer`

Contraintes :

- Nom : `post_generator_agent`
- `description` : explique qu'il recherche, résume, puis rédige le post LinkedIn.

### 4) Sous-agent 1 : `news_search_agent` (web search)

Créez :

- `linkedin_writer_agent/post_generator_agent/news_search_agent/agent.py`
- `linkedin_writer_agent/post_generator_agent/news_search_agent/prompt.py`

Contraintes :

- C'est un `LlmAgent`
- Il utilise le tool `google_search` (`tools=[google_search]`)
- Il a un `output_key="news"` (le résultat doit se retrouver dans `state['news']`)
- Son prompt (dans `prompt.py`) doit forcer l'utilisation de `google_search` avant de répondre

### 5) Sous-agent 2 : `news_summarizer` (résumé)

Créez :

- `linkedin_writer_agent/post_generator_agent/news_summarizer/agent.py`

Contraintes :

- C'est un `LlmAgent`
- Il lit `state['news']`
- Il écrit un résumé dans `state['summary']`
- Il utilise `output_key="summary"`

### 6) Sous-agent 3 : `linkedin_ghost_writer` (rédaction)

Créez :

- `linkedin_writer_agent/post_generator_agent/linkedin_ghost_writer/agent.py`
- `linkedin_writer_agent/post_generator_agent/linkedin_ghost_writer/prompt.py`

Contraintes :

- C'est un `LlmAgent`
- Il lit `state['summary']`
- Il produit le post LinkedIn dans `state['linkedin_post']` via `output_key="linkedin_post"`
- Le prompt doit demander un ton positif et (optionnellement) des emojis, comme un ghost writer LinkedIn

### 7) Arborescence attendue

À la fin, vous devez obtenir une arborescence proche de :

```text
steps/04-workshop-multi-agent/
	linkedin_writer_agent/
		__init__.py
		agent.py
		.env
		post_generator_agent/
			agent.py
			news_search_agent/
				agent.py
				prompt.py
			news_summarizer/
				agent.py
			linkedin_ghost_writer/
				agent.py
				prompt.py
```

### 8) Lancer et valider

Lancez l'UI de chat ADK :

```bash
cd linkedin_writer_agent
adk web
```

Dans l'interface, testez avec une demande du type :
- "Fais-moi un post LinkedIn sur les chats"

Validation attendue :
- Vous devez voir un appel au tool `google_search`
- Le post final doit être cohérent avec des infos récentes (issues de la recherche)

Si l'agent ne déclenche pas `google_search`, renforcez le prompt de `news_search_agent` (mots-clés : "ALWAYS", "MUST", "DO NOT answer without searching").

