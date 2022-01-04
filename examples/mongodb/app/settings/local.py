DEBUG = True
PLUGINS = [
    "fastack_mongoengine",
]
COMMANDS = []

MONGODB_NAME = "fastack_db"
MONGODB_USER = "fastack_user"
MONGODB_PASSWORD = "fastack_pass"
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
MONGODB_URI = (
    f"mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}/{MONGODB_NAME}"
)
