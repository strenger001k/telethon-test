from telethon import TelegramClient
from message import *
from work_txt import get_list_id
import schedule
import time

api_id = '<api_id>'
api_hash = '<api_hash>'
client = TelegramClient('test_app', api_id, api_hash)


async def sender():
    id_list = get_list_id()

    for chat_id in id_list:
        await client.send_message(chat_id, TEXT)


def job():
    with client:
        client.loop.run_until_complete(sender())


schedule.every(1).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
