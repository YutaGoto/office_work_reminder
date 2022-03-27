import os
from slack_bolt import App


app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

result = app.client.reminders_add(
    user=os.environ.get("USER_ID"),
    text="月初の事務作業する。",
    time="today 10:30am"
)


print(result)
