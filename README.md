# telegram_utilities

## Goals

Some scripts for telegram.

- <b>bouriket.py</b> : simply scan all the public users of the conversations present in the Telegram account and place them in a single CSV ready to be analyzed for cross-checking. Watch out, you're in the dataset! Could be improved by scrapping all conversations looking for users directly in messages.

## Instructions

- Get the at api_id and hash_id at https://core.telegram.org/api/obtaining_api_id
- Put them in the script
- Install the library Telethon (pip install telethon)
- Launch the script and connect to your account (will not work if MFA is activated)

## Recommandations

- Make sure what you're doing is legal. 
- Make sure what you're doing is secure.
