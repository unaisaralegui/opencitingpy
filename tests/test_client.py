import unittest

import opencitingpy.client


dois = ['10.3390/s19020353', '10.3390/s19143113']
doi = '10.3390/s19020353'
citing_documents = 23
oci = '0200303090036280109000200030503-020010001063619371025142314271634370200010337000602'


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = opencitingpy.client.Client()

    def test_get_references(self):
        data = self.client.get_references(doi=doi)
        self.assertEqual(len(data), citing_documents)

    def test_get_citation(self):
        data = self.client.get_citation(oci=oci)
        citing = 'coci => 10.3390/s19020353'
        cited = 'coci => 10.1016/j.apenergy.2013.10.062'
        self.assertEqual(data[0].cited, cited)
        self.assertEqual(data[0].citing, citing)

    def test_get_citations(self):
        data = self.client.get_citations(doi=doi)
        self.assertGreater(len(data), 0)

    def test_get_metadata(self):
        data = self.client.get_metadata(dois=dois) 
        self.assertEqual(len(data), len(dois))

    def test_get_citation_count(self):
        data = self.client.get_citation_count(doi=doi)
        self.assertGreater(data, 0)

    def test_get_reference_count(self):
        data = self.client.get_reference_count(doi=doi)
        self.assertEqual(data, citing_documents)


if __name__ == '__main__':
    unittest.main()
