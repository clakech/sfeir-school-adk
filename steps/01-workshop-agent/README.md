# 01-workshop-agent instructions

Pour ce premier lab vous allez créer votre premier agent qui devra appeler un tool pour vous répondre un message de bienvenue "Bonjour <votre_nom>".

## How to run?

```Bash
cd ./steps/01-workshop-agent
```
```Bash
pip install google-adk
```

# TP

## Création de l'agent

Dans ce TP nous allons créer notre premier agent, pour cela lancer la commande suivante:

```Bash
adk create hello_agent
```

La commande va vous demander de choisir un model et un backend, choisissez:
- `1. gemini-2.0-flash-001`
- `2. Google AI`

Ensuite générez une clef d'API depuis AI Studio (https://aistudio.google.com/apikey) ou demandez une clef d'api au formateur.

Votre premier agent est maintenant créé, vous pouvez jeter un oeil au fichier `__init__.py` pour constater l'export de votre agent.

Le fichier `.env` regroupe la configuration pour l'utilisation des modèles avec notamment la clef d'API utilisée par ADK.

Explorez le contenu du fichier `main.py`, qui contient la logique de votre agent, vous devriez avoir ce contenu:

```python
from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
```

Comme vous pouvez le constater pour l'instant notre agent se contente simplement de répondre aux questions de l'utilisateur

Testons ce premier agent en lancant la commande `adk web` qui permettra d'avoir une interface de chat avec votre agent. L'interface est accessible ici: https://127.0.0.1:8000

## Modification de l'agent

Maintenant que vous avez pu vérifier que votre agent fonctionne, vous allez pouvoir le modifier.

Mettez à jour les instructions pour que l'agent se contente uniquement de dire bonjour à l'utilisateur, eventuellement en donnant le nom de la personne.

Une fois les modifications faites vous pouvez retester votre agent en redémarrant la commande `adk web`.
