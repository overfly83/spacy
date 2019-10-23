from django.http import HttpResponse
from .spacy.SacParse import SacParse
import json


def parse(request):
    txt_to_parse = request.GET.get('txt')

    sp = SacParse('en_core_web_sm')
    doc = sp.read_document(txt_to_parse)
    ents = sp.entity_recognition(doc)
    verbs_dobj = sp.generate_verb_dobj(doc)
    ents_json = None
    verbs_dobj_json = None
    if ents:
        ents_json = list(ents)
    if verbs_dobj:
        verbs_dobj_json = json.loads(verbs_dobj)
    response = json.dumps({'ents': ents_json, 'verbs_dobj': verbs_dobj_json})
    # print(response)

    # print(json.load(verbs_dobj))
    return HttpResponse(response)
