from app import line_bot_api, handler
from linebot.models import MessageEvent, TextMessage, TextSendMessage


from app.picSearch import google

# 查詢 google
@handler.add(MessageEvent, message=TextMessage)
def replyText(event):
    if event.source.user_id == "您的 line User Id": #您的 line User Id

        replay = False

        if not replay:
            replay = google.googlesearch(event)

        if not replay:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="無法找到您的照片,情再打其他關鍵字")
            )
