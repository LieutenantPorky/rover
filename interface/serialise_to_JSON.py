#! python
'''
Read stdinput and serialise key:value pairs to JSON output
'''
import json
import sys

byteDict = {}

for arg in sys.argv[1:]:
    #print(arg.split(":"))
    byteDict[arg.split(":")[0]] = int(arg.split(":")[1])

print(json.dumps(byteDict))
