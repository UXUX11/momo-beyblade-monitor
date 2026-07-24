import os

try:
    from local_config import WEBHOOK_URL, LINE_CHANNEL_ACCESS_TOKEN
except ImportError:
    WEBHOOK_URL = os.environ["WEBHOOK_URL"]
    LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]

MESSAGE_ID_FILE = "status_message_id.txt"