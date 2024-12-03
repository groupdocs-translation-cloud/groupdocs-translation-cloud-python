# coding: utf-8

"""
    GroupDocs.Translation SDK

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 24.11.0
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from groupdocs_translation_cloud.models.xml_file_request import XmlFileRequest

class TestXmlFileRequest(unittest.TestCase):
    """XmlFileRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> XmlFileRequest:
        """Test XmlFileRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `XmlFileRequest`
        """
        model = XmlFileRequest()
        if include_optional:
            return XmlFileRequest(
                source_language = 'en',
                target_languages = [
                    ''
                    ],
                file = 'YQ==',
                original_file_name = '',
                url = '',
                origin = '',
                saving_mode = 'Files',
                ignore_list = [
                    ''
                    ],
                is_white_list = True
            )
        else:
            return XmlFileRequest(
                source_language = 'en',
                target_languages = [
                    ''
                    ],
        )
        """

    def testXmlFileRequest(self):
        """Test XmlFileRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
