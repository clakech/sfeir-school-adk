# 02-workshop-tools instructions


## How to run?

```Bash
cd ./steps/02-workshop-tools
```

# TP

## Création de l'agent

Dans ce TP nous allons créer un agent qui utilisera le tool `google_search`, pour cela créer l'agent avec la commande suivante:

```Bash
adk create news_agent
```

La commande va vous demander de choisir un model et un backend, choisissez:
- `1. gemini-2.0-flash-001`
- `2. Google AI`

Ensuite générez une clef d'API depuis AI Studio (https://aistudio.google.com/apikey) ou demandez une clef d'api au formateur.

## Modification de l'agent

Comme pour le premier TP, nous allons maintenant mettre jour les instructions de notre agent qui utilisera le tool pour aller chercher sur internet.

Pour cela, ajoutez à l'agent la configuration du tool, en utilisant le paramètre `tools=[google_search]` à la création de l'agent.

Ensuite vous pouvez modifier la description et les instructions pour que l'agent sache quand ce servir de l'outil. Par exemple vous pouvez demander à votre agent d'aider l'utilisateur a trouver des articles pertninent poufaire de la veille sur l'actualité d'OpenAI.

Une fois les modification effectuée, lancer l'agent via la commande `adk web` et vérifiez la bonne utilisation du tool par votre agent.

Si l'appel au tool ne se fait pas essayer de modifier vos instructions et de relancer votre agent jusqu'a ce que cela fonctionne.