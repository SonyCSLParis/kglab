# -*- coding: utf-8 -*-
"""
Generic helpers with graph building (mostly rdflib)
"""
from rdflib import Graph

def bind_ns(graph, prefix_to_ns):
    """ Binding namespaces to readable prefixes """
    for (prefix, ns) in prefix_to_ns.items():
        graph.bind(prefix, ns)
    return graph

def init_graph(prefix_to_ns):
    """ Init empty graph and bind prefixes/namespaces """
    graph = Graph()
    return bind_ns(graph=graph, prefix_to_ns=prefix_to_ns)
