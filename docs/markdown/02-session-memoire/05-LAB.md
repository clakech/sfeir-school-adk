<!-- .slide: class="exercice" -->

# Lab : Session & Memory

## Mise en pratique

##==##

<!-- .slide -->

# Objectifs du Lab

## Créer un agent avec mémoire persistante

<br>

Nous allons construire un agent capable de se souvenir du nom de l'utilisateur d'une session à l'autre.

### Étapes :

1. **Initialisation** : Configurer `InMemorySessionService` et `InMemoryMemoryService`.
2. **Chat 1** : L'utilisateur donne son nom ("Je m'appelle Bob"). L'agent le stocke dans le `State` (utilisez le préfixe `user:` !).
3. **Persistance** : À la fin du chat, sauvegarder la session en mémoire.
4. **Chat 2** : Nouvelle session. L'utilisateur demande "Quel est mon nom ?".
5. **Retrieval** : L'agent utilise la mémoire pour retrouver l'info.

<br>

### 📂 Workspace
Allez dans le dossier### Go to `02-session-lab`

##==##

<!-- .slide: class="with-code" -->

# Aide-mémoire

### Sauvegarder en mémoire (Callback)
```python
async def auto_save_callback(ctx):
    await ctx.memory_service.add_session_to_memory(ctx.session)

agent = Agent(..., after_agent_callback=auto_save_callback)
```

### Configurer l'outil de mémoire
```python
tools = [
    PreloadMemoryTool(memory_service=memory_service)
]
```

### State avec Scope
```python
# Dans un outil ou callback
ctx.session.state["user:name"] = "Bob"
```

<!-- .element: class="admonition tip" -->
N'oubliez pas que `InMemory` perd tout si vous relancez le script Python. Le test doit se faire dans la même exécution du script (2 boucles de chat successives).

Notes:
- Le piège classique est de relancer le script pour tester la "mémoire". Avec InMemory, ça ne marche pas.
