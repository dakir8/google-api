# separator used by search.py, categories.py, ...
SEPARATOR = ";"

LANG            = "en_US" # can be en_US, fr_FR, ...
ANDROID_ID      = "3f0c2b01b168eb16" # "xxxxxxxxxxxxxxxx"
GOOGLE_LOGIN    = "testerprice@gmail.com" # "username@gmail.com"
GOOGLE_PASSWORD = "nwDaniel86!"
AUTH_TOKEN      = None # "yyyyyyyyy"

# force the user to edit this file
if any([each == None for each in [ANDROID_ID, GOOGLE_LOGIN, GOOGLE_PASSWORD]]):
    raise Exception("config.py not updated")

