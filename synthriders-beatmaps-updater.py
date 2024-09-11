#!/usr/bin/python

import urllib.request as url
import json
import os

# you may need to change this
beatmap_dir = 'C:/Program Files (x86)/Steam/steamapps/common/SynthRiders/SynthRidersUC/CustomSongs'

beatmaps_url = 'https://synthriderz.com/api/beatmaps?publishedOnly=true'

 # because synthriderz.com blocks the default user agent (Python-urllib) for some reason.
headers = {'User-Agent' : "dl-script"}

try:
    beatmaps = json.load(url.urlopen(url.Request(beatmaps_url, None, headers)))
except:
    print("ERROR: couldn't download beatmaps list")
    input()
    exit(1)

local_maps = set(os.listdir(beatmap_dir))


download_queue = [m for m in beatmaps if m['filename'] not in local_maps]

print(f'{len(download_queue)} files in queue')



for i, m in enumerate(download_queue):
    print(f'file {i}\tof {len(download_queue)}: {m['title']}')
    while True: # retry loop
        try:
            map_url = f'https://synthriderz.com/api/beatmaps/hash/download/{m['hash']}'
            print(f'fetching {map_url}...')
            beatmap = url.urlopen(url.Request(map_url, None, headers)).read()
        except:
            print('ERROR: download failed')
            input('press enter to retry...')
            continue
        try:
            path = os.path.join(beatmap_dir, m['filename'])
            print(f"save map to {path}")
            open(path, 'wb').write(beatmap)
            break
        except:
            print("ERROR: can't write to file")
            input('press enter to retry...')


input("all done!")
