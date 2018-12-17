import en_core_web_sm

nlp = en_core_web_sm.load()
doc = nlp(u'lock the actual data in year 2016.')

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)