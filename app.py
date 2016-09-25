#Vincent Liok
#SoftDev1 pd8
#HW03 -- ...and Now Enjoy Its Contents
#2016-09-25

from flask import Flask, render_template
app = Flask(__name__)

import random

def convertToDict():
    file = open("occupations.csv","r")
    next(file)
    d = {}
    for line in file:
        if "\"" in line:
            line = line[1:]
            list = line.split("\",")
        else:
            list = line.split(",")
        d[ list[0] ] = float( list[1] )
    d.pop("Total")
    return d

def randomize(d):
    bound = 0.0
    randNum = random.random() * 99.8
    for job in d:
        bound += d[job]
        if randNum < bound:
            return job

occupations = convertToDict()

@app.route("/")
def mainPage():
    return "HELLO"

@app.route("/occupations")
def printTable():
    return render_template("table.html",title="Randomize",header="Find out what you will be in the future",dict=occupations,outcome=randomize(occupations))

if __name__ == "__main__" :
    app.debug = True
    app.run()
