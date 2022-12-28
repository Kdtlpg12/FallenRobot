class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "20400887"
    API_HASH = "
535abea1d0cc67a4be1f57de026a846f"
    CASH_API_KEY = "AJPUOQOL5KLJ9IUZ"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://qhfqcweh:c8Ew52O5IoJH64tRYg0GADXxnMnU7
GfQ@mouse.db.elephantsql.com/qhfqcweh"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://VegetaMusic:Vegeta@cluster0.dohyl.m
ongodb.net/myFirstDatabase?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "DevilsHeavenMF"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5854090671:AAGPB9j8HrvKGZciigaBzj56KA7kLkNRa_M"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "WJLELU3365VQ"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "5897158959"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
