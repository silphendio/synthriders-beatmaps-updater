# synthriders-beatmaps-updater
A simple script to download all missing costum maps from synthriderz.com

### Setup:
- make sure `python` is installed. You can get it in the windows store.
- Download the code ( click `code` -> `download zip` on github, and extract the files somewhere)
- Edit the `synthriders-beatmaps-updater.py` to make sure that `beatmap_dir` is the costum maps directory
- (optional) create a desktop shortcut to the bat file
  on Windows 11:
  - right-click on desktop -> new -> shortcut
  - copy the bat file & paste it into the location box (dragging doesn't work)

To run it, just double-click the bat file

Use `synthriders-beatmaps-updater.bat` to download new maps.
It stops when it finds 100 new maps in a row that are already saved locally.

`synthriders-beatmaps-update-everything.bat` checks every published map on synthriderz.com. This can take a bit longer.
