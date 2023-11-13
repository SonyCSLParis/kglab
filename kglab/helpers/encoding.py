# -*- coding: utf-8 -*-
"""
Encoding helpers
"""
from urllib.parse import quote

def encode(text: str) -> str:
    """ Encoding text (uris) to be readable for rdflib Graphs """
    return quote(text, safe="/:")
