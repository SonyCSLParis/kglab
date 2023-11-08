# -*- coding: utf-8 -*-
"""
Helpers related to KG queries
"""
import io
import requests
import pandas as pd
from helpers.variables import PREFIX_RDFS, STR_RDFS, HEADERS_CSV

def run_query(query: str, sparql_endpoint: str, headers: dict) -> pd.DataFrame:
    """ Using curl requests to run query from sparql endpoint"""
    response = requests.get(
        sparql_endpoint, headers=headers,
        params={"query": query}, timeout=3600)
    if "csv" in headers["Accept"]:
        return pd.read_csv(io.StringIO(response.content.decode('utf-8')))
    return response

def write_values_sparql(list_str: list[str], var: str):
    """ Convert a list of strings into `VALUES ?var {x1 x2 ...}`"""
    return f"VALUES ?{var} " + \
        "{" + ' '.join([f"<{x}>" for x in list_str]) + "}"

def get_labels(list_str: list[str], sparql_endpoint: str,
               filter_lang="") -> pd.DataFrame:
    """ Get rdfs:label of a list of predicate """
    sparql_filter_lang = f'FILTER(LANG(?label) = "{filter_lang}") .' if filter_lang else ""
    start, end = "{", "}"
    query = f"""
    PREFIX {PREFIX_RDFS}: <{STR_RDFS}>
    SELECT ?predicate ?label WHERE {start}
    ?predicate {PREFIX_RDFS}:label ?label .
    {sparql_filter_lang}
    {write_values_sparql(list_str=list_str, var="predicate")}
    {end}
    """
    return run_query(query=query, sparql_endpoint=sparql_endpoint, headers=HEADERS_CSV)

def get_outgoing(list_str: list[str], sparql_endpoint: str):
    """ Retrieve outgoing links of a list of subjects """
    start, end = "{", "}"
    query = f"""
    SELECT ?subject ?predicate ?object WHERE {start}
        ?subject ?predicate ?object .
        {write_values_sparql(list_str=list_str, var="subject")}
    {end}
    """
    return run_query(query=query, sparql_endpoint=sparql_endpoint, headers=HEADERS_CSV)
