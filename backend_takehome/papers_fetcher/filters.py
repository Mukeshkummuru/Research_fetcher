def is_non_academic(affiliation: str) -> bool:
    """Determine if the affiliation is non-academic."""
    academic_keywords = ["university", "college", "institute", "lab", "hospital"]
    return not any(word.lower() in affiliation.lower() for word in academic_keywords)
