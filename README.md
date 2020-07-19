# Commands

**All commands start with the prefix `/`**

- `eightball` : Une boule magique répond à toutes vos questions
- `pileface` : Lance une pièce
- `mdp` : Génére un mot de passe aléatoire
- `note` : Commande qui note l'input de l'user
- `bg` : Calcule la beauté d'un utilisateur

and a simple help command : `help` or `aide` or `list`

# Run

### Python

```
# Start the bot
python index.py
```

### PM2

```
# Start the bot
pm2 start pm2.json

# Tips on common commands
pm2 <command> [name]
  start em2500-M253X.py    Run the bot again if it's offline
  list                    Get a full list of all available services
  stop em2500-M253X.py     Stop the bot
  reboot em2500-M253X.py   Reboot the bot
```

### Docker

```
# Build and run the Dockerfile
docker-compose up -d --build

# Tips on common commands
docker-compose <command>
  ps      Check if bot is online or not (list)
  down    Shut down the bot
  reboot  Reboot the bot without shutting it down or rebuilding
  logs    Check the logs made by the bot.
```
