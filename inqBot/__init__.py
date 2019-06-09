from utils import default

config = defaults.get("config.json")

def main():
    bot.run(config.token)
