import base64
import os
import playsound
import tempfile

audio = base64.b64decode(audio_b64)

t = tempfile.NamedTemporaryFile(mode='w+b')
t.write(audio)

tmp_loc = t.name

playsound.playsound(tmp_loc, True)

t.close()

os.system('/usr/bin/whoami')
