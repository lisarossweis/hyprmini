#!/usr/bin/env python

import json
import sys

data = {}
message = 'waybar custom module'

if len(sys.argv) == 2:
    message = sys.argv[1]

data['text'] = ''
data['tooltip'] = message


print(json.dumps(data))
