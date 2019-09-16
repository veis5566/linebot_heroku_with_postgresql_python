from linebot.models import *
import pytz
from dbModel import *

def generate_reply_format_display(user_data):

  user_name = ""
  text_times = ""
  month_text_times = ""
  open_times = ""
  month_open_times = ""
  last_time = ""
  flex_list = [6,2,2]

  for _data in user_data:
    if len(_data.user_name) >=9:
      user_name = user_name+ _data.user_name[:9] + "...\n"
    else:
      user_name = user_name + _data.user_name + "\n"

    text_times = text_times + str(_data.text_times) + "\n"
    month_text_times = month_text_times + str(_data.month_text_times) + "\n"
    open_times = open_times + str(_data.open_times) + "\n"
    month_open_times = month_open_times + str(_data.month_open_times) + "\n"
    last_time = last_time + _data.birth_date.astimezone(pytz.timezone('Asia/Taipei')).strftime('%b - %d') + "\n"


  flex_template = FlexSendMessage(alt_text = "結算資料"
        ,contents=
        {
        "type": "carousel",
        "contents": [
          {
            "type": "bubble",
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "【月結算】",
                  "weight": "bold",
                  "size": "lg",
                  "align": "center"
                },
                {
                  "type": "separator",
                  "margin": "md"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "vertical",
                      "flex": flex_list[0],
                      "contents": [
                        {
                          "type": "text",
                          "text": "姓名",
                          "align": "center",
                          "weight": "bold"
                        },
                        {
                          "type": "separator",
                          "margin": "none"
                        },
                        {
                          "type": "text",
                          "text": user_name,
                          "wrap": True,
                          "size": "sm",
                          "align": "center"
                        }
                      ]
                    },
                    {
                      "type": "separator",
                      "margin": "none"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "flex": flex_list[1],
                      "contents": [
                        {
                          "type": "text",
                          "text": "發言",
                          "align": "center",
                          "weight": "bold"
                        },
                        {
                          "type": "separator",
                          "margin": "none"
                        },
                        {
                          "type": "text",
                          "text": month_text_times,
                          "wrap": True,
                          "size": "sm",
                          "align": "center"
                        }
                      ]
                    },
                    {
                      "type": "separator",
                      "margin": "none"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "flex": flex_list[2],
                      "contents": [
                        {
                          "type": "text",
                          "text": "開房",
                          "align": "center",
                          "weight": "bold"
                        },
                        {
                          "type": "separator",
                          "margin": "none"
                        },
                        {
                          "type": "text",
                          "text": month_open_times,
                          "wrap": True,
                          "size": "sm",
                          "align": "center"
                        }
                      ]
                    },
                  ]
                }
              ]
            }
          },
          {
            "type": "bubble",
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "【總結算】",
                  "weight": "bold",
                  "size": "lg",
                  "align": "center"
                },
                {
                  "type": "separator",
                  "margin": "md"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "vertical",
                      "flex": flex_list[0],
                      "contents": [
                        {
                          "type": "text",
                          "text": "姓名",
                          "align": "center",
                          "weight": "bold"
                        },
                        {
                          "type": "separator",
                          "margin": "none"
                        },
                        {
                          "type": "text",
                          "text": user_name,
                          "wrap": True,
                          "size": "sm",
                          "align": "center"
                        }
                      ]
                    },
                    {
                      "type": "separator",
                      "margin": "none"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "flex": flex_list[1],
                      "contents": [
                        {
                          "type": "text",
                          "text": "發言",
                          "align": "center",
                          "weight": "bold"
                        },
                        {
                          "type": "separator",
                          "margin": "none"
                        },
                        {
                          "type": "text",
                          "text": text_times,
                          "wrap": True,
                          "size": "sm",
                          "align": "center"
                        }
                      ]
                    },
                    {
                      "type": "separator",
                      "margin": "none"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "flex": flex_list[2],
                      "contents": [
                        {
                          "type": "text",
                          "text": "開房",
                          "align": "center",
                          "weight": "bold"
                        },
                        {
                          "type": "separator",
                          "margin": "none"
                        },
                        {
                          "type": "text",
                          "text": open_times,
                          "wrap": True,
                          "size": "sm",
                          "align": "center"
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          },
          {
            "type": "bubble",
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "【最後發言日期】",
                  "weight": "bold",
                  "size": "lg",
                  "align": "center"
                },
                {
                  "type": "separator",
                  "margin": "md"
                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "vertical",
                      "flex": 6,
                      "contents": [
                        {
                          "type": "text",
                          "text": "姓名",
                          "align": "center",
                          "weight": "bold"
                        },
                        {
                          "type": "separator",
                          "margin": "none"
                        },
                        {
                          "type": "text",
                          "text": user_name,
                          "wrap": True,
                          "size": "sm",
                          "align": "center"
                        }
                      ]
                    },
                    {
                      "type": "separator",
                      "margin": "none"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "flex": 4,
                      "contents": [
                        {
                          "type": "text",
                          "text": "上線日",
                          "align": "center",
                          "weight": "bold"
                        },
                        {
                          "type": "separator",
                          "margin": "none"
                        },
                        {
                          "type": "text",
                          "text": last_time,
                          "wrap": True,
                          "size": "sm",
                          "align": "center"
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          }
        ]
      }
)
  return flex_template

def generate_name_link_reply_format(user_data):
  user_name = ""
  game_name = ""
  for _data in user_data:
    if len(_data.user_name) >=8:
      user_name = user_name+ _data.user_name[:8] + "...\n"
    else:
      user_name = user_name + _data.user_name + "\n"

    if len(_data.game_name) >=8:
      game_name = game_name + _data.game_name[:8] + "...\n"
    else:
      game_name = game_name + _data.game_name + "\n"

  flex_template = FlexSendMessage(alt_text = "姓名搜尋"
    ,contents = 
    {
    "type": "bubble",
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "【搜尋結果】",
          "weight": "bold",
          "size": "lg",
          "align": "center"
        },
        {
          "type": "separator",
          "margin": "md"
        },
        {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "box",
              "layout": "vertical",
              "flex": 1,
              "contents": [
                {
                  "type": "text",
                  "text": "Line姓名",
                  "align": "center",
                  "weight": "bold"
                },
                {
                  "type": "separator",
                  "margin": "none"
                },
                {
                  "type": "text",
                  "text": user_name,
                  "wrap": True,
                  "size": "sm",
                  "align": "center"
                }
              ]
            },
            {
              "type": "separator",
              "margin": "none"
            },
            {
              "type": "box",
              "layout": "vertical",
              "flex": 1,
              "contents": [
                {
                  "type": "text",
                  "text": "遊戲姓名",
                  "align": "center",
                  "weight": "bold"
                },
                {
                  "type": "separator",
                  "margin": "none"
                },
                {
                  "type": "text",
                  "text": game_name,
                  "wrap": True,
                  "size": "sm",
                  "align": "center"
                }
              ]
            }
          ]
        }
      ]
    }
  }
  )
  return flex_template

def help_reply_message():
  flex_template = FlexSendMessage(alt_text="幫助",
    contents = 
    {
      "type": "carousel",
      "contents": [
        {
          "type": "bubble",
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "【幫助】",
                "size": "lg",
                "weight": "bold",
                "align": "center"
              },
              {
                "type": "separator",
                "margin": "sm"
              },
              {
                "type": "text",
                "text": "設定自己名字",
                "weight": "bold",
                "align": "center"
              },
              {
                "type": "text",
                "text": "\n我叫[遊戲名稱]@\n\n例： 我叫veis@",
                "wrap": True,
                "size": "sm"
              },
              {
                "type": "separator",
                "margin": "sm"
              },
              {
                "type": "text",
                "text": "搜尋",
                "weight": "bold",
                "align": "center"
              },
              {
                "type": "text",
                "text": "\n@[姓名1] @[公司名字2] [姓名3] @\n\n例： @veis @",
                "wrap": True,
                "size": "sm"
              }
            ]
          }
        }
      ]
    }
    )
  return flex_template