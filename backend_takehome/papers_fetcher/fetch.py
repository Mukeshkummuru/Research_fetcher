import requests
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional, Tuple
from papers_fetcher.utils import extract_authors

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_papers(query: str) -> List[Dict[str, str]]:
    """Fetch papers from PubMed API."""
    params: Dict[str, str] = {
        "db": "pubmed",
        "term": query,
        "retmode": "xml",
        "retmax": "10"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        raise Exception("Failed to fetch papers")

    root = ET.fromstring(response.content)
    ids: List[str] = [id_elem.text for id_elem in root.findall(".//Id") if id_elem.text]

    papers: List[Dict[str, str]] = []
    for paper_id in ids:
        paper_data = fetch_paper_details(paper_id)
        if paper_data:
            papers.append(paper_data)
    
    return papers

def fetch_paper_details(pubmed_id: str) -> Optional[Dict[str, str]]:
    """Fetch details of a single paper."""
    params: Dict[str, str] = {
        "db": "pubmed",
        "id": pubmed_id,
        "retmode": "xml"
    }
    response = requests.get(DETAILS_URL, params=params)
    if response.status_code != 200:
        return None

    root = ET.fromstring(response.content)
    title: Optional[str] = root.findtext(".//ArticleTitle")
    pub_date: Optional[str] = root.findtext(".//PubDate/Year")
    authors, company_affiliations = extract_authors(root)

    return {
        "PubmedID": pubmed_id,
        "Title": title or "Unknown",
        "Publication Date": pub_date or "Unknown",
        "Non-academic Author(s)": ", ".join(authors),
        "Company Affiliation(s)": ", ".join(company_affiliations)
    }
