#modules https://github.com/StarMiner99/musik/raw/master/source/modules.py
#main https://github.com/StarMiner99/musik/raw/master/source/main.py
#update https://minhaskamal.github.io/DownGit/#/home?url=https://github.com/StarMiner99/musik/tree/master/source
import subprocess
import hashlib
import os
import urllib.request
class updater:
    def look(self):
        changes = False
        ver = self.onlinemd5sum("https://github.com/StarMiner99/musik/raw/master/source/version")
        veroff = self.offlinemd5sum("version")
        if not ver == veroff:
            changes = True
        return changes
    def onlinemd5sum(self, link):
        out = subprocess.check_output("curl -sL " +link +" | md5sum | cut -d ' ' -f 1",shell = True)
        out = out.decode('utf-8').rstrip()
        return out
    def offlinemd5sum(self, file):
        dirpath = os.path.dirname(os.path.realpath(__file__))
        return hashlib.md5(open(dirpath+"/"+file,'rb').read()).hexdigest()