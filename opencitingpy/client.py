"""Client for making requests to the Open Citations API"""

import requests

API_URL = 'https://w3id.org/oc/index/api/v1'


class Client:
    """
    A client to make requests to the Open Citations API
    """

    def __init__(self, api_url=None):
        self.api_url = api_url if api_url is not None else API_URL

    def get_references(self, doi, **kwargs):
        raise NotImplementedError("Not available")

    def get_citation(self, oci, **kwargs):
        raise NotImplementedError("Not available")

    def get_citations(self, doi, **kwargs):
        raise NotImplementedError("Not available")

    def get_metadata(self, dois, **kwargs):
        raise NotImplementedError("Not available")

    def get_citation_count(self, doi, **kwargs):
        raise NotImplementedError("Not available")

    def get_reference_count(self, doi, **kwargs):
        raise NotImplementedError("Not available")
