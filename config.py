import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22238059"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1a1f1cb9ba85a88dc7cc5fcb473ff79a")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://rameshkumarjaat010:qt5IrVrAN7HCwHtZ@cluster0.by1gf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
