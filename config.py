from dotenv import load_dotenv
from os import getenv
load_dotenv('creds/.env')
TOKEN = getenv('TOKEN')
FOLDER_ID = getenv("FOLDER_ID")
IAM_TOKEN = getenv('IAM_TOKEN')
ADMINS_IDS = getenv('ADMINS_IDS')  # list

MAX_USERS = 3
MAX_GPT_TOKENS = 120
COUNT_LAST_MSG = 4
TOKENIZE_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/tokenizeCompletion"
GPT_MODEL = 'yandexgpt-lite'
GPT_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
MAX_USER_STT_BLOCKS = 10
MAX_USER_TTS_SYMBOLS = 5_000
MAX_USER_GPT_TOKENS = 2_000

LOGS = 'creds/logs.log' 
DB_FILE = 'messages.db'
SYSTEM_PROMPT = [{'role': 'system', 'text': 'Ты - популярный блогер в интернете, который ведёт блог о разных вещах.'
                                            'Ты должен будешь написать пост на тему, которую скажет тебе пользователь. '
                                            'Ты не должен давать пользователю подсказки. Текст должен быть только '
                                            'по теме. Пиши текст в .md разметке.'}]
