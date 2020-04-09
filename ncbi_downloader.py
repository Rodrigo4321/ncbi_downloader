#!/usr/bin/env python3

import sys
from Bio import Entrez

base_dados = sys.argv[1] #Atribuição dos parametro da linha de comandos a variáveis
search_term = sys.argv[2] 

search = Entrez.esearch(db=base_dados, term=search_term, usehistory="y") #O search é uma variável que vai publicar os resultados de uma pesquisa no histórico do servidor
search_results  = Entrez.read(search)

fetch = Entrez.efetch(db=base_dados, usehistory="y", webenv=search_results["WebEnv"], query_key=search_results["QueryKey"], rettype="fasta") #O efetch retorna registos de dados formatados para um conjunto de UIDs armazenados no histórico do servidor Entrez

sequences = fetch.read()
fetch.close()

sys.stdout.write(sequences)
sys.stdout.flush()

