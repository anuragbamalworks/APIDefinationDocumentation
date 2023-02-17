# APIDefinationDocumentation

A Python package to convert an OpenAPI 3.0 specification to a Microsoft Word document.

## Installation

pip install openapiToDocx 

## Usage

```python
from openapiToDocx import generateApiDocumentaion

generateApiDocumentaion('path/to/openapi.yml', 'output.docx')

This will create a Word document with the OpenAPI specification at the given path.

You can then create a `requirements.txt` file by running the following command in the project directory:

pip freeze > requirements.txt

This will save the current package requirements to a `requirements.txt` file. You can include this file in the project to make it easier for users to install the required dependencies.