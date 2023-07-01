from Bio import Entrez
import sys

Entrez.email = "youremail@email.com"

def Esearch(database,searchterm):
    handle = Entrez.esearch(db=database, term=searchterm,usehistory='y')
    record = Entrez.read(handle)
    return record

def History(record):
    
    querykey = record["QueryKey"]
    webenv = record["WebEnv"]
    y = querykey + "\n" + webenv
    return y
    
def Efetch(database,record):
    querykey = record["QueryKey"]
    webenv = record["WebEnv"]
    fhandle = Entrez.efetch(db=database,query_key=querykey,WebEnv=webenv,rettype = "fasta")
    sequences = fhandle.read()
    fhandle.close()
    return sequences

if __name__ == '__main__':
    record = Esearch(sys.argv[1], sys.argv[2])
    print(record)
    print(History(record))
    print(Efetch(sys.argv[1],record))