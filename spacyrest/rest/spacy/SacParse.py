import spacy
from spacy import displacy
from spacy.symbols import VERB, nsubj, root, dobj, prep, pobj, nn
import json


class SacParse:
    nlp = None
    spacy_model_name = 'en_core_web_sm'
    noisy_pos_tags = ['PUNCT', 'DET', 'X']
    min_token_length = 2

    def __init__(self, spacy_model_name=None):
        if spacy_model_name:
            self.spacy_model_name = spacy_model_name
        self.nlp = spacy.load(self.spacy_model_name)

    def read_document(self, text):
        return self.nlp(text)

    def is_noise(self, token):
        b_noise = False
        if token.pos_ in self.noisy_pos_tags:
            b_noise = True
        elif token.is_stop:
            b_noise = True
        elif len(token.string) <= self.min_token_length:
            b_noise = True
        return b_noise

    def _cleanup(self, token, lower=True):
        if lower:
            token = token.lower()
        return token.strip()

    def entity_recognition(self, document):
        entities = list()
        for ent in document.ents:
            entities.append({'label': ent.label_, 'data': self._cleanup(ent.string)})
        return entities

    def generate_verb_dobj(self, document):
        verb_dobj = list([tk, tk.root.head] for tk in document.noun_chunks if tk.root.dep == dobj or tk.root.dep == pobj)
        if verb_dobj and verb_dobj.__len__() > 0:
            return json.dumps({
                'dobj': verb_dobj[0][0].text,
                'verb': verb_dobj[0][1].text
            })
