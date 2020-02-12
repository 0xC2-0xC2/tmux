#!/usr/bin/env python
# by an4kein

import os
from os import path

os.system('sudo apt install python-pip -y')
package = "wget"
try:
    import wget
except:
    os.system("sudo pip install " + package)

def main():
    if  path.isfile('.tmux.conf') == True:
        print(".tmux.conf exist!")
    elif path.isfile('.tmux.conf') == False:
        print("Download .tmux.conf and TMUX-PLUGINS")
        if path.isdir('/opt/tmux-plugins/') == True:
            print("Exist plugins into /opt/ download only .tmux.conf")
            os.system('sudo wget https://raw.githubusercontent.com/an4kein/tmux/master/.tmux.conf')
        elif path.isdir('/opt/tmux-plugins') == False:
            os.system('sudo git clone https://github.com/tmux-plugins/tmux-logging.git /opt/tmux-plugins/')
            os.system('sudo wget https://raw.githubusercontent.com/an4kein/tmux/master/.tmux.conf')

if __name__== "__main__":
    main()
