# -*- coding: utf-8 -*-
"""
Data loading of various files
"""
import json
import pandas as pd
from rdflib import Graph

def open_json(path: str) -> dict:
    """ Json+encoding utf-8 """
    with open(path, encoding="utf-8") as openfile:
        data = json.load(openfile)
    return data

def read_csv(path: str) -> pd.DataFrame:
    """ Opening pandas, removing "Unnamed: 0" column """
    df = pd.read_csv(path)
    df = df[[col for col in df.columns if "Unnamed: 0" not in col]]
    return df

def parse_graph(path: str) -> Graph:
    """ Parsing .ttl file """
    graph = Graph()
    graph.parse(path)
    return graph
