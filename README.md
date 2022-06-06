# Python SDK for Translating Cloud Documents

![](https://img.shields.io/badge/api-v1.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/groupdocs-translation-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/groupdocs-translation-cloud) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/groupdocs-translation-cloud) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/groupdocs-translation-cloud) [![GitHub license](https://img.shields.io/github/license/groupdocs-translation-cloud/groupdocs-translation-cloud-python)](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python/blob/master/LICENSE)

[Product Page](https://products.groupdocs.cloud/translation/python/) | [Docs](https://docs.groupdocs.cloud/translation/) | [Demos](https://products.groupdocs.app/translation/family) | [Swagger UI](https://apireference.groupdocs.cloud/translation/) | [Examples](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python) | [Blog](https://blog.groupdocs.cloud/category/translation/) | [Search](https://search.groupdocs.cloud/) | [Free Support](https://forum.groupdocs.cloud/c/translation) | [Free Trial](https://purchase.groupdocs.cloud/trial)

[GroupDocs.Translation Cloud](https://products.groupdocs.cloud/translation/) is Cloud API to translate Word, Excel, PowerPoint, PDF, Markdown, OpenDocument files as well as plain text.

For convenience of our Python customers, we introduce a simple SDK that assists to add translation of Microsoft Word documents, Microsoft Excel workbooks, Microsoft PowerPoint presentations, PDF documents, Markdown, OpenDocument files, and plain text to your app with merely a few lines of code.

In detail, it's a set of SDKs for document and plain text translation in our Cloud. It supports translation of .doc, .docx, .docm, .xls, .xlsx, .xlsm, .ppt, .pptx, .pptm, .pdf, .md, .odt, .ods, .odp, .csv, .tsv, .rtf, .txt files. Just pass a specific file or text to the GroupDocs.Translation Cloud API, and it will translate and save translated file in our Cloud or will return translated text.

It is easy to get started with GroupDocs.Translation Cloud and there is nothing to install. Create an account at GroupDocs Cloud and get your application information, then you are ready to use SDKs.

## Cloud Document Translation Features

- Translation of Microsoft Word®, Microsoft Excel®, and Microsoft PowerPoint® documents
- [32 languages and 68 languages pairs support](https://docs.groupdocs.cloud/translation/supported-languages/)
- Translation of tables, headers, footers, footnotes/endnotes, image captions in Word documents and ODT files
- Translation of cells, charts, tables, pivot tables in Excel documents and ODS files
- Translation of text frames, tables, headers, footers, charts, comments in PowerPoint presentations and ODP files
- Translation of PDF files
- Translation of Markdown files
- Translation of plain text
- API that allows you to manage your files and folders in our Cloud

## Supported Translation Formats

You can specify format of document to translate putting in the request’s body:

- **extension of word file (docx / docm / doc / rtf)** — to translate **Microsoft Word® document**
- **extension of excel file (xlsx / xlsm / xls / csv / tsv)** — to translate **Microsoft Excel® workbook**
- **extension of powerpoint file (ppt / pptx / pptm)** — to translate **Microsoft PowerPoint® presentation**
- **extension of PDF file (pdf)** — to translate **Adobe PDF document**
- **extension of Markdown file (md)** — to translate **Markdown file**
- **extension of OpenDocument file (odt / ods / odp)** — to translate files created in OpenOffice or similar suits

Additionally, user could obtain translated file in any other format available for conversion. Just specify output format of translated document by putting file extension in the request’s body:

- **doc, docx, odt, rtf** — docx, rtf, html, odt, txt, md, pdf, tiff, svg, xps
- **xls, xlsx, ods, csv, tsv** — xlsx, xlsb, html, pdf, xps, ods, md, docx, pptx, tiff
- **ppt, pptx, odp** — pptx, pdf, tiff, html, xps, odp
- **pdf** — docx, pptx, html, svg, xps
- **md** — html, pdf, docx, tiff, xps

Please visit [Supported Formats](https://docs.groupdocs.cloud/translation/supported-formats/) for details.

## Supported Translation Languages

- **en-fr / fr-en** — to translate from English to French or from French to English.
- **en-de / de-en** — to translate from English to German or from German to English.
- **en-es / es-en** — to translate from English to Spanish or from Spanish to English.
- **en-it / it-en** — to translate from English to Italian or from Italian to English.
- **en-zh / zh-en** — to translate from English to Chinese or from Chinese to English.
- **en-ru / ru-en** — to translate from English to Russian or from Russian to English
- **en-ar / ar-en** — to translate from English to Arabic or from Arabic to English
- **en-pt / pt-en** — to translate from English to Portuguese or from Portuguese to English
- **en-pl / pl-en** — to translate from English to Polish or from Polish to English
- **en-uk / uk-en** — to translate from English to Ukrainian or from Ukrainian to English
- **en-vi / vi-en** — to translate from English to Vietnamese or from Vietnamese to English
- **en-id / id-en** — to translate from English to Indonesian or from Indonesian to English
- **en-hi / hi-en** — to translate from English to Hindi or from Hindi to English
- **en-el / el-en** — to translate from English to Greek or from Greek to English
- **en-nl / nl-en**— to translate from English to Dutch or from Dutch to English
- **en-hu / hu-en** — to translate from English to Hunngarian or from Hungarian to English
- **en-sv / sv-en** — to translate from English to Swedish or from Swedish to English
- **en-tr / tr-en** — to translate from English to Turkish or from Turkish to English
- **en-ja / ja-en** — to translate from English to Japanese or from Japanese to English
- **en-ko / ko-en** — to translate from English to Korean or from Korean to English
- **en-cs / cs-en** — to translate from English to Czech or from Czech to English
- **en-fi / fi-en** — to translate from English to Finnish or from Finnish to English
- **en-ga / ga-en** — to translate from English to Irish or from Irish to English
- **en-fa / fa-en** — to translate from English to Farsi or from Farsi to English
- **en-az / az-en** — to translate from English to Azerbaijani or from Azerbaijani to English
- **en-he / he-en** — to translate from English to Hebrew or from Hebrew to English
- **en-sk / sk-en** — to translate from English to Slovak or from Slovak to English
- **en-th / th-en** — to translate from English to Thai or from Thai to English
- **en-ro / ro-en** — to translate from English to Romanian or from Romanian to English
- **en-ms / ms-en** — to translate from English to Malay or from Malay to English
- **en-bg / bg-en** — to translate from English to Bulgarian or from Bulgarian to English
- **fr-de / de-fr** — to translate from French to German or from German to French
- **fr-it / it-fr** — to translate from French to Italian or from Italian to French
-  **fr-ar / ar-fr** — to translate from French to Arabic or from Arabic to French

## JSON Request Details

You can put the following information in the requests body to translate a document:

- **format** — format of file for translation (e.g. docx)
- **outformat** — format of translated file (e.g. pdf)
- **pair** — language translation pair (e.g. en-fr)
- **name** — name of file to translate (e.g. test.docx)
- **folder** — folder of file to translate (e.g. translate)
- **savepath** — folder for translated file (e.g. translated)
- **savefile** — name of translated file (e.g. translation.docx)
- **storage** — name of storage
- **masters** — if masters slides should be translated (only for presentations, pass true or false)
- **elements** — slide pages to translate (only for presentations, pass empty list to translate whole presentation)

To translate plain text the following information should be put in the requests body:

- **pair** — language translation pair (e.g. en-fr)
- **text** — text to translate (e.g. hello world)


## How to use the SDK?

Our API is completely independent of your operating system, database system, or development language. You can use any language and platform that supports HTTP to interact with our API. However, manually writing client code can be difficult, error-prone, and time-consuming. Therefore, we have provided and support [SDKs](https://github.com/groupdocs-translation-cloud) in many development languages to make it easier for your Cloud Apps to integrate with us.

## Quickstart

#### 1. Get API keys if you haven't

Make a personal account on [GroupDocs Cloud Dashboard](https://dashboard.groupdocs.cloud/#/) and click _Get Keys_. These keys are useful for all GroupDocs Cloud products. If you have any trouble, look at this [detailed manual](https://docs.groupdocs.cloud/total/creating-and-managing-application/). Once your keys are received, please follow this [article](https://docs.groupdocs.cloud/translation/quickstart/) to try GroupDocs.Translation Cloud or familiarize with [Developer guide](https://docs.groupdocs.cloud/translation/developer-guide/) for further details.

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
  * Set Your client\_id & client\_secret
  * Run Jupyter Notebook [demo.ipynb](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python/blob/master/demo.ipynb)

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

## Translate Word document

```python
# Load the gem
import groupdocs_translation_cloud
# Get Client Id and Client Secret from https://dashboard.groupdocs.cloud
my_client_id = ""
my_client_secret = ""

# Create instance of the API
configuration = Configuration(apiKey=my_client_secret, appSid=my_client_id)
api = TranslationApi(configuration)

#document translation
pair = "en-fr"
_format = "docx"
storage = "First Storage"
name = "test.docx"
folder = ""
savepath = ""
savefile = "test_python.docx"  
masters = False
elements = []
translator = TranslateDocument(pair, _format, storage, name, folder, savepath, savefile, masters, elements)
request = translator.to_string()
res_doc = api.post_translate_document(request)
print(res_doc.message)
```



## GroupDocs.Translation Cloud SDKs in Popular Languages

| .NET | Java | Python | Android |
|---|---|---|---|
| [GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-dotnet) | [GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-java) | [GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python) | [GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-android) |
| [NuGet](https://www.nuget.org/packages/GroupDocs.translation-Cloud/) | [Maven](https://repository.groupdocs.cloud/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-translation-cloud) | [PIP](https://pypi.org/project/groupdocs-translation-cloud/) | [Maven](https://repository.groupdocs.cloud/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-translation-cloud-android) |

[Product Page](https://products.groupdocs.cloud/translation/python/) | [Docs](https://docs.groupdocs.cloud/translation/) | [Demos](https://products.groupdocs.app/translation/family) | [Swagger UI](https://apireference.groupdocs.cloud/translation/) | [Examples](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python) | [Blog](https://blog.groupdocs.cloud/category/translation/) | [Search](https://search.groupdocs.cloud/) | [Free Support](https://forum.groupdocs.cloud/c/translation) | [Free Trial](https://purchase.groupdocs.cloud/trial)