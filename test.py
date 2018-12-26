#!/usr/bin/env python
# coding: utf8
from spacyrest.rest.spacy.SacParse import SacParse
import json

if __name__ == '__main__':

    print(u'=========================================')
    sentence = u'Please help me quickly lock the cell.'
    print(sentence)
    sp = SacParse()
    doc = sp.read_document(sentence)
    ents_json = sp.entity_recognition(doc)
    verb_dobj = sp.generate_verb_dobj(doc)
    if ents_json:
        print(ents_json)
    print(sp.generate_verb_dobj(doc))
    print(u'=========================================')
    sentence = u'Autonomous cars shift insurance liability toward manufacturers'
    print(sentence)
    sp = SacParse()
    doc = sp.read_document(sentence)
    ents_json = sp.entity_recognition(doc)
    verb_dobj = sp.generate_verb_dobj(doc)
    if ents_json:
        print(ents_json)
    print(sp.generate_verb_dobj(doc))
    print(u'=========================================')
    sentence = u'Lock the actual data from year 2016 to year 2018.'
    print(sentence)
    sp = SacParse()
    doc = sp.read_document(sentence)
    ents_json = sp.entity_recognition(doc)
    verb_dobj = sp.generate_verb_dobj(doc)
    if ents_json:
        print(ents_json)
    print(sp.generate_verb_dobj(doc))
    print(u'=========================================')
    sentence = u'Lock the actual data in 2016'
    print(sentence)
    sp = SacParse()
    doc = sp.read_document(sentence)
    ents_json = sp.entity_recognition(doc)
    if ents_json:
        print(ents_json)
    print(sp.generate_verb_dobj(doc))
    print(u'=========================================')
    sentence = u'Lock the cell from year 2016 to year 2018'
    print(sentence)
    sp = SacParse()
    doc = sp.read_document(sentence)
    ents_json = sp.entity_recognition(doc)
    if ents_json:
        print(ents_json)
    print(sp.generate_verb_dobj(doc))
    print(u'=========================================')
    sentence = u'Lock the cell of actual data in 2018'
    print(sentence)
    sp = SacParse()
    doc = sp.read_document(sentence)
    ents_json = sp.entity_recognition(doc)
    if ents_json:
        print(ents_json)
    print(sp.generate_verb_dobj(doc))
    print(u'=========================================')
    sentence = u'I don\'t lock that cell, I lock this cell'
    print(sentence)
    sp = SacParse()
    doc = sp.read_document(sentence)
    ents_json = sp.entity_recognition(doc)
    if ents_json:
        print(ents_json)
    print(sp.generate_verb_dobj(doc))
    print(u'=========================================')
    sentence = u'go to nice model list page'
    print(sentence)
    sp = SacParse()
    doc = sp.read_document(sentence)
    ents_json = sp.entity_recognition(doc)
    if ents_json:
        print(ents_json)
    print(sp.generate_verb_dobj(doc))
    print(u'=========================================')
    sentence = u'go to model list'
    print(sentence)
    sp = SacParse()
    doc = sp.read_document(sentence)
    ents_json = sp.entity_recognition(doc)
    if ents_json:
        print(ents_json)
    print(sp.generate_verb_dobj(doc))
    print(u'=========================================')
    sentence = u'go to the model detail page'
    print(sentence)
    sp = SacParse()
    doc = sp.read_document(sentence)
    ents_json = sp.entity_recognition(doc)
    if ents_json:
        print(ents_json)
    print(sp.generate_verb_dobj(doc))
    print(u'=========================================')
    sentence = u'naivgate to the model detail page'
    print(sentence)
    sp = SacParse()
    doc = sp.read_document(sentence)
    ents_json = sp.entity_recognition(doc)
    if ents_json:
        print(ents_json)
    print(sp.generate_verb_dobj(doc))
    # displacy.serve(doc, style='dep')
