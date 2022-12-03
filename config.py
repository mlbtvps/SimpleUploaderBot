import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5456141576:AAFnxg_mMT1DcNTHVKcmXjRWFbFvZShxN8Q")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", 17894641))
    API_HASH = os.environ.get("API_HASH", "4e5b39e5c7c6066e5144dfc50cf466cf")
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    VIDEO_FORMATS = ["mp4", "mkv", "mov", "m4v", "avi", "unknown_video"]
    AUDIO_FORMATS = ["mp3", "flac", "m4a", "wav"]
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "5468192421"))
    SESSION_NAME = "SIMPLEUPLOADERBOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://anasty:anasty@anasty.diboh0t.mongodb.net/?retryWrites=true&w=majority")
    MAX_RESULTS = "50"
