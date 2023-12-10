from telethon import TelegramClient, types # pip install telethon
from telethon.tl import types, functions
import pandas as pd

# Will not work if MFA is activated (password cloud)

# Use your own values from my.telegram.org

api_id =                               # number
api_hash =                             # string
client = TelegramClient('anon', api_id, api_hash)

async def main():

    data = pd.DataFrame(columns=['chat_id', 'chat_name', 'user_id', 'first_name', 'last_name'])

    async for dialog in client.iter_dialogs():

        # if str(dialog.id).startswith("-100"):        # only channels

        print(dialog.name, ";", dialog.id)

        try:
            chat = await client.get_entity(types.PeerChannel(dialog.id))

            participants = await client.get_participants(chat)

            for participant in participants:
                new_row = {
                    'chat_id': dialog.id,
                    'chat_name': dialog.name,
                    'user_id': participant.id,
                    'first_name': participant.first_name,
                    'last_name': participant.last_name
                }

                new_row_df = pd.DataFrame([new_row])

                data = pd.concat([data, new_row_df], ignore_index=True)

        except Exception as e:
            print(e)
            pass

    data.to_csv("final.csv")

with client:
    client.loop.run_until_complete(main())

