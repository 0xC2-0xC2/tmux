#!/usr/bin/env python3
# by an4kein

import os
from os import path


url = 'https://raw.githubusercontent.com/an4kein/tmux/master/.tmux.conf'
tmux_plugins = 'https://github.com/tmux-plugins/tmux-logging.git'

def main():
    if  path.isfile('.tmux.conf') == True:
        print(".tmux.conf exist!")
    elif path.isfile('.tmux.conf') == False:
        print("Download .tmux.conf and TMUX-PLUGINS")
        if path.isdir('/opt/tmux-plugins/') == True:
            print("Exist plugins into /opt/ download only .tmux.conf")
            os.system((f'sudo wget{url}'))
        elif path.isdir('/opt/tmux-plugins') == False:
            os.system(f'sudo git clone {tmux_plugins} /opt/tmux-plugins/')
            os.system(f'sudo wget {url}')

if __name__== "__main__":
    main()
