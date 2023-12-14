# coding: utf-8

"""
    GroupDocs.Translation SDK

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 23.10.5
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import groupdocs_translation_cloud
from groupdocs_translation_cloud.models.pdf_file_request import PdfFileRequest  # noqa: E501
from groupdocs_translation_cloud.rest import ApiException

class TestPdfFileRequest(unittest.TestCase):
    """PdfFileRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PdfFileRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PdfFileRequest`
        """
        model = groupdocs_translation_cloud.models.pdf_file_request.PdfFileRequest()  # noqa: E501
        if include_optional :
            return PdfFileRequest(
                source_language = 'en', 
                target_languages = [
                    ''
                    ], 
                file = 'YQ==', 
                original_file_name = '', 
                url = '', 
                origin = '', 
                saving_mode = 'Files', 
                output_format = '0', 
                preserve_formatting = True, 
                pages = [
                    56
                    ]
            )
        else :
            return PdfFileRequest(
                source_language = 'en',
                target_languages = [
                    ''
                    ],
                output_format = '0',
        )
        """

    def testPdfFileRequest(self):
        """Test PdfFileRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()