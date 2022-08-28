from discord_webhook import DiscordWebhook, DiscordEmbed

from config import getConfig

config = getConfig().get('notification')


def discord():
    global config
    try:
        discordConfig = config.get('discord')
        webHookUrl = discordConfig.get('web_hook')
    except:
        raise Exception('Discord config not valid')
    else:
        webhook = DiscordWebhook(url=webHookUrl)
        embed = DiscordEmbed(title='A Shiny has been detected', color='03b2f8')
        embed.set_timestamp()
        webhook.add_embed(embed)

        webhook.execute()