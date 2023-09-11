import requests
import discode
import os

channel_access_token = "bUZFu/tDYvZ14XTW3+BrGxzue4LuTNxxOs57HkeeB95gXhEFOwqgP7Nb4VgFb2/dF+chm+EC2GxVTFuEJKnBpHc44O72r99IvKaX1+68mRKUCdoEtesAFBckmSvD+w+hQGnscjJNH7qxZl6HPq0FlwdB04t89/1O/w1cDnyilFU="
group_id = "YOUR_GROUP_ID"

# ボットの設定
bot = discode.Bot(command_prefix='!', token=os.environ['MTE1MDc5ODE4NTk2MzQ1ODYxMQ.GTODdV.WplMXxuIeWh5__ppwK77cR8CWlo0Eqf1W0PpVQ'])

# LINEグループにメッセージを送信する関数
async def send_to_line_group(message_content):
    # ここにLINEグループへのメッセージ送信のコードを書く

# メンションされたメッセージを処理するイベントハンドラ
@bot.event
async def on_message(message):
    if bot.user_mentioned(message):
        # メンションされたらLINEグループにメッセージを送信
        await send_to_line_group(message.content)

# ボットを起動
bot.run()

