import time
import unittest

import groupdocs_translation_cloud
from groupdocs_translation_cloud import TextRequest, PdfFileRequest, TextDocumentFileRequest, SpreadsheetFileRequest, \
    CsvFileRequest, PresentationFileRequest, SrtFileRequest, MarkdownFileRequest, ImageToFileRequest, ImageToTextRequest, \
    HugoRequest, HtmlFileRequest
from groupdocs_translation_cloud.models.api_enums import SavingMode, Format

api = groupdocs_translation_cloud.api.TranslationApi()
file_api = groupdocs_translation_cloud.api.FileApi()
api.api_client.configuration.client_id = "your-id"
api.api_client.configuration.client_secret = "your-secret"


# Get File Translation


def get_file_translation(request_id: str):
    while True:
        file_response = api.document_request_id_get(request_id)
        if file_response.status == 200:
            print(file_response.message)
            for lang in file_response.urls:
                print(lang + ',' + str(int(file_response.urls[lang].size / 1000)) + ' kb, url: ' + file_response.urls[
                    lang].url)
            break
        time.sleep(2)


class TestTranslationApi(unittest.TestCase):

    # TEXT
    def testTextTranslation(self):
        text_request = TextRequest(source_language="en"
                                   , target_languages=["es", "fr", "ru"]
                                   , texts=["Hello World!", "This is a test text"]
                                   , origin="your_application_name"
                                   , contains_markdown=False)
        response = api.text_post(text_request)
        if response.status == 202:
            while True:
                status_response = api.text_request_id_get(response.id)
                if status_response.status == 200:
                    for lang in status_response.translations:
                        print(lang + ": " + status_response.translations[lang][0])
                    break
                time.sleep(2)

    # PDF
    def testPdfTranslation(self):
        url = file_api.file_upload_post(file="../test_data/TestPdf.pdf", format=Format.Pdf)
        pdf_request = PdfFileRequest(source_language="en"
                                     , target_languages=["ru"]
                                     , url=url
                                     , output_format=Format.Pdf)
        response = api.pdf_post(pdf_request)
        if response.status == 202:
            print('Pdf document translation started')
            get_file_translation(response.id)

    # Word
    def testWordTranslation(self):
        url = file_api.file_upload_post(file="../test_data/TestWord.docx")
        word_request = TextDocumentFileRequest(source_language="en"
                                               , target_languages=["ru"]
                                               , url=url
                                               , format=Format.Docx
                                               , saving_mode=SavingMode.Files
                                               , origin="python-test"
                                               , original_name="TestWord"
                                               , output_format=Format.Docx)
        response = api.document_post(word_request)
        if response.status == 202:
            print('Word document translation started')
            get_file_translation(response.id)

    # Spreadsheet
    def testSpreadsheetTranslation(self):
        url = file_api.file_upload_post(file="../test_data/TestExcel.xlsx")
        spreadsheet_request = SpreadsheetFileRequest(source_language="en"
                                                     , target_languages=["ru"]
                                                     , url=url
                                                     , format=Format.Xlsx
                                                     , saving_mode=SavingMode.Files
                                                     , origin="python-test"
                                                     , original_name="TestExcel"
                                                     , output_format=Format.Xlsx)
        response = api.spreadsheet_post(spreadsheet_request)
        if response.status == 202:
            print('Spreadsheet translation started')
            get_file_translation(response.id)

    # Csv
    def testCsvTranslation(self):
        url = file_api.file_upload_post(file="../test_data/TestCsv.csv")
        csv_request = CsvFileRequest(source_language="en",
                                     target_languages=["ru"],
                                     url=url,
                                     origin="python-test",
                                     saving_mode=SavingMode.Files,
                                     original_name="TestCsv",
                                     output_format=Format.Csv)
        response = api.csv_post(csv_request)
        if response.status == 202:
            print('Csv translation started')
            get_file_translation(response.id)

    # Presentation
    def testPresentation(self):
        url = file_api.file_upload_post(file="../test_data/SmallTest.pptx")
        presentation_request = PresentationFileRequest(source_language="en"
                                                       , target_languages=["ru"]
                                                       , url=url
                                                       , format=Format.Pptx
                                                       , saving_mode=SavingMode.Files
                                                       , origin="python-test"
                                                       , original_name="TestDeck"
                                                       , output_format=Format.Pptx)
        response = api.presentation_post(presentation_request)
        if response.status == 202:
            print('Presentation translation started')
            get_file_translation(response.id)

    # SRT
    def testSrtTranslation(self):
        url = file_api.file_upload_post(file="../test_data/TestSrt.srt", format=Format.Srt)
        srt_request = SrtFileRequest(source_language="en"
                                     , target_languages=["ru"]
                                     , url=url
                                     , output_format="srt")
        response = api.srt_post(srt_request)
        if response.status == 202:
            print('SRT document translation started')
            get_file_translation(response.id)

    # Markdown
    def testMarkdownTranslation(self):
        url = file_api.file_upload_post(file="../test_data/TestMarkdown.md", format=Format.Md)
        md_request = MarkdownFileRequest(source_language="en"
                                         , target_languages=["ru"]
                                         , url=url
                                         , output_format="md")
        response = api.markdown_post(md_request)
        if response.status == 202:
            print('Markdown document translation started')
            get_file_translation(response.id)

    # Image to File
    def testImageToFileTranslation(self):
        url = file_api.file_upload_post(file="../test_data/TestImage.png", format='Png')
        imgfile_request = ImageToFileRequest(source_language="en"
                                             , target_languages=["ru"]
                                             , url=url
                                             , output_format="png")
        response = api.image_to_file_post(imgfile_request)
        if response.status == 202:
            print('Image file translation started')
            get_file_translation(response.id)

    # Image to Text
    def testImageToTextTranslation(self):
        url = file_api.file_upload_post(file="../test_data/TestImage.png", format='Png')
        imgtxt_request = ImageToTextRequest(source_language="en"
                                            , target_languages=["ru"]
                                            , url=url)
        response = api.image_to_text_post(imgtxt_request)
        if response.status == 202:
            print('Image to Text translation started')
            get_file_translation(response.id)

    # HTML
    def testHtmlTranslation(self):
        url = file_api.file_upload_post(file="../test_data/TestHtml.html", format=Format.Html)
        html_request = HtmlFileRequest(source_language="en"
                                       , target_languages=["ru"]
                                       , url=url
                                       , output_format="html")
        response = api.html_post(html_request)
        if response.status == 202:
            print('HTML document translation started')
            get_file_translation(response.id)