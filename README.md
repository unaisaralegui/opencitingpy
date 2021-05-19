# opencitingpy

A python implementation to obtain data from [OpenCitations](https://opencitations.net/) API.

Easily access the OpenCitations API from python, without having to bother about remembering the urls to call
or formatting the data received from the API.

Access all the API endpoints available in OpenCitations to date:

* [/references/{doi}](https://opencitations.net/index/api/v1#/references/{doi})
* [/citations/{doi}](https://opencitations.net/index/api/v1#/citations/{doi})
* [/citation/{oci}](https://opencitations.net/index/api/v1#/citation/{oci})
* [/metadata/{dois}](https://opencitations.net/index/api/v1#/metadata/{dois})
* [/citation-count/{doi}](https://opencitations.net/index/api/v1#/citation-count/{doi})
* [/reference-count/{doi}](https://opencitations.net/index/api/v1#/reference-count/{doi})

You may use the OpenCitations easily as follows:

```python
import opencitingpy

client = opencitingpy.client.Client()
dois = ['10.3390/s19020353', '10.3390/s19143113']
# get metadata of a list of articles, including title, publication year, number of citing and cited documents, etc.
metadata = client.get_metadata(dois)
```


## Issues

If you run into any trouble or have questions, feel free to 
[open an issue](https://github.com/unaisaralegui/opencitingpy/issues).

## License

[MIT](LICENSE)
