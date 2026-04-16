import os

from tg_bot.sample_config import Config as SampleConfig


class Config(SampleConfig):
    LOGGER = True

    # REQUIRED — read from environment variables
    API_KEY = os.environ.get('TOKEN', SampleConfig.API_KEY)
    OWNER_ID = os.environ.get('OWNER_ID', SampleConfig.OWNER_ID)
    OWNER_USERNAME = os.environ.get('OWNER_USERNAME', SampleConfig.OWNER_USERNAME)

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', SampleConfig.SQLALCHEMY_DATABASE_URI)
    MESSAGE_DUMP = os.environ.get('MESSAGE_DUMP', SampleConfig.MESSAGE_DUMP)
    LOAD = os.environ.get('LOAD', '').split() or SampleConfig.LOAD
    NO_LOAD = os.environ.get('NO_LOAD', 'translation rss').split()
    WEBHOOK = bool(os.environ.get('WEBHOOK', SampleConfig.WEBHOOK))
    URL = os.environ.get('URL', SampleConfig.URL)

    # OPTIONAL
    SUDO_USERS = [int(x) for x in os.environ.get('SUDO_USERS', '').split() if x]
    SUPPORT_USERS = [int(x) for x in os.environ.get('SUPPORT_USERS', '').split() if x]
    WHITELIST_USERS = [int(x) for x in os.environ.get('WHITELIST_USERS', '').split() if x]
    DONATION_LINK = os.environ.get('DONATION_LINK', SampleConfig.DONATION_LINK)
    CERT_PATH = os.environ.get('CERT_PATH', SampleConfig.CERT_PATH)
    PORT = int(os.environ.get('PORT', SampleConfig.PORT))
    DEL_CMDS = bool(os.environ.get('DEL_CMDS', SampleConfig.DEL_CMDS))
    STRICT_GBAN = bool(os.environ.get('STRICT_GBAN', SampleConfig.STRICT_GBAN))
    WORKERS = int(os.environ.get('WORKERS', SampleConfig.WORKERS))
    BAN_STICKER = os.environ.get('BAN_STICKER', SampleConfig.BAN_STICKER)
    ALLOW_EXCL = bool(os.environ.get('ALLOW_EXCL', SampleConfig.ALLOW_EXCL))
    BMERNU_SCUT_SRELFTI = int(os.environ.get('BMERNU_SCUT_SRELFTI', SampleConfig.BMERNU_SCUT_SRELFTI))


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
