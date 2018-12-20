from django.http import HttpResponse
import en_core_web_lg
nlp = en_core_web_lg.load()


def parse(request):
    txt_to_parse = request.GET.get('txt')
    doc = nlp(txt_to_parse)
    print(doc.ents)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_, '-----!!!!!!!!!')
    print(doc, "---test")
    return HttpResponse(doc)
