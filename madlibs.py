from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """Play game?"""
    answer = request.args.get("question")

    if answer == 'sure_fine_whatever':
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Show madlib"""

    madlib_person = request.args.get("madlib_person")
    madlib_noun = request.args.get("madlib_noun")
    madlib_adj = request.args.get("madlib_adj")
    madlib_color = request.args.get("madlib_color")
    real_or_fake = request.args.get("real_or_fake")
    celebrity1 = request.args.get("celebrity1")
    celebrity2 = request.args.get("celebrity2")
    celebrity3 = request.args.get("celebrity3")
    plural_body_part = request.args.get("plural_body_part")
    place = request.args.get("place")
    plural_noun = request.args.get("plural_noun")
    verb_ing = request.args.get("verb_ing")


    return render_template("madlib.html",
                        madlib_person=madlib_person,
                        madlib_noun=madlib_noun,
                        madlib_adj=madlib_adj,
                        madlib_color=madlib_color,
                        real_or_fake=real_or_fake, 
                        celebrity1=celebrity1,
                        celebrity2=celebrity2,
                        celebrity3=celebrity3,
                        plural_body_part=plural_body_part,
                        place=place,
                        plural_noun=plural_noun,
                        verb_ing=verb_ing)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
