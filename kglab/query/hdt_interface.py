# -*- coding: utf-8 -*-
"""
Interface to query a KG - format compressed HDT
"""
import os
import fnmatch
from typing import List, Union
from hdt import HDTDocument

from kglab.query.interface import Interface

class HDTInterface(Interface):
    """
    Format of dataset = HDT, where you can do "simple" queries only, but much faster
    """
    def __init__(self, folder_hdt: str,
                 dates: Union(List[str], None) = None, default_pred: Union(List[str], None) = None,
                 nested_dataset: bool = True, filter_kb: bool = 1):
        """
        - `dataset_config`: dict, dataset config, example in `dataset-config` folder
        - `dates`: list of two strings, start and end dates of the event
        - `default_pred`: list of strings, predicates for rdf:type and dates
        - `folder_hdt`: string, path to the HDT dataset
        - `nested_dataset`: boolean, whether the dataset is chunked down in folders
        - `filter_kb`: boolean, whether to exclude some types of predicates or not
        """
        Interface.__init__(self, dates=dates,
                           default_pred=default_pred, filter_kb=filter_kb)

        if nested_dataset:
            dirs = [os.path.join(folder_hdt, file) for file in os.listdir(folder_hdt)]
            dirs = [elt for elt in dirs if not elt.split('/')[-1].startswith(".")]
            dirs = [os.path.join(old_dir, new_dir, "hdt") \
                for old_dir in dirs for new_dir in os.listdir(old_dir)]
            dirs = [elt for elt in dirs if not elt.split('/')[-2].startswith(".")]
            dirs = [elt for elt in dirs if os.path.exists(elt)]
            self.docs = [HDTDocument(file) for file in dirs]
        else:
            files = [os.path.join(folder_hdt, file) for file in os.listdir(folder_hdt) \
                        if fnmatch.fnmatch(file, "*.hdt")]
            self.docs = [HDTDocument(file) for file in files]

    def get_triples(self, **params: dict) -> list[(str, str, str)]:
        """ Querying HDT dataset """
        subject_t = params["subject"] if "subject" in params else ""
        predicate_t = params["predicate"] if "predicate" in params else ""
        object_t = params["object"] if "object" in params else ""

        triples = []
        for doc in self.docs:
            curr_triples, _ = doc.search_triples(subject_t, predicate_t, object_t)
            triples += list(curr_triples)

        return triples
