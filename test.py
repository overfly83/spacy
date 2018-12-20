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
    print(document.ents)
    labels = set([w.label_ for w in document.ents])
    for label in labels:
        entities = [cleanup(e.string, lower=False) for e in document.ents if label == e.label_]
        entities = list(set(entities))
        print(label, entities)


def generate_noun(document):
    for np in document.noun_chunks:
        print(np.text, np.root.dep_, np.root.head.text)


if __name__ == '__main__':
    doc = nlp(u'Please help me quickly lock the cell.')
    doc = nlp(u'Autonomous cars shift insurance liability toward manufacturers')
    # for token in doc:
    #     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #           token.shape_, token.is_alpha, token.is_stop)
    entity_recognization(doc)
    generate_noun(doc)
