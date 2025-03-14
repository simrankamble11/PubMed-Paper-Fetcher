This Python script allows users to fetch research papers from PubMed based on a user-specified search query. It retrieves the papers, extracts the relevant details, filters the results for non-academic authors and pharmaceutical/biotech affiliations, and saves the results to a CSV file or prints them to the console.

How the Code is Organized
1.	main.py: This is the main entry point of the script. It accepts user input, fetches the relevant research papers from PubMed, filters them, and saves them to a CSV file or prints them to the console.

2.	pubmed_fetcher.py: This file contains functions that interact with the PubMed API to fetch paper details based on a search query.
   
   o	fetch_papers(query): Fetches paper IDs based on a search query.

   o	fetch_paper_details(pmids): Fetches detailed information for a list of PubMed IDs (PMIDs).

   o	filter_papers(paper_details): Filters papers based on non-academic authors and pharmaceutical/biotech company affiliations.

3.	save_to_csv(paper_details, filename): This function saves the filtered paper details to a CSV file.

Dependencies

•	requests: For making HTTP requests to the PubMed API. 

•	csv: For writing the results to a CSV file.

•	argparse: For parsing command-line arguments.

To Install Dependencies:
You can install the required dependencies using pip:

          pip install requests

 Instructions to Run the Program
1.	Clone this repository (or download the files) to your local machine.
2.	Install dependencies:
o	Run pip install requests to install the necessary Python libraries.
3.	Run the script:

o	To fetch papers based on a search query and save them to a CSV file:

          python main.py "search query" -f output.csv
                                      
o	To fetch papers based on a search query and print the results to the console:

          python main.py "search query"
                                                
o	To enable debug mode (to see the intermediate steps):

          python main.py "search query" -f output.csv -d


4.	Replace "search query" with the desired research topic (e.g., "pharmaceutical biotech", "artificial intelligence in healthcare", etc.).

Command-Line Arguments

•	query (required): The search query that will be used to search PubMed.

•	-f, --file (optional): The output filename (CSV) where the results will be saved. If not provided, the results will be printed to the console.

•	-d, --debug (optional): If this flag is provided, the program will print debug information during execution, which can help you understand the intermediate steps.

Example Usage

Fetch Papers and Save to CSV

python main.py "pharmaceutical biotech" -f output.csv

This will search for papers related to "pharmaceutical biotech" on PubMed and save the filtered results to output.csv.

Fetch Papers and Print to Console

      python main.py "cancer treatment"

This will search for papers related to "cancer treatment" and print the filtered results to the console.

Fetch Papers with Debug Information

    python main.py "artificial intelligence in healthcare" -f results.csv -d

This will search for papers related to "artificial intelligence in healthcare", print debug information, and save the filtered results to results.csv.

Tools and Libraries Used

•	PubMed API: The script interacts with the PubMed API to fetch research papers and their details.

o	PubMed E-utilities Documentation

•	requests Library: Used to make HTTP requests to fetch data from the PubMed API.

o	requests Documentation

•	argparse Library: Used to parse command-line arguments.

o	argparse Documentation

•	csv Library: Used to write the results into a CSV file.









