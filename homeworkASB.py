from Bio import Entrez
import sys

# Set the email address to use for Entrez queries
Entrez.email = "your.email@example.com"

search_term = sys.argv[1]
database = sys.argv[2]

# Define search function
def Esearch(search_term,database):
    handle = Entrez.esearch(db=database, term=search_term, usehistory='y')
    record = Entrez.read(handle)
    print(record)
    return record


record = Esearch(search_term,database)
query_key = record['QueryKey']
webenv = record['WebEnv']



#Show the WebEnv and QueryKey of the History
def History(record):

    print(record["QueryKey"])
    print(record["WebEnv"])

History(record)


 #Use Entrez efetch to fetch the sequences
def Efetch(query_key,webenv,database):

    fhandle = Entrez.efetch(db=database,query_key=query_key,WebEnv=webenv,rettype='fasta')
    sequences = fhandle.read()
    fhandle.close()
    print(sequences)

Efetch(query_key,webenv,database)