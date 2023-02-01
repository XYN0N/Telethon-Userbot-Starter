import asyncio
import telethon
async def main():
    api_id =  # API ID
    api_hash = 'API HASH'
    phone_number = 'Your Telephone number'

    client = telethon.TelegramClient('session_name', api_id, api_hash)
    await client.start(phone=phone_number)

    me = await client.get_me()
    print('Sessione avviata come utente', me.first_name)

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print('Sessione terminata.')

asyncio.run(main())
