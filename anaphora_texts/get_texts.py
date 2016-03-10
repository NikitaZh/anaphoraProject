# -*- coding: utf8 -*-

import shutil

texts_ids = open('Documents.txt', 'r', encoding='utf-8')
for line in texts_ids:
    line = line.split()
    line = line[1].split('/')
    print(line)
    shutil.copyfile(line[0] + '/' + line[1], 'anaphora/' + line[1])


