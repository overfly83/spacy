from django.http import HttpResponse
import en_core_web_sm
nlp = en_core_web_sm.load()
doc = nlp(u'This is a sentence.')

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)

def index(request):
    print(request)
    return HttpResponse(doc)
