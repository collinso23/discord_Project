import discord
import logging
async def logger():
	logger = logging.getLogger('discord')
	logger.setLevel(logging.INFO)
	handler = logging.FileHandler(filename='discord.log', encoding='utf-8',mode='w')
	hanlder.setFormatter(logging.Formater('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
	logger.addHandler(handler)

