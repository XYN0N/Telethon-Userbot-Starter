import telethon

# replace with your own API ID and HASH
api_id = Your API ID
api_hash = 'Your API HASH'

# replace with the owner's user ID
OWNER_ID = #Your ADMIN ID

client = telethon.TelegramClient('session_name', api_id, api_hash)

@client.on(telethon.events.NewMessage)
async def handler(event):
    print("Received message:", event.message.text)
    if event.message.from_id.user_id != OWNER_ID:
        return

    if not event.message.text or not event.message.text.startswith("#ping"):
        return

    print("Sending response...")
    await event.respond("pong!")
    print("Response sent.")

client.start()
print("Client started :D")
client.run_until_disconnected()
