from Bio import Entrez
import sys

# Set your email address for Entrez queries
Entrez.email = "youremail@email.com"

def Search_databases(database,searchterm):
    # Perform the search in the specified database with the search term
    handle = Entrez.esearch(db=database, term=searchterm,usehistory='y')
    record = Entrez.read(handle)
    return record

def History(record):
    # Extract the QueryKey and WebEnv from the search record
    querykey = record["QueryKey"]
    webenv = record["WebEnv"]
    # Concatenate the QueryKey and WebEnv as a string
    history_info = querykey + "\n" + webenv
    return history_info
    
def Fetch_sequences(database,record):
    # Retrieve the sequences using the QueryKey and WebEnv
    querykey = record["QueryKey"]
    webenv = record["WebEnv"]
    fhandle = Entrez.efetch(db=database,query_key=querykey,WebEnv=webenv,rettype = "fasta")
    sequences = fhandle.read()
    fhandle.close()
    return sequences

if __name__ == '__main__':
    # Perform the search using the arguments provided in the command line
    record = Search_databases(sys.argv[1], sys.argv[2])
    # Print the search record
    print(record)
    # Extract and print the search history information
    print(History(record))
    # Fetch the sequences and print the result
    print(Fetch_sequences(sys.argv[1],record))
