#!/usr/bin/python3.9

from dotenv import load_dotenv
from src.myClient import MyClient
import os
import discord


intents = discord.Intents.default()
intents.members = True
client = MyClient(intents)
load_dotenv()
client.run(os.getenv("TOKEN"))
