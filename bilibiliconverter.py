#!/usr/bin/python3
# Maintainer: Estela ad Astra <i@estela.cn>
# License: AGPL3

import os
import json
import re
for root, dirs, files in os.walk("./", topdown=False):
    if "entry.json" in files:
        i = open(os.path.join(root, "entry.json"), "r")
        info = json.load(i)
        i.close()
        print("---")
        print(root)
        name = info["title"]
        if "page_data" in info:
            if "download_subtitle" in info["page_data"]:
                name = name + info["page_data"]["download_subtitle"]
        elif "ep" in info:
            name = info["ep"]["index"]
        name = re.sub(r'(?=[\x20-\x7e]+)[^A-Za-z0-9]+', "_", name)
        print(name)
        os.system("ffmpeg -i %s/video.m4s -i %s/audio.m4s -vcodec copy -acodec copy '%s.mp4' -loglevel quiet" %
                  (os.path.join(root, dirs[0]), os.path.join(root, dirs[0]), os.getcwd()+"/"+name))
