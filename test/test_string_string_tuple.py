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
from groupdocs_translation_cloud.models.string_string_tuple import StringStringTuple  # noqa: E501
from groupdocs_translation_cloud.rest import ApiException

class TestStringStringTuple(unittest.TestCase):
    """StringStringTuple unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StringStringTuple
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StringStringTuple`
        """
        model = groupdocs_translation_cloud.models.string_string_tuple.StringStringTuple()  # noqa: E501
        if include_optional :
            return StringStringTuple(
                item1 = '', 
                item2 = ''
            )
        else :
            return StringStringTuple(
        )
        """

    def testStringStringTuple(self):
        """Test StringStringTuple"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
