# coding: utf-8
# """
# --------------------------------------------------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_helper.py">
#    Copyright (c) 2020 GroupDocs.Translation for Cloud
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
import sys
sys.path.append('../')
from shutil import copy2
from groupdocstranslationcloud.configuration import Configuration
from groupdocstranslationcloud.api_client import ApiClient as Client
from groupdocstranslationcloud.api.translation_api import TranslationApi
from groupdocstranslationcloud.api.storage_api import StorageApi


class TestHelper(object):

    configuration = Configuration(
        client_secret="",
        client_id="",
        basePath="https://api.groupdocs.cloud/v1.0/translation",
        authPath="https://api.groupdocs.cloud/connect/token",
        debug=False)

    if not configuration.client_secret or not configuration.client_id:
        raise Exception("Setup client_id and client_secret in TestsHelper -> configuration.")

    client = Client(configuration)
    translation = TranslationApi(client)
    storage = StorageApi(client)

    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    test_src = os.path.join(parent_dir, 'testdata')
    test_dst = os.path.join(parent_dir, 'testresult')
    folder = 'TranslationTestDoc'

    @classmethod
    def get_folder(cls):
        return cls.folder

    @classmethod
    def get_local_folder(cls):
        return cls.test_src

    @classmethod
    def get_local_dest_folder(cls):
        return cls.test_dst

    @classmethod
    def upload_file(cls, file_name):
        res = cls.storage.upload_file(os.path.join(cls.folder, file_name), os.path.join(cls.test_src, file_name))
        return res

    @classmethod
    def download_file(cls, path):
        response = cls.storage.download_file(path)
        return response

    @classmethod
    def get_file_size(cls, file_name):
        return os.path.getsize(os.path.join(cls.test_src, file_name))

    @classmethod
    def move_file(cls, src_file, dst_file):
        if os.path.isfile(src_file):
            copy2(src_file, dst_file)
            os.remove(src_file)
