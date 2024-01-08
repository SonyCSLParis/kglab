"""
#TO DO: add documentation on this script
"""
from typing import Union, List
import urllib.request
from urllib.parse import quote_plus
from pandas.core.frame import DataFrame
from SPARQLWrapper import SPARQLWrapper, RDFXML
from kglab.query.interface import Interface

class SPARQLQuery:
    """
    Creating SPARQL queries based on templates + params
    """
    def __init__(self):
        self.query_template = self._set_query_template()

    def _set_query_template(self) -> str:
        query = """
        CONSTRUCT {
            ?s ?p ?o .
        }
        WHERE {
        <VALUES-unique-subject>
        <VALUES-unique-predicate>
        <VALUES-unique-object>
        ?s ?p ?o .
            }
        """
        return query

    def __call__(self, params: dict[str, str]) -> str:
        query = self.query_template
        for name, abbr in [("subject", "s"), ("predicate", "p"), ("object", "o")]:
            if name in params and params[name]:
                query = query.replace(
                    f"<VALUES-unique-{name}>",
                    "VALUES ?" + abbr + " { <" + quote_plus(params[name], safe='/:') + "> } "
                )
            else:
                query = query.replace(f"<VALUES-unique-{name}>", "")
        return query


class SPARQLInterface(Interface):
    """
    #TO DO: add documentation on this script
    """
    def __init__(self, agent: str,
                 dates: Union(List[str], None) = None, default_pred: Union(List[str], None) = None,
                 filter_kb: bool = 1, sparql_endpoint: str = "http://dbpedia.org/sparql"):
        Interface.__init__(self, dates=dates,
                           default_pred=default_pred, filter_kb=filter_kb)
        self.sparql = SPARQLWrapper(sparql_endpoint, agent=agent)
        self.sparql_query = SPARQLQuery()

    def get_triples(self, **params: dict[str, str]) -> list[(str, str, str)]:
        query = self.sparql_query(params=params)
        return self.call_endpoint(query=query)

    def call_endpoint(self, query: str) -> DataFrame:
        """ Querying KG through SPARQL endpoint """
        proxy_support = urllib.request.ProxyHandler({})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        self.sparql.setReturnFormat(RDFXML)
        self.sparql.setQuery(query)
        # self.sparql.setMethod(POST)
        try:
            results = self.sparql.query().convert()
            return [(str(triple[0]), str(triple[1]), str(triple[2])) \
                for triple in list(set(results))]
        except:
            return []
