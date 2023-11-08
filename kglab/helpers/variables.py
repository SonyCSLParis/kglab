# -*- coding: utf-8 -*-
"""
Variables re-used across projects
"""
from rdflib import Namespace, XSD, RDF, RDFS, OWL

# Headers
HEADERS_CSV = {"Accept": "text/csv"}
HEADERS_RDF_XML = {"Accept": "application/rdf+xml"}

# Sparql endpoints
DBPEDIA_ENDPOINT = "https://dbpedia.org/sparql"
EVENTKG_ENDPOINT = "http://eventkginterface.l3s.uni-hannover.de/sparql"

# KG prefixes
STR_DBR = "http://dbpedia.org/resource/"
STR_RDF = str(RDF)
STR_SEM = "http://semanticweb.cs.vu.nl/2009/11/sem/"
STR_XSD = str(XSD)
STR_FRAMESTER_FRAMENET_ABOX_FE = "https://w3id.org/framester/framenet/abox/fe/"
STR_FRAMESTER_FRAMENET_ABOX_GFE = "https://w3id.org/framester/framenet/abox/gfe/"
STR_FRAMESTER_ABOX_FRAME = "https://w3id.org/framester/framenet/abox/frame/"
STR_NIF = "http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#"
STR_EX = "http://example.com/"
STR_FRAMESTER_WSJ = "https://w3id.org/framester/wsj/"
STR_OBIO = "https://w3id.org/okg/obio-ontology/"
STR_EARMARK = "http://www.essepuntato.it/2008/12/earmark#"
STR_DUL = "http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#"
STR_RDFS = str(RDFS)
STR_OWL = str(OWL)

# Namespaces for KGs
NS_SEM = Namespace(STR_SEM)
NS_XSD = XSD
NS_FRAMESTER_FRAMENET_ABOX_FE = Namespace(STR_FRAMESTER_FRAMENET_ABOX_FE)
NS_FRAMESTER_FRAMENET_ABOX_GFE = Namespace(STR_FRAMESTER_FRAMENET_ABOX_GFE)
NS_FRAMESTER_ABOX_FRAME = Namespace(STR_FRAMESTER_ABOX_FRAME)
NS_NIF = Namespace(STR_NIF)
NS_EX = Namespace(STR_EX)
NS_RDF = RDF
NS_RDFS = RDFS
NS_FRAMESTER_WSJ = Namespace(STR_FRAMESTER_WSJ)
NS_OBIO = Namespace(STR_OBIO)
NS_EARMARK = Namespace(STR_EARMARK)
NS_DUL = Namespace(STR_DUL)
NS_DBR = Namespace(STR_DBR)
NS_OWL = OWL

# Ontologies prefixes
PREFIX_SEM = "sem"
PREFIX_XSD = "xsd"
PREFIX_FRAMESTER_FRAMENET_ABOX_FE = "framester-framenet-abox-fe"
PREFIX_FRAMESTER_FRAMENET_ABOX_GFE = "framester-framenet-abox-gfe"
PREFIX_FRAMESTER_ABOX_FRAME = "framester-framenet-abox-frame"
PREFIX_NIF = "nif"
PREFIX_EX = "ex"
PREFIX_RDF = "rdf"
PREFIX_FRAMESTER_WSJ = "framester-wsj"
PREFIX_OBIO = "obio"
PREFIX_EARMARK = "earmark"
PREFIX_DUL = "dul"
PREFIX_RDFS = "rdfs"
PREFIX_DBR = "dbr"
PREFIX_OWL = "owl"
