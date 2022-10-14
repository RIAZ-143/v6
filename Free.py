import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from v6 import riaz

    riaz()

elif bit == '32bit':

    from v6s import riaz

    riaz()
