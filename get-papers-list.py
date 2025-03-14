import requests
import csv
from typing import List, Dict

# Function to fetch PubMed paper IDs based on a query
def fetch_papers(query: str) -> List[str]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "xml",
        "retmax": "100"  # Limiting to 100 results for now
    }
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    
    # Parse the response to get PMIDs (PubMed IDs)
    pmids = []
    if response.status_code == 200:
        # Parse XML to extract PMIDs
        from xml.etree import ElementTree
        tree = ElementTree.ElementTree(ElementTree.fromstring(response.text))
        root = tree.getroot()
        for id_tag in root.findall(".//Id"):
            pmids.append(id_tag.text)
    
    return pmids

# Function to fetch paper details from PubMed using PMIDs
def fetch_paper_details(pmids: List[str]) -> List[Dict[str, str]]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    paper_details = []
    
    for pmid in pmids:
        params = {
            "db": "pubmed",
            "id": pmid,
            "retmode": "xml"
        }
        
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        # Parse the response to get paper details
        if response.status_code == 200:
            from xml.etree import ElementTree
            tree = ElementTree.ElementTree(ElementTree.fromstring(response.text))
            root = tree.getroot()
            
            docsum = root.find(".//DocSum")
            paper_data = {}
            if docsum is not None:
                for item in docsum.findall(".//Item"):
                    name = item.attrib.get('Name')
                    if name == "Title":
                        paper_data["Title"] = item.text
                    elif name == "Source":
                        paper_data["Journal"] = item.text
                    elif name == "PubDate":
                        paper_data["PubDate"] = item.text
                    elif name == "AuthorList":
                        authors = item.text.split(", ")
                        paper_data["Authors"] = authors
                    elif name == "CorrespondingAuthor":
                        paper_data["Corresponding Author Email"] = item.text
                paper_data["PubmedID"] = pmid
                paper_details.append(paper_data)
    
    return paper_details

# Function to filter papers based on non-academic authors and pharmaceutical/biotech company affiliations
def filter_papers(paper_details: List[Dict[str, str]]) -> List[Dict[str, str]]:
    pharmaceutical_keywords = ["pharma", "biotech", "company", "inc", "corporation"]
    filtered_papers = []
    
    for paper in paper_details:
        non_academic_authors = []
        company_affiliations = []
        
        # Identify non-academic authors and companies
        for author in paper["Authors"]:
            if any(keyword in author.lower() for keyword in pharmaceutical_keywords):
                company_affiliations.append(author)
            elif "@" in author:  # Simple heuristic for non-academic authors: presence of "@" (email)
                non_academic_authors.append(author)
        
        if company_affiliations:
            paper["Non-academic Author(s)"] = ", ".join(non_academic_authors)
            paper["Company Affiliation(s)"] = ", ".join(company_affiliations)
            filtered_papers.append(paper)
    
    return filtered_papers

# Function to save the results to a CSV file
def save_to_csv(paper_details: List[Dict[str, str]], filename: str):
    print(f"Saving results to {filename}...")
    fieldnames = ["PubmedID", "Title", "PubDate", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email","Authors", "Journal"]
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(paper_details)
