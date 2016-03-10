# -*- coding: utf8 -*-
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

def get_pron_snips(file_name):
    snips = []
    pronouns = ['он', 'она', 'оно', 'они', 'я', 'свой', 'мой', 'себе', 'который']
    with open(file_name, encoding='utf-8') as f1:
        text = f1.read()
        text = text.split()
    for i in range(len(text)):
        p = morph.parse(text[i])[0].normal_form
        if p in pronouns:
            if text[i-24] and text[i+5]:
                snips.append(text[i-24:i+5])
            else:
                snips.append(text[:i+5])
    return snips
for q in get_pron_snips('anaphora/3.txt'):
    print(q)



