from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
import configparser

app = Flask(__name__)

# 導入 config.ini 檔案
config = configparser.ConfigParser()
config.read('config.ini')

# Line 聊天機器人的基本資料
line_bot_api = LineBotApi(config.get('LineBot','channel_access_token'))
handler = WebhookHandler(config.get('LineBot','channel_secret'))

# 導入其他的程式模組
from app import router, linebotmodules