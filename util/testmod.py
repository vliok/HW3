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
