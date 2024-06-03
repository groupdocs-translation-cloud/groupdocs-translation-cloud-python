# Python SDK for Translating Cloud Documents

![](https://img.shields.io/badge/api-v2.0-lightgrey) ![PyPi](https://img.shields.io/pypi/v/groupdocs-translation-cloud) ![PyPi](https://img.shields.io/pypi/dm/groupDocs-translation-cloud) [![GitHub license](https://img.shields.io/github/license/groupdocs-translation-cloud/groupdocs-translation-cloud-python)](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python/blob/master/LICENSE)

[Product Page](https://products.groupdocs.cloud/translation/python/) | [Docs](https://docs.groupdocs.cloud/translation/) | [Demos](https://products.groupdocs.app/translation/family) | [Swagger UI](https://reference.groupdocs.cloud/translation/) | [Examples](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python) | [Blog](https://blog.groupdocs.cloud/category/translation/) | [Search](https://search.groupdocs.cloud/) | [Free Support](https://forum.groupdocs.cloud/c/translation) | [Free Trial](https://purchase.groupdocs.cloud/trial)

[GroupDocs.Translation Cloud](https://products.groupdocs.cloud/translation/) is Cloud API to translate Word (including RTF and TXT files), Excel (including CSV / TSV files), PowerPoint, PDF, HTML, Markdown (including Markdown with Hugo syntax), OpenDocument, RESX, SRT files, images of JPG, PNG, SVG, BMP and GIF formats and scanned PDFs  as well as plain text.

For convenience of our Python customers, we introduce a simple SDK that assists to add translation of all document and image file formats mentioned above and plain text to your app with merely a few lines of code.

In detail, it's a set of SDKs for document and plain text translation in our Cloud. It supports translation of .doc, .docx, .docm, .xls, .xlsx, .xlsm, .ppt, .pptx, .pptm, .pdf, .html, .md, .odt, .ods, .odp, .csv, .tsv, .rtf, .txt, .resx, .srt, .png, .jpg, .svg, .bmp and .gif files. Just pass a specific file or text to the GroupDocs.Translation Cloud API, and it will translate and save translated file in S3 or will return translated text.

It is easy to get started with GroupDocs.Translation Cloud and there is nothing to install. Create an account at GroupDocs Cloud and get your application information, then you are ready to use SDKs.

## Cloud Document Translation Features

- Translation of Microsoft Word®, Microsoft Excel®, and Microsoft PowerPoint® documents
- [46 languages and 140 languages pairs support](https://docs.groupdocs.cloud/translation/supported-languages/)
- Translation of tables, headers, footers, footnotes/endnotes, image captions in Word documents and ODT files
- Translation of cells, charts, tables, pivot tables in Excel documents and ODS files
- Translation of text frames, tables, headers, footers, charts, comments in PowerPoint presentations and ODP files
- Translation of PDF files
- Translation of Markdown files
- Translation of Hugo syntax in Markdown files
- Translation of plain text
- Translation of .NET resources of RESX format
- Translation of subtitles in SRT format
- Translation of images and scanned PDFs getting plain text or PDF as a result
- Translation of scanned tables getting Excel workbook as a result
- Translation of handwritten text 

## Supported Translation Formats

You shoukd specify format of document to translate putting in the request’s body the appropriate enum value.

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
- **en-bn / bn-en** — to translate from English to Bengali or from Bengali to English
- **en-da / da-en** — to translate from English to Danish or from Danish to English
- **en-lt / lt-en** — to translate from English to Lithuanian or from Lithuanian to English
- **en-lv / lv-en** — to translate from English to Latvian or from Latvian to English
- **en-no / no-en** — to translate from English to Norwegian or from Norwegian to English
- **en-et / et-en** — to translate from English to Estonian or from Estonian to English
- **en-hy / hy-en** — to translate from English to Armenian or from Armenian to English
- **en-ca / ca-en** — to translate from English to Catalan or from Catalan to English
- **en-hr / hr-en** — to translate from English to Croatian or from Croatian to English
- **en-sr / sr-en** — to translate from English to Serbian or from Serbian to English
- **en-af / af-en** — to translate from English to Afrikaans or from Afrikaans to English
- **en-ur / ur-en** — to translate from English to Urdu or from Urdu to English
- **en-tl / tl-en** — to translate from English to Tagalog or from Tagalog to English
- **en-ka / ka-en** — to translate from English to Georgian or from Georgian to English
- **fr-de / de-fr** — to translate from French to German or from German to French
- **fr-it / it-fr** — to translate from French to Italian or from Italian to French
- **fr-ar / ar-fr** — to translate from French to Arabic or from Arabic to French
- **fr-es / es-fr** — to translate from French to Spanish or from Spanish to French
- **fr-id / id-fr** — to translate from French to Indonesian or from Indonesian to French
- **fr-ms / ms-fr** — to translate from French to Malay or from Malay to French
- **fr-pl / pl-fr** — to translate from French to Polish or from Polish to French
- **fr-ru / ru-fr** — to translate from French to Russian or from Russian to French
- **fr-ar / ar-fr** — to translate from French to Arabic or from Arabic to French
- **de-it / it-de** — to translate from German to Italian or from Italian to German
- **de-pl / pl-de** — to translate from German to Polish or from Polish to German
- **de-ar / ar-de** — to translate from German to Arabic or from Arabic to German
- **de-zh / zh-de** — to translate from German to Chinese or from Chinese to German
- **de-es / es-de** — to translate from German to Spanish or from Spanish to German
- **de-ms / ms-de** — to translate from German to Malay or from Malay to German
- **de-uk / uk-de** — to translate from German to Ukrainian or from Ukrainian to German
- **it-es / es-it** — to translate from Italian to Spanish or from Spanish to Italian
- **it-ar / ar-it** — to translate from Italian to Arabic or from Arabic to Italian
- **it-uk / uk-it** — to translate from Italian to Ukrainian or from Ukrainian to Italian
- **it-ms / ms-it** — to translate from Italian to Malay or from Malay to Italian
- **sv-zh / zh-sv** — to translate from Swedish to Chinese or from Chinese to Swedish
- **ar-es / es-ar** — to translate from Arabic to Spanish or from Spaish to Arabic
- **ar-tr / tr-ar** — to translate from Arabic to Turkish or from Turkish to Arabic 
- **ar-pl / pl-ar** — to translate from Arabic to Polish or from Polish to Arabic 
- **ru-es / es-ru** — to translate from Russian to Spanish or from Spaish to Russian

## JSON Request Details

You can put the following information in the requests body to translate a document:

- **format** — format of file for translation 
- **outputFormat** — format of translated file (e.g. pdf)
- **sourceLanguage** — language of original document (e.g. en)
- **targetLanguages** — languages of translation as list (e.g. [fr, de])
- **file** — file to translate in form of array of bytes
- **url** — link to file to translate, either file or url should be provided
- **originalFileName** — original name of file to translate, if null or empty request id will be used
- **masters** — if masters slides should be translated (only for presentations, pass true or false)
- **elements** — slide pages to translate (only for presentations, pass empty list to translate whole presentation)
- **separator** — delimiter for CSV files
- **ranges** - dictionary of ranges in Excel workbook 
- **shortcodedict** — dictionary of short code syntax in Hugo to translate, where the key is zero based short code index, and value is a list of parameters names that require translation
- **frontmatterdict** — dictionary of front matter syntax in Hugo to translate, where the key is zero based front matter index and value is list of paths to values that require translation, each path is also a list.

To translate plain text the following information should be put in the requests body:

- **sourceLanguage** — language of original text (e.g. en)
- **targetLanguages** — languages of translation as list (e.g. [fr, de])
- **texts** — list of texts to translate (e.g. [hello world])
- **contains-markdown** — true if text contains markdown syntax

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

## Translate Plain text

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

## Documentation for API Endpoints

All URIs are relative to *https://api.groupdocs.cloud/v2.0/translation*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*TranslationApi* | [**autoPost**](docs/TranslationApi.md#autoPost) | **POST** /auto | Translate any supported file
*TranslationApi* | [**csvPost**](docs/TranslationApi.md#csvPost) | **POST** /csv | Translate CSV and TSV files
*TranslationApi* | [**documentPost**](docs/TranslationApi.md#documentPost) | **POST** /document | Translate Microsoft Word documents, rtf, txt, odt
*TranslationApi* | [**documentRequestIdGet**](docs/TranslationApi.md#documentRequestIdGet) | **GET** /document/{requestId} | Return document translation status.  Also return URLs for downloading of translated document if translation was successful
*TranslationApi* | [**documentTrialPost**](docs/TranslationApi.md#documentTrialPost) | **POST** /document/trial | Trial translate Microsoft Word documents, rtf, txt, odt without conversation. Translate only first page or 1000 symbols.
*TranslationApi* | [**hcGet**](docs/TranslationApi.md#hcGet) | **GET** /hc | Health check for all services.
*TranslationApi* | [**htmlPost**](docs/TranslationApi.md#htmlPost) | **POST** /html | Translate HTML files
*TranslationApi* | [**hugoGet**](docs/TranslationApi.md#hugoGet) | **GET** /hugo | Get hugo syntax structure from markdown file
*TranslationApi* | [**hugoPost**](docs/TranslationApi.md#hugoPost) | **POST** /hugo | Run hugo syntax structure analyzing from markdown file
*TranslationApi* | [**imageToFilePost**](docs/TranslationApi.md#imageToFilePost) | **POST** /image-to-file | Translate image or scanned pdf and return file
*TranslationApi* | [**imageToTextPost**](docs/TranslationApi.md#imageToTextPost) | **POST** /image-to-text | Translate text on image or scanned pdf
*TranslationApi* | [**languagesGet**](docs/TranslationApi.md#languagesGet) | **GET** /languages | Return list of available language pairs
*TranslationApi* | [**markdownPost**](docs/TranslationApi.md#markdownPost) | **POST** /markdown | Translate Markdown files
*TranslationApi* | [**pdfPost**](docs/TranslationApi.md#pdfPost) | **POST** /pdf | Translate pdf files
*TranslationApi* | [**pdfTrialPost**](docs/TranslationApi.md#pdfTrialPost) | **POST** /pdf/trial | Trial pdf translation. Translate only first page without conversion to another format.
*TranslationApi* | [**presentationPost**](docs/TranslationApi.md#presentationPost) | **POST** /presentation | Translate Microsoft PowerPoint presentations, odp
*TranslationApi* | [**resxPost**](docs/TranslationApi.md#resxPost) | **POST** /resx | Translate RESX files
*TranslationApi* | [**spreadsheetPost**](docs/TranslationApi.md#spreadsheetPost) | **POST** /spreadsheet | Translate Microsoft Excel workbooks, ods
*TranslationApi* | [**textPost**](docs/TranslationApi.md#textPost) | **POST** /text | Translate text
*TranslationApi* | [**textRequestIdGet**](docs/TranslationApi.md#textRequestIdGet) | **GET** /text/{requestId} | Return text translation status.  Also return translated text if translation was successful
*TranslationApi* | [**textTrialPost**](docs/TranslationApi.md#textTrialPost) | **POST** /text/trial | Trial translate text. Translate only 1000 symbols.


## Documentation for Models

- [CloudFileResponse](docs/CloudFileResponse.md)
- [CloudHugoResponse](docs/CloudHugoResponse.md)
- [CloudTextResponse](docs/CloudTextResponse.md)
- [CsvFileRequest](docs/CsvFileRequest.md)
- [FileRequest](docs/FileRequest.md)
- [HealthCheckStatus](docs/HealthCheckStatus.md)
- [HtmlFileRequest](docs/HtmlFileRequest.md)
- [HttpStatusCode](docs/HttpStatusCode.md)
- [HugoRequest](docs/HugoRequest.md)
- [ImageToFileRequest](docs/ImageToFileRequest.md)
- [ImageToTextRequest](docs/ImageToTextRequest.md)
- [LanguagePairData](docs/LanguagePairData.md)
- [MarkdownFileRequest](docs/MarkdownFileRequest.md)
- [PdfFileRequest](docs/PdfFileRequest.md)
- [PresentationFileRequest](docs/PresentationFileRequest.md)
- [ResxFileRequest](docs/ResxFileRequest.md)
- [SpreadsheetFileRequest](docs/SpreadsheetFileRequest.md)
- [StatusResponse](docs/StatusResponse.md)
- [StringStringTuple](docs/StringStringTuple.md)
- [TextDocumentFileRequest](docs/TextDocumentFileRequest.md)
- [TextRequest](docs/TextRequest.md)
- [UrlFileInfo](docs/UrlFileInfo.md)
- [WorksheetData](docs/WorksheetData.md)

## GroupDocs.Translation Cloud SDKs in Popular Languages

| .NET | Java | Python | Android |
|---|---|---|---|
| [GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-dotnet) | [GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-java) | [GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python) | [GitHub](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-android) |
| [NuGet](https://www.nuget.org/packages/GroupDocs.translation-Cloud/) | [Maven](https://repository.groupdocs.cloud/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-translation-cloud) | [PIP](https://pypi.org/project/groupdocs-translation-cloud/) | [Maven](https://repository.groupdocs.cloud/webapp/#/artifacts/browse/tree/General/repo/com/groupdocs/groupdocs-translation-cloud-android) |

[Product Page](https://products.groupdocs.cloud/translation/python/) | [Docs](https://docs.groupdocs.cloud/translation/) | [Demos](https://products.groupdocs.app/translation/family) | [Swagger UI](https://reference.groupdocs.cloud/translation/) | [Examples](https://github.com/groupdocs-translation-cloud/groupdocs-translation-cloud-python) | [Blog](https://blog.groupdocs.cloud/category/translation/) | [Search](https://search.groupdocs.cloud/) | [Free Support](https://forum.groupdocs.cloud/c/translation) | [Free Trial](https://purchase.groupdocs.cloud/trial)