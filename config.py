import os

WEBHOOK_URL = os.getenv(
    "WEBHOOK_URL",
    "https://discord.com/api/webhooks/1529498055466942586/G5lM7uUKDOK25XpOAcA9CWNtJQEiMyGsmGDt2mf4Z-pz7Z_Bax28lxRpTC2VsgeW6jfs"
)

MESSAGE_ID_FILE = "status_message_id.txt"