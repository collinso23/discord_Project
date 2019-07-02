# discord_Project
Just a home for a wee" python bot

The goal for this bot is to utilze discord.py, requests, lxml, and BeautifulSoup to create a functional discord bot that is able to receive commands via the bot-commands discord channel.


Some commands to be implemented:
  search: -s | --search; Will scrape various webpages for dnd content (ie: Spells, Classes, Races, ect.)
  help: -h | --help

Some tasks to be implemented:
  server count
  player count
  join channel message --> all channels
  Message of the Day --> announcements

Big changes

Gonna overhaul the bot adding features to allow for the creation of monsters and player characters via commands to the discord bot.
Just about to finish defining playerclass so that the bot may later call information scraped of the database to populate fields in character creation menu.
The bot will save and create pdfs for the users characters which can be called and embeded into the discord server so they players may track the progress of their character

#TODO:
Implement character generation locally,the implement dynamic character creation with DnD_DB_Scrapper, finally create cog to manage and control inqGen
