from flask import request
from flask import Flask, url_for
from flask import render_template, redirect
from forms import InputForm
from CharacterCreator import create_pc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dndrandomizer'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Home')


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


if __name__ == '__main__':
    app.run()
