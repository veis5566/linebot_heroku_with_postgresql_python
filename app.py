from flask import Flask, request, abort
from dbModel import *
from datetime import datetime
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,LineBotApiError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage,BubbleContainer, BoxComponent, TextComponent
)
from reply_format import generate_reply_format_display,generate_name_link_reply_format,help_reply_message
from sqlalchemy import and_,or_
from fnmatch import fnmatch
import pytz
import json
app = Flask(__name__)


# Channel Access Token
line_bot_api = LineBotApi('LINE_ACCESS_TOKEN')
# Channel Secret
handler = WebhookHandler('LINE_CHANNEL_SECRET')
# Target strings
stage_string = ["【ゴールドラッシュ】","【EXバトル】"]
sns_string = "https://cdn-resources.monst-dreamcompany.com/matching.html?user_code="
execute_string = ["display@","clean_all@","clean_month@"]


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    bodyjson=json.loads(body)
    app.logger.error("Request body: " + body)
    user_id = bodyjson['events'][0]['source']['userId']
    if ('text' in bodyjson['events'][0]['message']):
        user_text = bodyjson['events'][0]['message']['text']
    else:
        user_text = "No text"

    user_timestamp = int(bodyjson['events'][0]['timestamp'])/1000
    user_month = datetime.fromtimestamp(user_timestamp).strftime('%b')

    if bodyjson['events'][0]['source']['type'] == "group":
        group_id = bodyjson['events'][0]['source']['groupId']
    else:
        group_id = ""

    
    try:
        if group_id == "":
            profile = line_bot_api.get_profile(user_id)
        else:
            profile = line_bot_api.get_group_member_profile(group_id,user_id)
    except LineBotApiError as e:
        abort(400)


    if exist_in_database(user_id = user_id,group_id = group_id):
        #change the data
        user_data_in_db = usermessage.query.filter_by(user_id = user_id,group_id = group_id).first()
        
        #change the data you retrieve
        #....
        db.session.commit()

    else:   
    #insertdata
        print('-----in----------')
        add_data = usermessage(
                id = bodyjson['events'][0]['message']['id'],
                user_id = user_id,
                group_id = group_id,
                achievement = "",
                text_times = 1,
                month_text_times = 1,
                open_times = 0,
                month_open_times = 0,
                birth_date = datetime.fromtimestamp(user_timestamp),
                record_month = user_month,
                user_name = profile.display_name,
                game_name = ""
            )
        db.session.add(add_data)
        db.session.commit()

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# self defined function area
#======================================================
def exist_in_database(user_id,group_id):
    return bool(usermessage.query.filter_by(user_id = user_id,group_id = group_id).first())

def find_in_database_user_name(user_name,group_id):
    rule = or_(*[usermessage.user_name.ilike(w) for w in user_name])
    rule2 = or_(*[usermessage.game_name.ilike(w) for w in user_name])
    user_data = usermessage.query.filter(and_(usermessage.group_id == group_id,or_(rule,rule2)))
    if bool(user_data.first()):
        return user_data
    else:
        return None

#======================================================
#End of self-defined function


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    admin_user_id = ["ADMIN_USER_ID"]#choose who can execute the admin command

    if event.source.type == "group":
        group_id = event.source.group_id
    else:
        group_id = ""




    if (event.source.user_id in admin_user_id) and (event.message.text.lower() == "display@"):
        display_user_data =  usermessage.query.filter_by(group_id = group_id)
        message = generate_reply_format_display(display_user_data)
        line_bot_api.reply_message(event.reply_token,message)

    elif (event.source.user_id in admin_user_id) and (event.message.text.lower() == "clean_month@"):
        clean_user_data = usermessage.query.filter_by(group_id = group_id)
        for _data in clean_user_data:
            _data.month_text_times = 0
            _data.month_open_times = 0
            db.session.commit()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "Clean Month!"))

    elif (event.source.user_id in admin_user_id) and (event.message.text.lower() == "clean_all@"):
        clean_user_data = usermessage.query.filter_by(group_id = group_id)
        for _data in clean_user_data:
            _data.text_times = 0
            _data.month_text_times = 0
            _data.open_times = 0
            _data.month_open_times = 0
            db.session.commit()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = "Clean Clear!"))

    elif fnmatch(event.message.text.lower().replace("＠","@") ,"我叫*@") and event.message.text.lower()!="我叫@":
        change_name_data = usermessage.query.filter_by(user_id = event.source.user_id,group_id = group_id).first()
        change_name_data.game_name = event.message.text[2:-1].strip(" ")
        user_name = change_name_data.user_name
        db.session.commit()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text = user_name + " 叫 " + event.message.text[2:-1].strip(" ") + " 啊～"))

        #search user name or game name
    elif fnmatch(event.message.text.lower().replace("＠","@"),"@*@") and any(s.isalpha() or s.isnumeric() for s in event.message.text.lower()):
        search_string_list = ['%{}%'.format(s) for s in event.message.text.lower().replace("@"," ").replace("＠"," ").split(" ") if len(s)!=0]
        search_user_data = find_in_database_user_name(search_string_list,group_id)
        if search_user_data != None:
            message = generate_name_link_reply_format(search_user_data)
            line_bot_api.reply_message(event.reply_token,message)
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text = str(search_string_list)))

    elif event.message.text.lower() == "help@":
        line_bot_api.reply_message(event.reply_token,help_reply_message())




import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)