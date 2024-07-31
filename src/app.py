import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

# xoxb-hoge
app = App(token=os.environ.get("SLACK_BOT_USER_OAUTH_TOKEN"))

@app.event("app_mention")
def response(event, say):
    input_text = event["text"]
    channel = event["channel"]
    if "スーパーカップ" in input_text:
        say(text = "バニラ味がおすすめです。", channel = channel)
    else:
        say(text = "次は `スーパーカップ` を含んだコメントをしてください。", channel = channel)


if __name__ == "__main__":
    # xapp-hoge
    SocketModeHandler(app, os.environ.get("SLACK_APP_LEVEL_TOKEN")).start()
