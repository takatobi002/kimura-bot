import requests
import discode
import os

channel_access_token = "直接書かない"
group_id = "直接書かない"

# ボットの設定
bot = discode.Bot(command_prefix='!', token=os.environ['直接書かない'])

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

