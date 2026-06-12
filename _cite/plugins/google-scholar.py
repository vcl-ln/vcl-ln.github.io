import os
import json
from urllib.request import Request, urlopen
from urllib.parse import quote
from serpapi import GoogleSearch
from util import *


@log_cache
@cache.memoize(name=__file__, expire=30 * (60 * 60 * 24))
def find_doi(title, author_first):
    """Query Crossref API to find DOI by title and first author."""
    try:
        query = quote(title)
        url = f"https://api.crossref.org/works?query.title={query}&rows=1"
        if author_first:
            url += f"&query.author={quote(author_first)}"
        request = Request(
            url=url,
            headers={"User-Agent": "VCL-LN/1.0 (mailto:visual_cognition_lab@ln.edu.hk)"},
        )
        response = json.loads(urlopen(request).read())
        items = response.get("message", {}).get("items", [])
        if items:
            doi = items[0].get("DOI", "")
            if doi:
                return f"doi:{doi}"
    except Exception:
        pass
    return None


def main(entry):
    """
    receives single list entry from google-scholar data file
    returns list of sources to cite
    """

    # get api key (serp api key to access google scholar)
    api_key = os.environ.get("GOOGLE_SCHOLAR_API_KEY", "")
    if not api_key:
        raise Exception('No "GOOGLE_SCHOLAR_API_KEY" env var')

    # serp api properties
    params = {
        "engine": "google_scholar_author",
        "api_key": api_key,
        "num": 100,  # max allowed
    }

    # get id from entry
    _id = get_safe(entry, "gsid", "")
    if not _id:
        raise Exception('No "gsid" key')

    # query api
    @log_cache
    @cache.memoize(name=__file__, expire=1 * (60 * 60 * 24))
    def query(_id):
        params["author_id"] = _id
        return get_safe(GoogleSearch(params).get_dict(), "articles", [])

    response = query(_id)

    # list of sources to return
    sources = []

    # go through response and format sources
    for work in response:
        year = get_safe(work, "year", "")
        title = get_safe(work, "title", "")
        authors = get_safe(work, "authors", "")
        author_first = authors.split(",")[0].strip() if authors else ""

        # try to find DOI via Crossref
        if title:
            doi_id = find_doi(title, author_first)
        else:
            doi_id = None

        if doi_id:
            log(f"Found DOI: {doi_id}", 3)
            # DOI found — let Manubot handle full citation details
            source = {"id": doi_id}
        else:
            # no DOI — keep Google Scholar citation data as fallback
            source = {
                "id": get_safe(work, "citation_id", ""),
                # api does not provide Manubot-citeable id, so keep citation details
                "title": title,
                "authors": (
                    list(map(str.strip, authors.split(","))) if authors else []
                ),
                "publisher": get_safe(work, "publication", ""),
                "date": (year + "-01-01") if year else "",
                "link": get_safe(work, "link", ""),
            }

        # copy fields from entry to source
        source.update(entry)

        # add source to list
        sources.append(source)

    return sources
