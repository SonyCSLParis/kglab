# -*- coding: utf-8 -*-
"""
Generic helpers with graphs (mostly rdf_ones)
"""
from rdflib import Graph

def get_intersection_difference(g1: Graph, g2: Graph) -> (list[tuple], Graph, Graph):
    """ returns (intersection, g1-g2, g2-g1) """
    intersection = []
    smaller = g1 if len(g1) < len(g2) else g2
    bigger = g2 if len(g1) < len(g2) else g1
    for triple in smaller:
        if triple in bigger:
            intersection.append(triple)
    return intersection, g1-g2, g2-g1
