#!/usr/bin/env python
# coding: utf8
import spacy
nlp = spacy.load('en_core_web_sm')

noisy_pos_tags = ['PUNCT', 'DET', 'X']
min_token_length = 2


def isNoise(token):
    is_noise = False
    if token.pos_ in noisy_pos_tags:
        is_noise = True
    elif token.is_stop:
        is_noise = True
    elif len(token.string) <= min_token_length:
        is_noise = True
    return is_noise


def cleanup(token, lower=True):
    if lower:
        token = token.lower()
    return token.strip()


def entity_recognization(document):
    labels = set([ent.label_ for ent in document.ents])
    print(labels)
    for label in labels:
        entities = [cleanup(e.string, lower=False) for e in document.ents if label == e.label_]
        entities = list(set(entities))
        print('label, entities: ', label, entities)


def generate_noun(document):
    for np in document.noun_chunks:
        print(np.text, np.root.dep_, np.root.head.text, np.sent.ents)


if __name__ == '__main__':
    print(u'=========================================')
    doc = nlp(u'Please help me quickly lock the cell.')
    entity_recognization(doc)
    generate_noun(doc)
    print(u'=========================================')
    doc = nlp(u'Autonomous cars shift insurance liability toward manufacturers')
    entity_recognization(doc)
    generate_noun(doc)
    print(u'=========================================')
    doc = nlp(u'Lock the cell of year 2016')
    entity_recognization(doc)
    generate_noun(doc)
    print(u'=========================================')
    doc = nlp(u'Lock the cell from year 2016 to year 2018')
    entity_recognization(doc)
    generate_noun(doc)
    print(u'=========================================')
    doc = nlp(u'Lock the cell of actual data in 2018')
    entity_recognization(doc)
    generate_noun(doc)
    # for token in doc:
    #     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #           token.shape_, token.is_alpha, token.is_stop)

