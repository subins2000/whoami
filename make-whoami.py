import base64
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

f = open(dir_path + '/than-aara.mp3', 'rb')
encoded = str(base64.b64encode(f.read()))
f.close()

f = open(dir_path + '/whoami.py', 'r')
program = f.read()
f.close()

shebang = '#!/usr/bin/env python3'

f = open('whoami', 'w')
f.write(shebang + "\n\naudio_b64 = " + encoded + "\n\n\n" + program)
f.close()
