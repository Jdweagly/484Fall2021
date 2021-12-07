from flask import request, session, redirect, render_template, url_for
from flask import Flask, url_for
from flask_pymongo import PyMongo
from flask import render_template, redirect
import bcrypt
from forms import InputForm
from CharacterCreator import create_pc
from MapNPCCreator import create_setting
from VillianCreator import create_Villan
import random

Setting = ["Desert", "Haunted Town", "Tavern", "Magical University", "Forrest", "Mountains"]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dndrandomizer'

app.config['MONGO_DBNAME'] = 'COSCwebdev'
app.config['MONGO_URI'] = 'mongodb+srv://admin:Password123@coscwebdev.pywpm.mongodb.net/COSCwebdev?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/signup', methods=['GET'])



@app.route('/', methods=['GET'])
def index():
    if 'username' in session:
        return render_template('charactergen.html', title='Home', user=session['username'])
    return render_template('index.html', title='index')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    userlogin = users.find_one({'name': request.form['username']})
    if userlogin:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), userlogin['password']) == userlogin['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    return 'Your Username and Password do not match'



@app.route('/sign_out')
def sign_out():
    print("got this far")
    session.pop('username', None)

    return redirect(url_for('index'))


@app.route('/welcomepage', methods=['GET', 'POST'])
def welcomePage():

    if request.method == 'POST':

        users = mongo.db.users
        exisiting_user = users.find_one({'name' : request.form['username']})

        if exisiting_user is None:

            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())

            print("got this far")
            users.insert_one({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return 'That username already exists!'
    return render_template('welcomePage.html')
@app.route('/input', methods=['GET', 'POST'])
def input():
    form = InputForm()
    if form.validate_on_submit():
        character_name = {form.character_name.data}
        return redirect(url_for('output', character_name=character_name))

    return render_template('input.html', title='Enter Data', form=form)


@app.route('/output', methods=['GET'])
def output():
    name = request.args.get('character_name').split("'")[1]
    value = create_pc()
    return render_template('output.html', title='Output', name=name, result=value)


@app.route('/setting', methods=['GET'])
def npc():
    story_setting = random.choice(Setting) 
    value = create_pc()
    return render_template('setting.html', title='NPC', result=value, Setting = story_setting)

@app.route('/villain', methods=['GET'])
def villain():
    value = create_Villan()
    return render_template('villain.html', title='Villain', result=value)


if __name__ == '__main__':
    app.run()
