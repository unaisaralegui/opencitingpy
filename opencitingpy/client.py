"""Client for making requests to the Open Citations API"""

import requests

API_URL = 'https://w3id.org/oc/index/api/v1'


class Client:
    """
    A client to make requests to the Open Citations API
    """

    def __init__(self, api_url=None):
        self.api_url = api_url if api_url is not None else API_URL

    def __construct_url(self, operation, document_identifier, **kwargs):
        uri = f'{self.api_url}/{operation}/{document_identifier}'
        return uri

    @staticmethod
    def __make_request(uri):
        request = requests.get(uri)
        data = request.json()
        return data

    def __get_data(self, operation, document_identifier, **kwargs):
        uri = self.__construct_url(operation, document_identifier, **kwargs)
        data = self.__make_request(uri)
        return data

    def get_references(self, doi, **kwargs):
        """
        This operation retrieves the citation data for all the outgoing references to other
        cited works appearing in the reference list of the bibliographic entity identified by the input DOI.

        :param doi: A valid Digital Object Identifier (DOI) e.g. '10.3390/s19020353'
        :type doi: str
        :param kwargs:
        :return:
        """
        operation = 'references'
        data = self.__get_data(operation, doi)
        return data

    def get_citation(self, oci, **kwargs):
        """
        This operation retrieves the citation metadata for the citation identified by
        the input Open Citation Identifier (OCI).

        :param oci:
        :param kwargs:
        :return:
        """
        operation = 'citation'
        data = self.__get_data(operation, oci)
        return data

    def get_citations(self, doi, **kwargs):
        """
        This operation retrieves the citation data for all the references appearing in the reference lists of other
        citing works to the bibliographic entity identified by the input DOI, that constitute the incoming citations
        of that identified bibliographic entity.

        :param doi: A valid Digital Object Identifier (DOI) e.g. '10.3390/s19020353'
        :type doi: str
        :param kwargs:
        :return:
        """
        operation = 'citations'
        data = self.__get_data(operation, doi)
        return data

    def get_metadata(self, dois, **kwargs):
        """
        This operation retrieves the bibliographic metadata for each of the bibliographic
        entities identified by one or more input DOIs.

        :param dois: A list of Digital Object Identifierers (DOIs) e.g. ['10.3390/s19020353', '10.3390/s19143113']
        :type dois: list
        :param kwargs:
        :return:
        """
        operation = 'metadata'
        # dois should be a list
        if isinstance(dois, str):
            dois = [dois]
        dois = '__'.join(dois)
        data = self.__get_data(operation, dois)
        return data

    def get_citation_count(self, doi, **kwargs):
        """
        This operation retrieves the number of incoming citations to the
        bibliographic entity identified by the input DOI.

        :param doi: A valid Digital Object Identifier (DOI) e.g. '10.3390/s19020353'
        :type doi: str
        :param kwargs:
        :return:
        """
        operation = 'citation-count'
        data = self.__get_data(operation, doi)
        return data

    def get_reference_count(self, doi, **kwargs):
        """
        This operation retrieves the number of outgoing citations from the bibliographic
        entity identified by the input DOI.

        :param doi: A valid Digital Object Identifier (DOI) e.g. '10.3390/s19020353'
        :type doi: str
        :param kwargs:
        :return:
        """
        operation = 'reference-count'
        data = self.__get_data(operation, doi)
        return data
