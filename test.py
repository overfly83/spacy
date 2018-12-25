#!/usr/bin/env python
# coding: utf8
import spacy
from spacy.symbols import VERB, nsubj, root, dobj
nlp = spacy.load('en_core_web_sm')


noisy_pos_tags = ['PUNCT', 'DET', 'X']
min_token_length = 2


def is_noise(token):
    b_noise = False
    if token.pos_ in noisy_pos_tags:
        b_noise = True
    elif token.is_stop:
        b_noise = True
    elif len(token.string) <= min_token_length:
        b_noise = True
    return b_noise


def cleanup(token, lower=True):
    if lower:
        token = token.lower()
    return token.strip()


def entity_recognition(document):
    labels = set([ent.label_ for ent in document.ents])
    for label in labels:
        entities = [cleanup(e.string, lower=False) for e in document.ents if label == e.label_]
        entities = list(set(entities))
        print('label, entities: ', label, entities)


def generate_noun(document):
    for np in document.noun_chunks:
        print('np.text, np.root.dep_, np.root.head.text, np.sent.ents: ', np.text, np.root.dep_, np.root.head.text, np.sent.ents)


def find_verb(document):
    verbs = set()
    for possible_subject in document:
        if (possible_subject.dep == nsubj or possible_subject.dep_ == 'ROOT') and possible_subject.head.pos == VERB:
            verbs.add(possible_subject.head)
    for possible_verb in doc:
        if possible_verb.pos == VERB:
            for possible_subject in possible_verb.children:
                if possible_subject.dep == nsubj:
                    verbs.add(possible_verb)
                    break
    return verbs


def find_direct_object(verbs):
    dire_objects = []
    for verb in verbs:
        for child in verb.children:
            if child.dep == dobj:
                dire_objects.append(child)
    return dire_objects


if __name__ == '__main__':
    verbs = set()
    print(u'=========================================')
    sentence = u'Please help me quickly lock the cell.'
    print(sentence)
    doc = nlp(sentence)
    entity_recognition(doc)
    generate_noun(doc)
    verbs = find_verb(doc)
    print(verbs)
    print(find_direct_object(verbs))
    print(u'=========================================')
    sentence = u'Autonomous cars shift insurance liability toward manufacturers'
    print(sentence)
    doc = nlp(sentence)
    entity_recognition(doc)
    generate_noun(doc)
    verbs = find_verb(doc)
    print(verbs)
    print(find_direct_object(verbs))
    print(u'=========================================')
    sentence = u'Lock the cell of year 2016'
    print(sentence)
    doc = nlp(sentence)
    entity_recognition(doc)
    generate_noun(doc)
    verbs = find_verb(doc)
    print(verbs)
    print(find_direct_object(verbs))
    print(u'=========================================')
    sentence = u'Lock the cell from year 2016 to year 2018'
    print(sentence)
    doc = nlp(sentence)
    entity_recognition(doc)
    generate_noun(doc)
    verbs = find_verb(doc)
    print(verbs)
    print(find_direct_object(verbs))
    print(u'=========================================')
    sentence = u'Lock the cell of actual data in 2018'
    print(sentence)
    doc = nlp(sentence)
    entity_recognition(doc)
    generate_noun(doc)
    verbs = find_verb(doc)
    print(verbs)
    print(find_direct_object(verbs))
    print(u'=========================================')
    sentence = u'I don\'t lock that cell, I lock this cell'
    print(sentence)
    doc = nlp(sentence)
    entity_recognition(doc)
    generate_noun(doc)
    verbs = find_verb(doc)
    print(verbs)
    print(find_direct_object(verbs))
    print(u'=========================================')
    sentence = u'Navigate to the model lists page'
    print(sentence)
    doc = nlp(sentence)
    entity_recognition(doc)
    generate_noun(doc)
    verbs = find_verb(doc)
    print(verbs)
    print(find_direct_object(verbs))
