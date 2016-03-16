# here we get the current path of this script so that we can specify things relative to
# this script, rather than the execution folder. And the modules path...
import sys, os
from os.path import dirname, join
ScriptPath = dirname(__file__)
RunScript = os.path.abspath(os.path.join(ScriptPath, "run.py"))
Root = os.getcwd()

import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'
import matplotlib.pyplot as plt
import json
from subprocess import run, DEVNULL
from pprint import pprint

# having trouble with conflicting MKL DLLs if do this all in one script?!
resultsFileName = os.path.abspath(os.path.join(Root, "results.json"))
#default parameters - results
run(["python", RunScript], stdout=DEVNULL)
with open(resultsFileName) as resultsFile:
    results = json.load(resultsFile)

labelText = str(results["materialParameters"])
plt.plot(results["fibre"]["strain"], results["fibre"]["stress"], "b-", label=labelText)
plt.plot(results["cross"]["strain"], results["cross"]["stress"], "b--")

run(["python", RunScript, "2.0", "5.0", "10.0", "5.0"], stdout=DEVNULL)
with open(resultsFileName) as resultsFile:
    results = json.load(resultsFile)

labelText = str(results["materialParameters"])
plt.plot(results["fibre"]["strain"], results["fibre"]["stress"], "g-", label=labelText)
plt.plot(results["cross"]["strain"], results["cross"]["stress"], "g--")

run(["python", RunScript, "1.0", "10.0", "10.0", "5.0"], stdout=DEVNULL)
with open(resultsFileName) as resultsFile:
    results = json.load(resultsFile)

labelText = str(results["materialParameters"])
plt.plot(results["fibre"]["strain"], results["fibre"]["stress"], "r-", label=labelText)
plt.plot(results["cross"]["strain"], results["cross"]["stress"], "r--")


plt.ylim(ymax=50)
plt.ylabel('some numbers')
plt.legend()
plt.show()
