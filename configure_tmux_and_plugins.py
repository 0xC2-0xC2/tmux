#!/usr/bin/env python
# by an4kein
from tqdm import tqdm
import requests
import os
import os.path
from os import path

def main():
    if  path.isfile('.tmux.conf') == True:
        print(".tmux.conf exist!")
    elif path.isfile('.tmux.conf') == False:
        print("Download .tmux.conf and TMUX-PLUGINS")
        os.system("sudo git clone https://github.com/tmux-plugins/tmux-logging.git /opt/tmux-plugins/")

        print("Download my config tmux from github")
        url = "https://raw.githubusercontent.com/an4kein/tmux/master/.tmux.conf"
        file = requests.get(url, stream=True)
        with open(".tmux.conf", "wb") as handle:
            for data in tqdm(file.iter_content()):
                handle.write(data)


if __name__== "__main__":
    main()
