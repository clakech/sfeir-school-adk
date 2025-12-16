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

Votre but est de configurer l'agent pour qu'il utilise le service de mémoire et de session en mémoire (`InMemory`).

Vous devez :
1.  **Configurer les services** : Instancier `InMemoryMemoryService` et `InMemorySessionService`.
2.  **Sauvegarder** : Mettre en place un mécanisme pour sauvegarder la session dans la mémoire à la fin de chaque interaction (indice : regardez du côté des callbacks de l'agent).
3.  **Retrouver** : Assurez-vous que l'agent a les moyens de retrouver l'information (indice : il existe un tool fait pour ça).
4.  **Tester** : Vérifiez que l'agent se souvient de votre nom même si vous simulez une nouvelle session.


> **Note**: Avec `InMemory`, la mémoire est conservée tant que le processus Python tourne.

### Test

Lancez votre agent :

```Bash
adk run
```

Dans le chat :
1.  Dites "Je m'appelle Bob".
2.  Ouvrez une nouvelle conversation.
3.  Demandez "Quel est mon nom ?".
