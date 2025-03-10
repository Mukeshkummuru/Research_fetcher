import csv
import xml.etree.ElementTree as ET
from typing import List, Tuple, Dict
from papers_fetcher.filters import is_non_academic

def extract_authors(root: ET.Element) -> Tuple[List[str], List[str]]:
    """Extract authors and check if they are non-academic."""
    authors: List[str] = []
    company_affiliations: List[str] = []

    for author in root.findall(".//Author"):
        last_name = author.findtext("LastName") or ""
        first_name = author.findtext("ForeName") or ""
        name = f"{last_name} {first_name}".strip()
        affiliation = author.findtext("AffiliationInfo/Affiliation") or ""

        if affiliation and is_non_academic(affiliation):
            authors.append(name)
            company_affiliations.append(affiliation)

    return authors, company_affiliations

def save_to_csv(data: List[Dict[str, str]], filename: str = "papers.csv") -> None:
    """Save the extracted data to a CSV file."""
    if not data:
        print("No data to save.")
        return
    
    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
