import argparse
import sys
from get-papers-list import fetch_papers, fetch_paper_details, filter_papers, save_to_csv

# Function to parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed based on a user query.")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-f", "--file", help="Output filename (CSV)", default=None)
    parser.add_argument("-d", "--debug", help="Print debug information", action="store_true")
    return parser.parse_args()

# Main function to execute the program
def main():
    args = parse_args()

    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    try:
        # Fetch papers based on the user query
        pmids = fetch_papers(args.query)
        
        if args.debug:
            print(f"PMIDs fetched: {pmids}")

        if not pmids:
            print("No papers found for the query.", file=sys.stderr)
            return

        # Fetch paper details for the retrieved PMIDs
        paper_details = fetch_paper_details(pmids)

        if args.debug:
            print(f"Paper details fetched: {paper_details}")

        if not paper_details:
            print("No paper details found for the given PMIDs.", file=sys.stderr)
            return

        # Filter papers based on non-academic authors and pharmaceutical/biotech company affiliations
        filtered_papers = filter_papers(paper_details)

        if args.debug:
            print(f"Filtered papers: {filtered_papers}")

        # Save the results to a CSV file if the filename argument is provided
        if args.file:
            save_to_csv(filtered_papers, args.file)
            print(f"Results saved to {args.file}")
        else:
            # Otherwise, print the filtered papers to the console
            for paper in filtered_papers:
                print(paper)

    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
