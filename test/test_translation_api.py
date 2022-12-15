# coding: utf-8
# """
# --------------------------------------------------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_translation_api.py">
#    Copyright (c) 2022 GroupDocs.Translation for Cloud
#  </copyright>
#  <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# --------------------------------------------------------------------------------------------------------------------
# """

from __future__ import absolute_import


import os
import unittest
import sys
import shutil

from groupdocstranslationcloud.api.storage_api import StorageApi

sys.path.append('../')
import groupdocstranslationcloud.models
from groupdocstranslationcloud.models import translate_text, translate_document, translate_hugo
from groupdocstranslationcloud.rest import ApiException
from test_helper import TestHelper

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

class TestTranslationApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = TestHelper.translation
        cls.storageApi = TestHelper.storage

    ###############################################################
    #                          Translation tests
    ###############################################################

    def test_text_translation(self):
        pair = "en-fr"
        text = "Welcome to Paris"
        try:
            translator = translate_text.TranslateText(pair, text)
            request = translator.to_string()
            response = self.api.post_translate_text(request)
            print(response)
            self.assertEqual(response.status, "ok")
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

    def test_document_translation(self):
        pair = "en-fr"
        _format = "hugo"
        outformat = "hugo"
        storage = "First Storage"
        name = "hugo_test_file.md"
        folder = "TranslationTestDoc"
        savepath = "TranslationTestDoc"
        savefile = "translated_hugo_test_file.md"
        masters = False
        elements = None

        frontMatterDict = {0: [["title"], ["frontmatter", "title" ], ["frontmatter", "description"]]}
        shortCodeDict = {0: ["1","3"]}

        src = TestHelper.get_local_folder() + "/" + name
        dst = TestHelper.get_folder() + "/" + name
        dst_trs = TestHelper.get_folder() + "/" + savefile
        src_trs = TestHelper.get_local_folder() + "/" + savefile

        if self.storageApi.object_exists(dst).to_dict()['exists']:
            print(name, 'already exists')
        else:
            result = self.storageApi.upload_file(dst, src).to_dict()
            if len(result['errors']) == 0:
                print(result['uploaded'], "was uploaded")
            else:
                print(name, 'wasn\'t uploaded')
        try:
            translator = translate_document.TranslateDocument(pair, _format, outformat, storage, name, folder, savepath, savefile, masters, elements, ",", shortCodeDict, frontMatterDict)
            request = translator.to_string()
            response = self.api.post_translate_document(request)
            print(response)
            self.assertEqual(response.status, "ok")
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

        result = self.storageApi.download_file(dst_trs)
        if result:
            print(savefile, "was downloaded")
        else:
            print(savefile, 'wasn\'t downloaded')

        shutil.move(result, src_trs)

        self.storageApi.delete_file(dst)
        self.storageApi.delete_file(dst_trs)

    def test_hugo_translation(self):
        storage = "First Storage"
        name = "hugo_test_file.md"
        folder = ""

        try:
            translator = translate_hugo.TranslateHugo(name, folder, storage)
            request = translator.to_string()
            response = self.api.post_translate_hugo(request)
            print(response)
            self.assertEqual(response.status, "ok")
        except ApiException as ex:
            print("Exception")
            print("Info: " + str(ex))
            raise ex

if __name__ == '__main__':
    unittest.main()
