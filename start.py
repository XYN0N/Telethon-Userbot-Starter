import telethon

# replace with your own API ID and HASH
api_id = apid  # from https://my.telegram.org/
api_hash =  'apihash'  #from https://my.telegram.org/

client = telethon.TelegramClient('session_name', api_id, api_hash)

@client.on(telethon.events.NewMessage)
async def handler(event):
    if event.message.text and event.message.text.startswith("#ping"):
        await event.respond("Pong!")

client.start()
client.run_until_disconnected()
