#!/usr/bin/env python3

import sys
from Bio import Entrez

base_dados = sys.argv[1]
search_term = sys.argv[2]


file = open("sequences.fasta", "w")
sys.stdout = file

search = Entrez.esearch(db=base_dados, term=search_term, usehistory="y")
search_results  = Entrez.read(search)

fetch = Entrez.efetch(db=base_dados, usehistory="y", webenv=search_results["WebEnv"], query_key=search_results["QueryKey"], rettype="fasta")

sequences = fetch.read()

fetch.close()

file.write(sequences)
