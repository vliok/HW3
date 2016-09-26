#Vincent Liok
#SoftDev1 pd8
#HW03 -- ...and Now Enjoy Its Contents
#2016-09-25

from flask import Flask, render_template
app = Flask(__name__)

import util.testmod

occupations = util.testmod.convertToDict()

@app.route("/")
def mainPage():
    return "HELLO"

@app.route("/occupations")
def printTable():
    return render_template("table.html",title="Randomize",header="Find out what you will be in the future",dict=occupations,outcome=util.testmod.randomize(occupations))

if __name__ == "__main__" :
    app.debug = True
    app.run()
