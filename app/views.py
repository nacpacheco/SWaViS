from StringIO import StringIO
import urllib
import base64
import requests
import glymur
from PIL import Image

from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    file = StringIO(urllib.urlopen('https://api.helioviewer.org/v2/getJP2Image/?date=2014-01-01T23:59:59Z&sourceId=14').read())
    #print(file)
    #jp2 = glymur.Jp2k(img)
    img = Image.open(file)
    #img.write('CB_TM432.jpeg')
    rgb_im = img.convert('RGB')
    rgb_im.save('colors.png')
    # output = StringIO.StringIO()
    # im = Image.open(rgb_im)  # Your image here!
    # im.save(output, format='PNG')
    # output.seek(0)
    # output_s = output.read()
    # b64 = base64.b64encode(output_s)
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
