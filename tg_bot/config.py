import os
import sys

from tg_bot.sample_config import Config as SampleConfig

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _require_env(name: str) -> str:
    """Return the value of a required environment variable.

    Raises a clear RuntimeError (instead of a cryptic ValueError later) when
    the variable is missing or still holds a placeholder value.
    """
    value = os.environ.get(name, "").strip()
    if not value:
        print(
            f"[config] ERROR: Required environment variable '{name}' is not set. "
            "Please set it in your Railway service variables.",
            file=sys.stderr,
        )
        sys.exit(1)
    return value


def _int_env(name: str, default: int) -> int:
    """Read an integer from an environment variable, falling back to *default*."""
    raw = os.environ.get(name, "").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        print(
            f"[config] ERROR: Environment variable '{name}' must be an integer, "
            f"got: {raw!r}",
            file=sys.stderr,
        )
        sys.exit(1)


# ---------------------------------------------------------------------------
# Config classes
# ---------------------------------------------------------------------------

class Config(SampleConfig):
    LOGGER = True

    # REQUIRED — must be provided via environment variables.
    # TOKEN: Telegram bot token from @BotFather.
    API_KEY = os.environ.get("TOKEN", "").strip() or None

    # OWNER_ID: stored as int so __init__.py never has to convert a placeholder
    # string.  Falls back to the owner's known Telegram user ID.
    OWNER_ID = _int_env("OWNER_ID", default=8206476526)

    # OWNER_USERNAME: plain username without the leading '@'.
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "").strip() or "owner"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", SampleConfig.SQLALCHEMY_DATABASE_URI)
    MESSAGE_DUMP = os.environ.get("MESSAGE_DUMP", SampleConfig.MESSAGE_DUMP) or None
    LOAD = os.environ.get("LOAD", "").split() or SampleConfig.LOAD
    NO_LOAD = os.environ.get("NO_LOAD", "translation rss").split()
    WEBHOOK = bool(os.environ.get("WEBHOOK", SampleConfig.WEBHOOK))
    URL = os.environ.get("URL", SampleConfig.URL) or None

    # OPTIONAL
    SUDO_USERS = [int(x) for x in os.environ.get("SUDO_USERS", "").split() if x]
    SUPPORT_USERS = [int(x) for x in os.environ.get("SUPPORT_USERS", "").split() if x]
    WHITELIST_USERS = [int(x) for x in os.environ.get("WHITELIST_USERS", "").split() if x]
    DONATION_LINK = os.environ.get("DONATION_LINK", SampleConfig.DONATION_LINK) or None
    CERT_PATH = os.environ.get("CERT_PATH", SampleConfig.CERT_PATH) or None
    PORT = _int_env("PORT", default=SampleConfig.PORT)
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", SampleConfig.DEL_CMDS))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", SampleConfig.STRICT_GBAN))
    WORKERS = _int_env("WORKERS", default=SampleConfig.WORKERS)
    BAN_STICKER = os.environ.get("BAN_STICKER", SampleConfig.BAN_STICKER)
    ALLOW_EXCL = bool(os.environ.get("ALLOW_EXCL", SampleConfig.ALLOW_EXCL))
    BMERNU_SCUT_SRELFTI = _int_env("BMERNU_SCUT_SRELFTI", default=SampleConfig.BMERNU_SCUT_SRELFTI)

    # Validate TOKEN at class-definition time so the error is obvious.
    if not API_KEY:
        print(
            "[config] ERROR: Required environment variable 'TOKEN' is not set. "
            "Please set it in your Railway service variables.",
            file=sys.stderr,
        )
        sys.exit(1)


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
