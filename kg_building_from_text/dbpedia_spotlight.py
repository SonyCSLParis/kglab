# -*- coding: utf-8 -*-
"""
DBpedia Spotlight
To download locally, follow instructions in:
https://github.com/MartinoMensio/spacy-dbpedia-spotlight

Make sure that Spotlight is running locally
1. Go to spotlight folder
2. Run

```bash
java -Xmx8G -jar rest-1.1-jar-with-dependencies.jar en http://localhost:2222/rest
```

Download spacy
Load `en_core_web_sm` model using:

```bash
python -m spacy download en_core_web_sm
```
"""
import spacy

def init_spacy_pipeline(spotlight=True):
    """ Init spacy pipeline with additional components """
    nlp = spacy.load("en_core_web_sm")
    if spotlight:
        # nlp.add_pipe(
        #     "dbpedia_spotlight",
        #     config={'confidence': 0.7, 'dbpedia_rest_endpoint': 'http://localhost:2222/rest'})
        nlp.add_pipe(
            "dbpedia_spotlight",
            config={'confidence': 0.7})
    return nlp

def ent_to_uri(ent: spacy.tokens.Span) -> str:
    """ From entity return DBpedia URI """
    return ent._.dbpedia_raw_result["@URI"]

def get_db_entities(doc: spacy.tokens.doc.Doc) -> list[str]:
    """ Return URIs of entities (if applicable) """
    db_entities = [ent._.dbpedia_raw_result for ent in doc.ents if ent._.dbpedia_raw_result]
    return [ent['@URI'] for ent in db_entities]
