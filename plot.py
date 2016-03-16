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

# having trouble with conflicting MKL DLLs if do this all in one script?!
resultsFileName = os.path.abspath(os.path.join(Root, "results.json"))
#default parameters - results
run(["python", RunScript], stdout=DEVNULL, stderr=DEVNULL)
with open(resultsFileName) as resultsFile:
    results = json.load(resultsFile)
 
plt.plot(results["fibre"])
plt.plot(results["cross"])
plt.ylabel('some numbers')
plt.show()
