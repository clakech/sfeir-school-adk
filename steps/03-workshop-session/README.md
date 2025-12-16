# 03-workshop-session instructions

## How to run?

```Bash
cd ./steps/03-workshop-session
```

## TP

### Création de l'agent

Dans ce TP nous allons créer un agent capable de se souvenir du nom de l'utilisateur d'une session à l'autre (persistance).

Commencez par créer l'agent avec la commande suivante :

```Bash
adk create memory_agent
```

Choisissez le modèle et le backend habituels (gemini-2.5-flash / Google AI).

### Modification de l'agent

Commencez par structurer votre agent dans un package `memory_agent` avec un fichier `agent.py` et `__init__.py`.

#### Objectif

Votre but est de configurer l'agent pour qu'il utilise le service de mémoire et de session.

Vous devez :
1.  **Configurer les outils** : L'agent doit avoir le tool `load_memory` pour récupérer les informations passées.
2.  **Sauvegarder** : Mettre en place un callback qui sera appelé après chaque interaction pour sauvegarder la session dans la mémoire (indice : `after_agent_callback` et `callback_context.add_session_to_memory()`).
3.  **Tester** : Vérifiez que l'agent se souvient de votre nom même si vous créez une nouvelle session (bouton "New Chat" dans l'interface).

> **Note**: Avec `adk web`, les services `InMemoryMemoryService` et `InMemorySessionService` sont créés automatiquement par le framework. Vous n'avez pas besoin de les instancier vous-même.

> **Astuce**: Pour vérifier que le mécanisme fonctionne, regardez les logs dans le terminal. Vous devriez voir l'agent appeler le tool `load_memory` lors de la deuxième session.


### Test

Lancez votre agent :

```Bash
adk run
```

Dans le chat :
1.  Dites "Je m'appelle Bob".
2.  Ouvrez une nouvelle conversation.
3.  Demandez "Quel est mon nom ?".
