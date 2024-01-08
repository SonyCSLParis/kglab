# -*- coding: utf-8 -*-
"""
Interface to query the data 
Generic interface that cannot be used alone
Classes that will inherit that class (eg HDT, SPARQL)
"""
from typing import List, Union, Dict
import pandas as pd
from pandas.core.frame import DataFrame


class Interface:
    """ Querying the KG """
    def __init__(self,
                 dates: Union(List[str], None) = None, default_pred: Union(List[str], None) = None,
                 filter_kb: bool = 1):
        self.pred = default_pred if default_pred else []

        dates = dates if dates else [None, None]
        self.start_date = dates[0]
        self.end_date = dates[1]
        self.filter_kb = filter_kb

    def get_triples(self, **params: Dict) -> list:
        """ Will be inherited by subclassses """
        return []

    def get_superclass(self, node: str, sub_class_of: str, owl_thing: str) -> str:
        """ Superclass of a node
        Most ancient ancestor before owl:Thing """
        triples = self.get_outgoing(node=node)
        triples = self.filter_node(triples=triples, vals={"node": [sub_class_of]},
                                   in_f=True, subject_f=False, object_f=False)

        if not triples:
            return node
        if str(triples[0][2]) == owl_thing:
            return node
        return self.get_superclass(str(triples[0][2]), sub_class_of=sub_class_of,
                                   owl_thing=owl_thing)

    def filter_namespace(self, triples: list[(str, str, str)], vals: Dict, in_f: bool = True,
                         subject_f: bool = True, predicate_f: bool = True, object_f: bool = True):
        """ Filters nodes that start with a regexed value
        - in_f: filtering in (=keeping)
        - out_f: filtering out (=removing)
        - subject, predicate, object: filtering on which part of the triple """

        def f_namespace(x: str , vals: Dict, in_f: bool = True):
            if in_f:
                return x.startswith(vals["namespace"])
            return not x.startswith(vals["namespace"])

        return self.filter(triples, f_namespace, vals, in_f, subject_f, predicate_f, object_f)

    def get_outgoing(self, node: str) \
        -> list[(str, str, str)]:
        """ Return all triples (s, p, o) s.t. s = node """
        params = {"subject": node}
        return self.get_triples(**params)

    def get_ingoing(self, node: str) \
        -> list[(str, str, str)]:
        """ Return all triples (s, p, o) s.t. o = node """
        params = {"object": node}
        return self.get_triples(**params)

    def filter_node(self, triples: list[(str, str, str)], vals: Dict, in_f: bool = True,
                         subject_f: bool = True, predicate_f: bool = True, object_f: bool = True):
        """ Filters nodes that start with a regexed value
        - in_f: filtering in (=keeping)
        - out_f: filtering out (=removing)
        - subject, predicate, object: filtering on which part of the triple """

        def f_node(x: str, vals: Dict, in_f: bool = True):
            if in_f:
                return x in vals["node"]
            return x not in vals["node"]

        return self.filter(triples, f_node, vals, in_f, subject_f, predicate_f, object_f)

    def filter(self, triples: list[(str, str, str)], f_function, vals: Dict, in_f: bool = True,
               subject_f: bool = True, predicate_f: bool = True, object_f: bool = True):
        """ Filter in/out from filter function f_function. Designed to be as generic as possible.
        f_function should have three arguments:
        - x (the value to filter or not)
        - vals: any necessary key-value for the function
        - in_f: boolean (filter in, eg keep, or filter out, eg discard) """
        if subject_f:
            triples = [elt for elt in triples if f_function(x=elt[0], vals=vals, in_f=in_f)]
        if predicate_f:
            triples = [elt for elt in triples if f_function(x=elt[1], vals=vals, in_f=in_f)]
        if object_f:
            triples = [elt for elt in triples if f_function(x=elt[2], vals=vals, in_f=in_f)]
        return triples

    @staticmethod
    def _get_df(list_triples: list[tuple], type_df: str) -> DataFrame:
        """ Transform into df """
        return pd.DataFrame({"subject": [str(row[0]) for row in list_triples],
                             "predicate": [str(row[1]) for row in list_triples],
                             "object": [str(row[2]) for row in list_triples],
                             "type_df": [type_df] * len(list_triples)}).drop_duplicates()
