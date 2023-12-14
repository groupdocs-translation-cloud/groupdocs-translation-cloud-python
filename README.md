# Python SDK for Translating Cloud Documents

![GitHub](https://img.shields.io/github/license/groupdocs-translation-cloud/groupdocs-translation-cloud-android) ![](https://img.shields.io/badge/api-v2.0-lightgrey) ![Nuget](https://img.shields.io/nuget/vpre/GroupDocs.translation-Cloud) ![Nuget](https://img.shields.io/nuget/dt/GroupDocs.translation-Cloud) [![GitHub license](https://img.shields.io/github/license/groupdocs-translation-cloud/groupdocs-translation-cloud-dotnet)](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-dotnet/blob/master/LICENSE)

[Product Page](https://products.groupdocs.cloud/translation/dotnet/) | [Docs](https://docs.groupdocs.cloud/translation/) | [Demos](https://products.groupdocs.app/translation/family) | [Swagger UI](https://apireference.groupdocs.cloud/translation/) | [Examples](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-dotnet) | [Blog](https://blog.groupdocs.cloud/category/translation/) | [Search](https://search.groupdocs.cloud/) | [Free Support](https://forum.groupdocs.cloud/c/translation) | [Free Trial](https://purchase.groupdocs.cloud/trial)

[GroupDocs.Translation Cloud](https://products.groupdocs.cloud/translation/) is Cloud API to translate Word, Excel, PowerPoint, PDF, HTML, Markdown (including Markdown with Hugo syntax), OpenDocument, RESX, SRT files, scanned images and scanned PDF documents and plain text.

For convenience of our Python customers, we introduce a simple SDK that assists to add translation of Microsoft Word documents, Microsoft Excel workbooks, Microsoft PowerPoint presentations, PDF documents, Markdown (including Hugo), OpenDocument files, scanned images and PDFs and plain text to your app with merely a few lines of code.

In detail, it's a set of SDKs for document, images and plain text translation in our Cloud. It supports translation of .doc, .docx, .docm, .xls, .xlsx, .xlsm, .ppt, .pptx, .pptm, .pdf, .html, .md, .odt, .ods, .odp, .csv, .tsv, .rtf, .txt, .resx, .srt, .png, .jpg, .bmp files. Just pass a specific file or text to the GroupDocs.Translation Cloud API, and it will translate and save translated file in our Cloud or will return translated text.

It is easy to get started with GroupDocs.Translation Cloud and there is nothing to install. Create an account at GroupDocs Cloud and get your application information, then you are ready to use SDKs.

## Cloud Document Translation Features

- Translation of Microsoft Word®, Microsoft Excel®, and Microsoft PowerPoint® documents
- [46 languages and 96 languages pairs support](https://docs.groupdocs.cloud/translation/supported-languages/)
- Translation of tables, headers, footers, footnotes/endnotes, image captions in Word documents and ODT files
- Translation of cells, charts, tables, pivot tables in Excel documents and ODS files
- Translation of text frames, tables, headers, footers, charts, comments in PowerPoint presentations and ODP files
- Translation of PDF files
- Translation of Markdown files
- Translation of Hugo syntax in Markdown files
- Translation of plain text
- Translation of images
- API that allows you to manage your files and folders in our Cloud

## Supported Translation Formats

You can specify format of document to translate putting in the request’s body:

- **extension of word file (docx / docm / doc / rtf)** — to translate **Microsoft Word® document**
- **extension of excel file (xlsx / xlsm / xls / csv / tsv)** — to translate **Microsoft Excel® workbook**
- **extension of powerpoint file (ppt / pptx / pptm)** — to translate **Microsoft PowerPoint® presentation**
- **extension of PDF file (pdf)** — to translate **Adobe PDF document**
- **extension of Markdown file (md)** — to translate **Markdown file**
- **extension of HTML file (html)** — to translate **HTML file**
- **extension of OpenDocument file (odt / ods / odp)** — to translate files created in OpenOffice or similar suits
- **extension of Resources file (resx)** — to translate **resource file for .NET application**
- **hugo** - to translate Markdown file with Hugo syntax

Additionally, user could obtain translated file in any other format available for conversion. Just specify output format of translated document by putting file extension in the request’s body:

- **doc, docx, odt, rtf** — docx, rtf, html, odt, txt, md, pdf, tiff, svg, xps
- **xls, xlsx, ods, csv, tsv** — xlsx, xlsb, html, pdf, xps, ods, md, docx, pptx, tiff
- **ppt, pptx, odp** — pptx, pdf, tiff, html, xps, odp
- **pdf** — docx, pptx, html, svg, xps
- **md** — html, pdf, docx, tiff, xps
- **html** — md, pdf, docx, tiff, xps

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
- **en-nl / nl-en** — to translate from English to Dutch or from Dutch to English
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
- **en-be / be-en** — to translate from English to Bengali or from Bengali to English
- **en-da / da-en** — to translate from English to Danish or from Danish to English
- **en-no / no-en** — to translate from English to Norwegian or from Norwegian to English
- **en-lv / lv-en** — to translate from English to Latvian or from Latvian to English
- **en-lt / lt-en** — to translate from English to Lithuanian or from Lithuanian to English
- **en-et / et-en** — to translate from English to Estonian or from Estonian to English
- **en-ca / ca-en** — to translate from English to Catalan or from Catalan to English
- **en-hy / hy-en** — to translate from English to Armenian or from Armenian to English
- **en-hr / hr-en** — to translate from English to Croatian or from Croatian to English
- **en-sr / sr-en** — to translate from English to Serbian or from Serbian to English
- **en-af / af-en** — to translate from English to Afrikaans or from Afrikaans to English
- **en-ur / ur-en** — to translate from English to Urdu or from Urdu to English
- **en-tl / tl-en** — to translate from English to Tagalog or from Tagalog to English
- **en-ka / ka-en** — to translate from English to Georgian or from Georgian to English
- **fr-de / de-fr** — to translate from French to German or from German to French
- **fr-it / it-fr** — to translate from French to Italian or from Italian to French
- **fr-ar / ar-fr** — to translate from French to Arabic or from Arabic to French


## How to use the SDK?

Our API is completely independent of your operating system, database system, or development language. You can use any language and platform that supports HTTP to interact with our API. However, manually writing client code can be difficult, error-prone, and time-consuming. Therefore, we have provided and support [SDKs](https://github.com/groupdocs-translation-cloud) in many development languages to make it easier for your Cloud Apps to integrate with us.

### Get API keys if you haven't

Make a personal account on [GroupDocs Cloud Dashboard](https://dashboard.groupdocs.cloud/#/) and click _Get Keys_. These keys are useful for all GroupDocs Cloud products. If you have any trouble, look at this [detailed manual](https://docs.groupdocs.cloud/total/creating-and-managing-application/). Once your keys are received, please follow this [article](https://docs.groupdocs.cloud/translation/quickstart/) to try GroupDocs.Translation Cloud or familiarize with [Developer guide](https://docs.groupdocs.cloud/translation/developer-guide/) for further details.

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python.git`)

or

```sh
pip install groupdocs-translation-cloud
```

Then import the package:
```python
import groupdocs_translation_cloud
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import groupdocs_translation_cloud
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import groupdocs_translation_cloud
from groupdocs_translation_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_translation_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs_translation_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)


# Enter a context with an instance of the API client
with groupdocs_translation_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_translation_cloud.SwaggerApi(api_client)
    is_yaml = False # bool |  (optional) (default to False)
    serialaize_as_v2 = False # bool |  (optional) (default to False)

    try:
        api_instance.swagger_spec_get(is_yaml=is_yaml, serialaize_as_v2=serialaize_as_v2)
    except ApiException as e:
        print("Exception when calling SwaggerApi->swagger_spec_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.groupdocs.cloud/v2.0/translation*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*SwaggerApi* | [**swagger_spec_get**](docs\SwaggerApi.md#swagger_spec_get) | **GET** /swagger/spec | 
*TranslationApi* | [**auto_post**](docs\TranslationApi.md#auto_post) | **POST** /auto | Translate any supported file
*TranslationApi* | [**csv_post**](docs\TranslationApi.md#csv_post) | **POST** /csv | Translate CSV and TSV files
*TranslationApi* | [**document_post**](docs\TranslationApi.md#document_post) | **POST** /document | Translate Microsoft Word documents, rtf, txt, odt
*TranslationApi* | [**document_request_id_get**](docs\TranslationApi.md#document_request_id_get) | **GET** /document/{requestId} | Return document translation status.  Also return URLs for downloading of translated document if translation was successful
*TranslationApi* | [**document_trial_get**](docs\TranslationApi.md#document_trial_get) | **GET** /document/trial | Return document translation status for trial request.  Also return URLs for downloading of translated document if translation was successful
*TranslationApi* | [**document_trial_post**](docs\TranslationApi.md#document_trial_post) | **POST** /document/trial | Trial translate Microsoft Word documents, rtf, txt, odt without conversation. Translate only first page or 1000 symbols.
*TranslationApi* | [**hc_get**](docs\TranslationApi.md#hc_get) | **GET** /hc | Health check for all services.
*TranslationApi* | [**html_post**](docs\TranslationApi.md#html_post) | **POST** /html | Translate HTML files
*TranslationApi* | [**hugo_get**](docs\TranslationApi.md#hugo_get) | **GET** /hugo | Get hugo syntax structure from markdown file
*TranslationApi* | [**hugo_post**](docs\TranslationApi.md#hugo_post) | **POST** /hugo | Run hugo syntax structure analyzing from markdown file
*TranslationApi* | [**image_to_file_post**](docs\TranslationApi.md#image_to_file_post) | **POST** /image-to-file | Translate image or scanned pdf and return file
*TranslationApi* | [**image_to_text_post**](docs\TranslationApi.md#image_to_text_post) | **POST** /image-to-text | Translate text on image or scanned pdf
*TranslationApi* | [**languages_get**](docs\TranslationApi.md#languages_get) | **GET** /languages | Return list of available language pairs
*TranslationApi* | [**markdown_post**](docs\TranslationApi.md#markdown_post) | **POST** /markdown | Translate Markdown files
*TranslationApi* | [**pdf_post**](docs\TranslationApi.md#pdf_post) | **POST** /pdf | Translate pdf files
*TranslationApi* | [**pdf_trial_post**](docs\TranslationApi.md#pdf_trial_post) | **POST** /pdf/trial | Trial pdf translation. Translate only first page without conversion to another format.
*TranslationApi* | [**presentation_post**](docs\TranslationApi.md#presentation_post) | **POST** /presentation | Translate Microsoft PowerPoint presentations, odp
*TranslationApi* | [**resx_post**](docs\TranslationApi.md#resx_post) | **POST** /resx | Translate Resx files
*TranslationApi* | [**spreadsheet_post**](docs\TranslationApi.md#spreadsheet_post) | **POST** /spreadsheet | Translate Microsoft Excel workbooks, ods
*TranslationApi* | [**srt_post**](docs\TranslationApi.md#srt_post) | **POST** /srt | Translate Srt files
*TranslationApi* | [**text_post**](docs\TranslationApi.md#text_post) | **POST** /text | Translate text
*TranslationApi* | [**text_request_id_get**](docs\TranslationApi.md#text_request_id_get) | **GET** /text/{requestId} | Return text translation status.  Also return translated text if translation was successful
*TranslationApi* | [**text_trial_get**](docs\TranslationApi.md#text_trial_get) | **GET** /text/trial | Return text translation status for trial requests.  Also return translated text if translation was successful
*TranslationApi* | [**text_trial_post**](docs\TranslationApi.md#text_trial_post) | **POST** /text/trial | Trial translate text. Translate only 1000 symbols.


## Documentation For Models

 - [CloudFileRequest](docs\CloudFileRequest.md)
 - [CloudFileResponse](docs\CloudFileResponse.md)
 - [CloudFileResponseWithAdditionalInfo](docs\CloudFileResponseWithAdditionalInfo.md)
 - [CloudHugoResponse](docs\CloudHugoResponse.md)
 - [CloudTextResponse](docs\CloudTextResponse.md)
 - [CsvFileRequest](docs\CsvFileRequest.md)
 - [FileRequest](docs\FileRequest.md)
 - [HealthCheckStatus](docs\HealthCheckStatus.md)
 - [HtmlFileRequest](docs\HtmlFileRequest.md)
 - [HttpStatusCode](docs\HttpStatusCode.md)
 - [HugoRequest](docs\HugoRequest.md)
 - [ImageToFileRequest](docs\ImageToFileRequest.md)
 - [ImageToTextRequest](docs\ImageToTextRequest.md)
 - [LanguagePairData](docs\LanguagePairData.md)
 - [MarkdownFileRequest](docs\MarkdownFileRequest.md)
 - [PdfFileRequest](docs\PdfFileRequest.md)
 - [PresentationFileRequest](docs\PresentationFileRequest.md)
 - [SpreadsheetFileRequest](docs\SpreadsheetFileRequest.md)
 - [SrtFileRequest](docs\SrtFileRequest.md)
 - [StatusResponse](docs\StatusResponse.md)
 - [StringStringTuple](docs\StringStringTuple.md)
 - [TextDocumentFileRequest](docs\TextDocumentFileRequest.md)
 - [TextRequest](docs\TextRequest.md)
 - [UrlFileInfo](docs\UrlFileInfo.md)
 - [WorksheetData](docs\WorksheetData.md)


## GroupDocs.Translation Cloud SDKs in Popular Languages

| .NET | Java | Python | Android |
|---|---|---|---|
| [GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-dotnet) | [GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-java) | [GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python) | [GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-android) |
| [NuGet](https://www.nuget.org/packages/GroupDocs.translation-Cloud/) | [Maven](https://repository.groupdocs.cloud/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-translation-cloud) | [PIP](https://pypi.org/project/groupdocs-translation-cloud/) | [Maven](https://repository.groupdocs.cloud/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-translation-cloud-android) |

[Product Page](https://products.groupdocs.cloud/translation/python/) | [Docs](https://docs.groupdocs.cloud/translation/) | [Demos](https://products.groupdocs.app/translation/family) | [Swagger UI](https://apireference.groupdocs.cloud/translation/) | [Examples](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python) | [Blog](https://blog.groupdocs.cloud/category/translation/) | [Search](https://search.groupdocs.cloud/) | [Free Support](https://forum.groupdocs.cloud/c/translation) | [Free Trial](https://purchase.groupdocs.cloud/trial)
