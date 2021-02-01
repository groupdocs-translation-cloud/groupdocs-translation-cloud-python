![](https://img.shields.io/badge/api-v1.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/groupdocs-translation-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/groupdocs-translation-cloud) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/groupdocs-translation-cloud) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/groupdocs-translation-cloud) [![GitHub license](https://img.shields.io/github/license/groupdocs-translation-cloud/groupdocs-translation-cloud-python)](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python/blob/master/LICENSE)
# Python SDK for Translating Cloud Documents

[GroupDocs.Translation Cloud](https://products.groupdocs.cloud/translation) is Cloud API to translate Word, Excel and PowerPoint files as well as plain text.

For convenience of our Java customers we introduce a simple SDK used to add translation of Microsoft Word documents, Microsoft Excel workbooks, Microsoft PowerPoint presentations and plain text to your app with merely a few lines of code.

In detail, it's a set of SDKs for document and plain text translation in our Cloud. It supports translation of .doc, .docx, .docm, .xls, .xlsx, .xlsm, .ppt, .pptx, .pptm files. Just pass a specific file or text to the GroupDocs.Translation Cloud API, and it will translate and save translated file in our Cloud or will return translated text.

It is easy to get started with GroupDocs.Translation Cloud, and there is nothing to install. Create an account at [GroupDocs Cloud](https://dashboard.groupdocs.cloud/#/) and get your application information, then you are ready to use [SDKs](https://github.com/groupdocs-translation-cloud)

## Cloud Document Translation Features

- Translation of Microsoft Word, Microsoft Excel,, and Microsoft PowerPoint documents
- [10 languages and 22 languages pairs support](https://docs.groupdocs.cloud/translation/supported-languages/)
- Translation of tables, headers, footers, footnotes/endnotes, image captions in Word documents
- Translation of cells, charts, tables, pivot tables in Excel documents
- Translation of text frames, tables, headers, footers, charts, comments in PowerPoint presentations
- Translation of plain text
- API that allows you to manage your files and folders in our Cloud

## Supported Formats

GroupDocs.Translation Cloud allows to translate Microsoft Word and Excel documents. User should specify format of document to translate putting in the request’s body:

- **extension of word file (docx / docm / doc)** — to translate **Microsoft Word document**
- **extension of excel file (xlsx / xlsm / xls**) — to translate **Microsoft Excel workbook**
- **extension of powerpoint file (ppt / pptx / pptm**) — to translate **Microsoft PowerPoint presentation**

Additionally, user could obtain translated file in any other format available for conversion. Just specify output format of translated document putting file extension in the request’s body:

- **doc, docx** — docx, rtf, html, odt, txt, md, pdf, tiff, svg, xps
- **xls, xlsx** — xlsx, xlsb, html, pdf, xps, ods, md, docx, pptx, tiff
- **ppt, pptx** — pptx, pdf, tiff, html, xps, odp

## New Features & Enhancements Release 20.12
- Conversion of translated files to other formats is added

## New Features & Enhancements Release 20.10
- Microsoft PowerPoint presentations translation
- French-Italian language pair support

## New Features & Enhancements Release 20.9
- French-German language pair support

## New Features & Enhancements Release 20.8
- GroupDocs.Translation Java SDK


## How to use the SDK?

Our API is completely independent of your operating system, database system, or development language. You can use any language and platform that supports HTTP to interact with our API. However, manually writing client code can be difficult, error-prone, and time-consuming. Therefore, we have provided and support [SDKs](https://github.com/groupdocs-translation-cloud) in many development languages to make it easier to integrate with us.

## Examples

```python
from groupdocstranslationcloud.configuration import Configuration
from groupdocstranslationcloud.api.translation_api import TranslationApi
from groupdocstranslationcloud.models.translate_text import TranslateText
from groupdocstranslationcloud.models.translate_document import TranslateDocument

#enter valid client_secret and client_id
configuration = Configuration(client_secret="", client_id="")
api = TranslationApi(configuration)

# text translation
pair = "en-fr"
text = "Welcome to Paris"
translator = TranslateText(pair, text)
request = translator.to_string()
res_text = api.post_translate_text(request)
print(res_text.translation)

#document translation
pair = "en-fr"
_format = "docx"
ourformat = "docx"
storage = "First Storage"
name = "test.docx"
folder = ""
savepath = ""
savefile = "test_python.docx"  
masters = False
elements = []
translator = TranslateDocument(pair, _format, outformat, storage, name, folder, savepath, savefile, masters, elements)
request = translator.to_string()
res_doc = api.post_translate_document(request)
print(res_doc.message)
```
_________________________

## Quickstart

Make your solution using [SDK](https://github.com/groupdocs-translation-cloud), follow these steps:

#### 1. Get API keys if you haven't

Make a personal account on [GroupDocs Cloud Dashboard](https://dashboard.groupdocs.cloud/#/) and click _Get Keys_. These keys are useful for all GroupDocs Cloud products. If you have any trouble, look at this [detailed manual](https://docs.groupdocs.cloud/total/creating-and-managing-application/).

#### 2. Install SDK

Install `groupdocs-translation-cloud` with [PIP](https://pypi.org/project/pip/) from [PyPI](https://pypi.org/) by:

```sh
pip install groupdocs-translation-cloud
```

Or clone repository and install it via [Setuptools](http://pypi.python.org/pypi/setuptools):

```sh
python setup.py install
```

#### 3. Run Demo

  * Checkout the SDK or get from PiPy
  * Set Your client_id & client_secret
  * Run Jupyter Notebook [demo.ipynb](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python/blob/master/demo.ipynb)

---------------------------

### Structure

This project includes:

- Module "groupdocstranslationcloud", this is SDK. You can integrate it in your application. It contains both Translation and Storage API
- Module "test", unittests. You can take a look at them to see various code examples.
- Jupyter notebook "demo". Sample demo notebook.

### Dependencies
- See requirements.txt

## Versions support:
- Python :: 2.7
- Python :: 3
- Python :: 3.4
- Python :: 3.5
- Python :: 3.6
- Python :: 3.7
- Python :: 3.8



## GroupDocs.Translation Cloud SDKs in Popular Languages

| .NET | Java | Python |
|---|---|---|
| [GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-dotnet) | [GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-java) |[GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python) |
| [NuGet](https://www.nuget.org/packages/GroupDocs.translation-Cloud/) | [Maven](https://repository.groupdocs.cloud/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-translation-cloud) | [PIP](https://pypi.org/project/groupdocs-translation-cloud/) |

[Home](https://www.groupdocs.cloud/) | [Product Page](https://products.groupdocs.cloud/translation/python) | [Docs](https://docs.groupdocs.cloud/translation/) | [Demos](https://products.groupdocs.app/viewer/family) | [API Reference](https://apireference.groupdocs.cloud/translation/) | [Examples](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python) | [Blog](https://blog.groupdocs.cloud/category/translation/) | [Free Support](https://forum.groupdocs.cloud/c/translation) | [Free Trial](https://purchase.groupdocs.cloud/trial)
