#!/usr/env/bin python3

import py7zr
import os
from shutil import copyfile

model_list = []
with py7zr.SevenZipFile('svencoop_addon.7z', mode='r') as archive:
    for name in archive.getnames():
        if name.endswith('.mdl'):
            model_list.append(os.path.normpath('svencoop_addon/' + name))

print('Models to be replaced:', len(model_list))
for model in model_list:
    if os.path.isfile(model):
        continue
    os.makedirs(os.path.dirname(model), exist_ok=True)
    copyfile('replace.mdl', model)