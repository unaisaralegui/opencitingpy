"""Client for making requests to the Open Citations API"""

import requests

from .classes import Citation, Metadata

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

    def __parse_citation_data(self, data):
        parsed_data = [Citation(d) for d in data]
        return parsed_data

    def __parse_counts(self, data):
        if len(data):
            counts = int(data[0]['count'])
        else:
            counts = 0
        return counts


    def get_references(self, doi, parse_data=True, **kwargs):
        """
        This operation retrieves the citation data for all the outgoing references to other
        cited works appearing in the reference list of the bibliographic entity identified by the input DOI.

        :param doi: A valid Digital Object Identifier (DOI) e.g. '10.3390/s19020353'
        :type doi: str
        :param parse_data: (Default True) Whether to parse data with opencitingpy.classes.Citation
        :type parse_data: bool
        :param kwargs:
        :return:
        """
        operation = 'references'
        data = self.__get_data(operation, doi)
        if parse_data:
            data = self.__parse_citation_data(data)
        return data

    def get_citation(self, oci, parse_data=True, **kwargs):
        """
        This operation retrieves the citation metadata for the citation identified by
        the input Open Citation Identifier (OCI). The Open Citation Identifier is a globally unique persistent
        identifier for bibliographic citations, which has a simple structure: the lower-case letters "oci" followed
        by a colon, followed by two numbers separated by a dash (XXXXXX-YYYYYY)

        :param oci: Open Citation Identifier (OCI)
        :type oci: str
        :param parse_data: (Default True) Whether to parse data with opencitingpy.classes.Citation
        :type parse_data: bool
        :param kwargs:
        :return:
        """
        operation = 'citation'
        data = self.__get_data(operation, oci)
        if parse_data:
            data = self.__parse_citation_data(data)
        return data

    def get_citations(self, doi, parse_data=True, **kwargs):
        """
        This operation retrieves the citation data for all the references appearing in the reference lists of other
        citing works to the bibliographic entity identified by the input DOI, that constitute the incoming citations
        of that identified bibliographic entity.

        :param doi: A valid Digital Object Identifier (DOI) e.g. '10.3390/s19020353'
        :type doi: str
        :param parse_data: (Default True) Whether to parse data with opencitingpy.classes.Citation
        :type parse_data: bool
        :param kwargs:
        :return:
        """
        operation = 'citations'
        data = self.__get_data(operation, doi)
        if parse_data:
            data = self.__parse_citation_data(data)
        return data

    def get_metadata(self, dois, parse_data=True, **kwargs):
        """
        This operation retrieves the bibliographic metadata for each of the bibliographic
        entities identified by one or more input DOIs.

        :param dois: A list of Digital Object Identifierers (DOIs) e.g. ['10.3390/s19020353', '10.3390/s19143113']
        :type dois: list
        :param parse_data: (Default True) Whether to parse data with opencitingpy.classes.Metadata
        :type parse_data: bool
        :param kwargs:
        :return:
        """
        operation = 'metadata'
        # dois should be a list
        if isinstance(dois, str):
            dois = [dois]
        dois = '__'.join(dois)
        data = self.__get_data(operation, dois)
        if parse_data:
            data = [Metadata(d) for d in data]
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
        counts = self.__parse_counts(data)
        return counts

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
        counts = self.__parse_counts(data)
        return counts
