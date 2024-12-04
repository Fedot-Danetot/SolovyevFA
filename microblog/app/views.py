from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Fedot_Danetot' } # выдуманный пользователь
    posts = [
        {
            'author': { 'nickname': 'Petr' },
            'body': { 'Another good day in Germany'}
        },
        {
            'author': { 'nickname': 'Adam' },
            'body': { 'I love studying medicine!'}
        }
    ]
    return render_template("index.html",
                           title = 'Home',
                           user = user,
                           posts = posts)