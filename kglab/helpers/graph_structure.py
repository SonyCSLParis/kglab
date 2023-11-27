# -*- coding: utf-8 -*-
"""
Generic helpers with graphs (mostly rdf_ones)
"""
from rdflib import Graph
from urllib.parse import unquote

def get_unquoted_triples(graph):
    res = []
    for subject, predicate, obj in graph:
        res.append((unquote(str(subject)), unquote(str(predicate)), unquote(str(obj))))
    return res

def get_intersection_difference(g1: Graph, g2: Graph) -> (list[tuple], Graph, Graph):
    """ returns (intersection, g1-g2, g2-g1) """
    g1 = get_unquoted_triples(graph=g1)
    g2 = get_unquoted_triples(graph=g2)

    intersection = []
    smaller = g1 if len(g1) < len(g2) else g2
    bigger = g2 if len(g1) < len(g2) else g1

    for triple in smaller:
        if triple in bigger:
            intersection.append(triple)
    return intersection, [x for x in g1 if x not in g2], [x for x in g2 if x not in g1]