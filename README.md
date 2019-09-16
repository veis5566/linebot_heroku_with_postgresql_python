# line_bot_heroku_sql_python

Before we start to push database up to postgresql, we need to install required packages on our PC:

    pip install Flask-Migrate
    pip install Flask-Script
    pip install psycopg2

After the installation on our command line, we need to initialize the database first.

1.initial

    python dbModel.py db init
2.Migrate

    python dbModel.py db migrate
3.Upgrade

    python dbModel.py db upgrade
    
If we need to add or delete column in your database, we just need to repeat step 2 and 3.

At last, we need to push all of our code to heroku:

    heroku login
    git init
    heroku git:remote -a {HEROKU_APP_NAME}
    
    git add .
    git commit -am "Add Code"
    git push heroku master
    
