from flask import request, session, redirect, render_template, url_for
from flask import Flask, url_for
from flask_pymongo import PyMongo
from flask import render_template, redirect
import bcrypt
from forms import InputForm
from CharacterCreator import create_pc
from MapNPCCreator import getNPC
from VillianCreator import create_Villan
import random




Setting = ["Desert", "Haunted Town", "Tavern", "Magical University", "Forrest", "Mountains"]
Desert_NPC = ["Sorcerer"]
Haunted_Town_NPC = ["Cleric", "Paladin"]
Tavern_NPC = ["Rogue", "Fighter"]
Magical_University_NPC = ["Wizard"]
Forrest_NPC = ["Druid", "Ranger"]
Mountains_NPC = ["Barbarian", "Ranger"]
Race_Choices = ['Human', 'Half-Elf', 'Elf', 'Dwarf', 'Half-Orc', 'Halfling', 'Tiefling', 'Dragonborn', 'Gnome']

Villian_Choices = ['Dragon', 'Vampire', 'Orc Warchief', 'Giant', 'Lich', 'Hydra']
Dragon_desc = "The odor of sulfur and pumice surrounds a red dragon, whose swept-back horns and spinal frill define its silhouette. Its beaked snout vents smoke at all times, and its eyes dance with flame when it is angry."
Vampire_desc = "An undead creature. Looks as it did in life, with pale skin, haunting red eyes, and a feral cast to its features. "
OrcWarchief_desc = "The war chief of an orc tribe is its strongest and most cunning member. The reign of a war chief lasts only as long as it commands the fear and respect of other tribe members, whose bloodlust must be regularly satisfied lest the chief appear weak."
Giant_desc = "Giants are humanoid creatures of great strength and size. All giants have low-light vision."
Lich_desc = "A lich is an evil humanoid spellcaster who has become undead through the use of dark magic. Their iconic ability is to cheat death by hiding their soul in an object known as a phylactery."
Hydra_desc = "The hydra is a reptilian horror with a crocodilian body and multiple heads on long, serpentine necks. Although its heads can be severed, the hydra magically regrows them in short order."
Dragon_abilites = ['Multiattack: The dragon can use its Frightful Presence. It then makes three attacks: one with its bite and two with its claws.', 'Claw: Melee Weapon Attack: +17 to hit, reach 10 ft., one target. Hit: 17 (2d6 + 10) slashing damage.' , 'Tail: Melee Weapon Attack: +17 to hit, reach 20 ft., one target. Hit: 19 (2d8 + 10) bludgeoning damage.', 'Fire Breath: The dragon exhales fire in a 90-foot cone. Each creature in that area must make a DC 24 Dexterity saving throw, taking 91 (26d6) fire damage on a failed save']
Vampire_abilities = ['Multiattack: The vampire makes three attacks, only one of which can be a bite attack.', 'Bite:  Melee Weapon Attack: +14 to hit, reach 5 ft., one willing creature, or a creature that is grappled by the vampire, incapacitated, or restrained. Hit: 16 (3d6 + 6) piercing damage plus 21 (6d6) necrotic damage.', 'Claw: Melee Weapon Attack: +14 to hit, reach 5 ft, one creature. Hit: 11 (1d10 + 6) bludgeoning damage. ', 'Vamparic Touch: Melee Spell Attack: +15 to hit, reach 10 ft., one creature. Hit: 28 (6d6 + 7) necrotic damage. The vampire regains hit points equal to half the necrotic damage dealt.', 'Charm: The vampire targets one humanoid it can see within 30 feet of it. If the target can see the vampire lord, the target must succeed on a DC 23 Wisdom saving throw against this magic or be charmed by the vampire.']
Orc_abilities = ['Multiattack: The orc makes two attacks with its greataxe or its spear.', 'Great-axe: Melee Weapon Attack: +6 to hit, reach 5 ft., one target. Hit: 15 (1d12 + 4 plus 1d8) slashing damage.', 'Spear: Melee or Ranged Weapon Attack: +6 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 12 (1d6 + 4 plus 1d8) piercing damage.', 'Battle Cry: Each creature of the war chief’s choice that is within 30 feet of it, can hear it, and not already affected by Battle Cry gain advantage on attack rolls until the start of the war chief’s next turn. ']
Giant_abilities = ['Multiattack: The giant makes two greatclub attacks', 'Greatclub: Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: (3d8 + 5) bludgeoning damage.', 'Rock:  Ranged Weapon Attack: +8 to hit, reach 60/240 ft., one target. Hit: (3d10 + 5) bludgeoning damage.']
Lich_abilities = ['Paralyzing Touch: Melee Spell Attack: +12 to hit, reach 5 ft., one creature. Hit: 10 (3d6) cold damage. The target must succeed on a DC 18 Constitution saving throw or be paralyzed for 1 minute. ']
Hydra_abilities = ['Multiattack: The hydra makes as many bite attacks as it has heads.', 'Bite: Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: (1d10 + 5) piercing damage.']


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


@app.route('/npc', methods=['GET'])
def npc():
    selected_race = random.choice(Race_Choices)
    selected_setting = random.choice(Setting)
    value = getNPC(selected_setting)
    return render_template('npc.html', title='NPC', result=value)

@app.route('/villain', methods=['GET'])
def villain():
    value = create_Villan()
    return render_template('villain.html', title='Villain', result=value)


if __name__ == '__main__':
    app.run()
