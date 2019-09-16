# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 10:54:15 2017
@author: goingcosme20
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://...'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class usermessage(db.Model):
    __tablename__ = 'usermessage'

    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String(50))
    group_id = db.Column(db.String(50))
    achievement = db.Column(db.Text)
    #===========
    text_times = db.Column(db.Integer)
    month_text_times = db.Column(db.Integer)
    #===========
    open_times = db.Column(db.Integer)
    month_open_times = db.Column(db.Integer)
    #===========
    birth_date = db.Column(db.TIMESTAMP)
    record_month = db.Column(db.String(5))
    #===========
    user_name = db.Column(db.Text)
    game_name = db.Column(db.Text)

    def __init__(self
                 , id
                 , user_id
                 , group_id
                 , achievement
                 , text_times
                 , month_text_times
                 , open_times
                 , month_open_times
                 , birth_date
                 , record_month
                 , user_name
                 , game_name
                 ):
        self.id = id
        self.user_id = user_id
        self.group_id = group_id
        self.achievement = achievement
        self.text_times = text_times
        self.month_text_times = month_text_times
        self.open_times = open_times
        self.month_open_times = month_open_times
        self.birth_date = birth_date
        self.record_month = record_month
        self.user_name = user_name
        self.game_name = game_name


if __name__ == '__main__':
    manager.run()