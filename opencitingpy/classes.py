"""Classes for different response types from the OpenCitations API"""


def parse_lists_from_api(list_string, separator=';'):
    """
    Parse list of items returned by the OpenCitations API
    :param list_string: list of dois separated by sep
    :type list_string: str
    :param separator: (Default ';') separator to separate elements in string
    :type separator: str
    :return: items in the string as a list
    :rtype: list
    """
    if list_string is None:
        return None
    items = [item.strip() for item in list_string.split(separator)]
    return items


class Citation:
    """
    Custom class for citation type objects, this includes results from more than one
    OpenCitations API: references, citations, citation

    :param data: The dictionary (json) with the information for each item returned by the OpenCitations API
    :type data: dict
    """

    def __init__(self, data: dict):
        self.oci = data.get('oci', None)
        self.citing = data.get('citing', None)
        self.cited = data.get('cited', None)
        self.creation = data.get('creation', None)
        self.timespan = data.get('timespan', None)
        self.journal_sc = data.get('journal_sc', None)
        self.author_sc = data.get('author_sc', None)
        self.data = data

    def __str__(self):
        return str(self.data)


class Metadata:
    """
    Custom class for Metadata type objects.

    :param data: The dictionary (json) with the information for each item returned by the OpenCitations API
    :type data: dict
    """

    def __init__(self, data: dict):
        self.author = parse_lists_from_api(data.get('author', None))
        self.year = data.get('year', None)
        self.title = data.get('title', None)
        self.source_title = data.get('source_title', None)
        self.source_id = data.get('source_id', None)
        self.volume = data.get('volume', None)
        self.issue = data.get('issue', None)
        self.page = data.get('page', None)
        self.doi = data.get('doi', None)
        self.reference = parse_lists_from_api(data.get('reference', None))
        self.citation = parse_lists_from_api(data.get('citation', None))
        self.citation_count = data.get('citation_count', None)
        self.oa_link = data.get('oa_link', None)
        self.data = data

    def __str__(self):
        d = dict(self.data)
        d['author'] = self.author
        d['reference'] = self.reference
        d['citation'] = self.citation
        return str(d)
