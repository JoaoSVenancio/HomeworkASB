# Homework ASB

## Entrez Sequence Retrieval

This script utilizes the Biopython library to search and retrieve sequences from the <a target="_balnk" href="https://www.ncbi.nlm.nih.gov">NCBI</a> Entrez database.
It provides functions to perform a search in a specified Entrez database, retrieve search history information, and fetch sequences in FASTA format.

### Installation (Windows)

1. Make sure you have Python installed on your system. You can download it from the official <a target="_blank" href="https://www.python.org/downloads/">Python website</a>.
2. Install the Biopython library using `pip`:
```
pip install biopyhton
```
Clone this repository or download the homeworkASB.py file.

### Installation (Linux)

1. Make sure you have Python installed on your system. You can check if it's already installed by running the following command in your terminal:
```
python --version
```
If Pyhton is not installed, you can install it by running the following commands:
```
sudo apt update
sudo apt install python3
```
Install the Biopython library using `pip`:
```
pip install biopython
```
If you don´t have pip installed, you can install it by running the following command:
```
sudo apt install python3-pip
```
Clone this repository or download the homeworkASB.py file.

### Usage (Windows)

Import the necessary libraries
```
from Bio import Entrez
import sys
```
Set your email address for Entrez queries:
```
Entrez.email = "your_email@example.com"
```
Run the script from the command line, providing the necessary arguments:
```
python homeworkASB.py "database" "searchterm"
```
Replace the `database` with the name of the Entrez databse you want to search (e.g., **nucleotide**, **protein**) and `searchterm` with your desired search term.

The script will perform the search, print the search record, extract and print the search history information, and fetch the sequences matching the search term. The retrieved sequences will be printed to the console in FASTA format.

### Usage (Linux)

Open a terminal and navigate to the directory where the **homeworkASB.py** file is located.
Set your email address for Entrez queries. Open the script in a text editor and replace `your_email@example.com` with your own email address:
```
Entrez.email = "your_email@example.com"
```
Run the script by executing the following command in your terminal:
```
python3 homeworkASB.py "database" "searchterm"
```
Replace `database` with the name of the Entrez database you want to search (e.g., **nucleotide**, **protein**) and `searchterm` with your desired search term.

The script will perform the search and retrieve the sequences matching your search term from the specified Entrez database. The search record, search history information, and the fetched sequences will be printed to the terminal.

### Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

