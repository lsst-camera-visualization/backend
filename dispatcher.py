import json
import os
from optparse import OptionParser
import sys
import tempfile
import numpy


# from tasks import tasks

def tasks(param):
    return {'result': 'success'}, None

usage = "usage: %prog [options]"
parser = OptionParser(usage=usage)


# add parameter readings
parser.add_option("-d", "--work", dest="workdir",
                  help="work directory", metavar="DIR")
parser.add_option("-i", "--in", dest="infile",
                  help="json file with task params", metavar="FILE")
parser.add_option("-n", "--name", dest="task",
                  help="task name (no spaces)", metavar="TASK")
parser.add_option("-o", "--outdir", dest="outdir",
                  help="directory for the final output file", metavar="DIR")
parser.add_option("-s", "--sep", dest="separator", default='___TASK STATUS___',
                  help="separator string, after which task status is written", metavar="STR")


# read the paremeters
(options, args) = parser.parse_args()
taskParams = None
with open(options.infile) as paramfile:
    taskParams = json.load(paramfile)

result, error = tasks(taskParams)


(fd, outfile) = tempfile.mkstemp(suffix=".json", prefix=options.tasks, dir=options.outdir)
f = os.open(fd)
json.dump(result, f)
json.dump(result, open('/www/algorithm/log2', 'w'))

os.system("echo here > /www/algorithm/log3")

if error:
    status = {"error": " ".join(errors)}
    print(json.dumps(status))
    sys.exit(1)
else:
    status = {"outfile": outfile}
    print(json.dumps(status))




