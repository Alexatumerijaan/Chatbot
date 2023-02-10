# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/YukkiChatBot >.
#
# This file is part of < https://github.com/TeamYukki/YukkiChatBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiChatBot/blob/master/LICENSE >
#
# All rights reserved.
#

import asyncio
from sys import version as pyver

import pyrogram
from pyrogram import __version__ as pyrover
from pyrogram import filters, idle
from pyrogram.errors import FloodWait
from pyrogram.types import Message

import config
import mongo
from mongo import db

loop = asyncio.get_event_loop()
SUDO_USERS = config.SUDO_USER

app = pyrogram.Client(
    ":YukkiBot:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

save = {}
grouplist = 1

GREETINGS = ["hi", "hello", "hey", "greetings", "hola", "wassup", "what's good"]
GOODBYES = ["bye", "goodbye", "see you later", "adios", "later", "peace out"]
HINGLISH_FUNNY_MESSAGES = [
    "Bhagwan ke liye kuch bhi!",
    "Arre wah!",
    "Kya baat hai!",
    "Maza aa gaya!",
    "Haan ji!",
    "Sahi hai!",
]

def chatbot_response(message, sender_id):
    message = message.lower()

    for greeting in GREETINGS:
        if message.startswith(greeting):
            return random.choice(GREETINGS)
    
    for goodbye in GOODBYES:
        if message.startswith(goodbye):
            return random.choice(GOODBYES)

    # Check if the message contains any hinglish words and respond with a funny message
    if re.search("[A-Za-z]+", message):
        return random.choice(HINGLISH_FUNNY_MESSAGES)

    return "I'm sorry, I don't understand what you're trying to say."

def handle_message(message, sender_id):
    response = chatbot_response(message, sender_id)
    print(f"{sender_id}: {message}")
    print(f"Chatbot: {response}")
