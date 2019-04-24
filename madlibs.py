"""A madlib game that compliments its users."""

from random import choice, choices

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = choices(AWESOMENESS, k=3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    answer = request.args.get("start-game")

    if answer == 'yes':
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    
    madlib =choice(["madlib.html","madlib2.html", "madlib3.html"])
    return render_template(madlib, 
        color=request.args.get("color"),
        person=request.args.get("person"),
        noun=request.args.get("noun"),
        adjective=request.args.get("adjective"),
        exclamation=request.args.get("exclamation"),
        today1=request.args.get("today1"),
        today2=request.args.get("today2"),
        today3=request.args.get("today3")
        )


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)

#checkbox1 value = "interesting", checkbox2 value = "crazy"
#request.args.get("checkboxes") =? ["interesting", "crazy"]