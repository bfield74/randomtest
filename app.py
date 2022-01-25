from flask import Flask, render_template, request
from get_random import getr
import pandas as pd
from data_out import save_random

app = Flask(__name__)


@app.route('/random', methods=["POST", "GET"])
# launch page to the problem.
def random():
    rand = getr(0,100)
    print("here is the random int: ", rand)
    print("what is going on??")

    rand10 = getr(0,9)
    words = pd.read_csv("files/10words.csv")
    output = words['words'].tolist()

    randword = output[rand10]
    print("here is the random word we found: ", randword)

    if request.method == "POST":
        print("into post")
        save_random(rand, randword)
        return render_template("random.html", value=rand, word=randword)
    else:
        print("in else for post******")
        return render_template("random.html", value=-1, word=randword)

if __name__== "__web_output__":
    app.run(debug=True)