# About
Python script to symlink (symbolic link) all hotkeys/account variables to new accounts so you don't need to manually copy over `Hotkeys` directory/`variables.txt` when creating a new account/moving operating systems. This way all hotkey profiles/account settings are "synced" between all SC2 accounts. Requires a bit of setup but may be useful for people with tons of accounts/are moving OS.

Note that some settings are synced to battle.net/Starcraft 2 (not loaded from variables.txt) directly and need to be explicitly set within Starcraft 2 (e.g. Hotkey profile - but doesnt need to be copied to new account directory)

## Usage
```
usage: python s2_settings.py [-h] [-k] [-v] dir

positional arguments:
  dir              Path to StarCraft II Documents directory

options:
  -h, --help       show this help message and exit

include (at least one of these flags is required):
  files to symlink to all accounts

  -k, --hotkeys    Copy hotkeys from $dir/Hotkeys to all accounts
  -v, --variables  Copy variables from $dir/Account-Variables/Variables.txt to
                   all accounts
```

## Steps
- Copy `Hotkeys` you want to symlink to `Documents/Starcraft ll/Hotkeys`
- Copy `Variables.txt` you want to sync (should be one from the accounts directory not the root `Starcraft ll` directory into `Documents/Starcraft ll/Account-Variables`
- Log into new account on SC2 (any region) 
- Close SC2
- Run script

For ease of use a run.sh script is provided in the scripts directory. Be sure to create a vars.sh in the same directory with `sc_dir` variable defined.
e.g.
```
# modify this to your StarCraft II Documents directory
sc_dir="/home/<username>/Games/battlenet/drive_c/users/<username>/Documents/StarCraft II"
```

Make sure python is installed and in your `PATH` before running.
