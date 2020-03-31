# ncbi_downloader
A simple script to download ncbi sequences in fasta format.

## Prerequisites
Biopython
```
pip install biopython
```
## Instructions
run with python3, with the first argument being the database and the second argument the search_term(with "" if has spaces).
###
Example:
```
python3 ncbi_downloader.py nucleotide "Psammodromus algirus[organism], cytb[gene]"
```
## Authors
* Rodrigo Gomes
* Diogo Almeida
* Bruno Pedro
