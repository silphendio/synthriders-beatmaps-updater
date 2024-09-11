#!/usr/bin/python

import urllib.request as url
import json
import os
import sys
from itertools import count

# you may need to change this
beatmap_dir = 'C:/Program Files (x86)/Steam/steamapps/common/SynthRiders/SynthRidersUC/CustomSongs'


update_everything = len(sys.argv) > 1 and sys.argv[1] == "update-everything"
url_template = "https://synthriderz.com/api/beatmaps?select=title,filename,hash,published_at&limit=100&page={}&sort=published_at,DESC"
headers = {'User-Agent' : "dl-script"}  # because synthriderz.com blocks the default user agent (Python-urllib) for some reason.

try:
    local_maps = set(os.listdir(beatmap_dir))
except Exception as e:
    print(e, file=sys.stderr)
    input("press enter to exit...")
    exit(1)

download_queue = []
for i in count(1):
    try:
        print(f"fetching {url_template.format(i)} ...")
        response = json.load(url.urlopen(url.Request(url_template.format(i), None, headers)))
    except:
        print("ERROR: couldn't download beatmaps list", file=sys.stderr)
        input()
        exit(1)

    new_maps = [m for m in response['data'] if m['filename'] not in local_maps]
    download_queue += new_maps

    if not(new_maps or update_everything) or not response['data']:
        break

print(f'{len(download_queue)} files in queue')



for i, m in enumerate(download_queue):
    print(f'file {i}\tof {len(download_queue)}: {m['title']}')
    while True: # retry loop
        try:
            map_url = f'https://synthriderz.com/api/beatmaps/hash/download/{m['hash']}'
            print(f'fetching {map_url}...')
            beatmap = url.urlopen(url.Request(map_url, None, headers)).read()
        except:
            print('ERROR: download failed', file=sys.stderr)
            input('press enter to retry...')
            continue
        try:
            path = os.path.join(beatmap_dir, m['filename'])
            print(f"save map to {path}")
            open(path, 'wb').write(beatmap)
            break
        except:
            print("ERROR: can't write to file", file=sys.stderr)
            input('press enter to retry...')


input("all done!")
