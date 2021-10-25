# Anti-TWLZ model generator

## Requirements

* Python 3.9 or higher

## Usage

1. Place your `svencoop_addon.7z` from TWLZ (https://distfiles.lifeisabug.com/svencoop/playermodels/svencoop_addon.7z) in this folder
2. Copy some player `.mdl` file from Sven Co-op and rename it to `replace.mdl` (e.g. copy `uboa4.mdl` and rename it to `replace.mdl`)
3. Run the following command to install dependencies:
```
python -m pip install -r requirements.txt
```
Replace `python` with `python3` if it doesn't work.
4. Run the script with `python replace-models.py`