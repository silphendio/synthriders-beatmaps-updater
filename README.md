# synthriders-beatmaps-updater
A simple script to download all missing costum maps from synthriderz.com.(Steam/PC Version)
There's no User Interface. Just double-click the bat file and wait for it to finish.
It shouldn't take much longer than it takes to download everything.

### Setup:
- make sure `python` is installed. You can get it in the windows store.
- Download the code ( click `code` -> `download zip` on github, and extract the files somewhere)
- The script assumes that the costum maps are in `C:\Program Files (x86)\Steam\steamapps\common\SynthRiders\SynthRidersUC\CustomSongs`
  This should be the case in a stardard installation of the Synth Riders Beta Version.
  Otherwise, open `sr-update.py` with a text editor and change `beatmap_dir` on line 12.

Use `sr-update.bat` to download new maps.
It checks 100 maps at a time, newest first. When the 50 oldest of those were already installed, it stops checking.

`sr-update-all.bat` checks every published map on synthriderz.com. This takes a bit longer.
