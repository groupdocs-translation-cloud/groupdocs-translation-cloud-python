# coding: utf-8

"""
    GroupDocs.Translation.ApiGateway.Web

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.cloud_text_response import CloudTextResponse  # noqa: E501
from GroupDocs.Translation.Api.rest import ApiException

class TestCloudTextResponse(unittest.TestCase):
    """CloudTextResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CloudTextResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CloudTextResponse`
        """
        model = GroupDocs.Translation.Api.models.cloud_text_response.CloudTextResponse()  # noqa: E501
        if include_optional :
            return CloudTextResponse(
                status = 100, 
                message = '', 
                translations = {
                    'key' : [
                        ''
                        ]
                    }
            )
        else :
            return CloudTextResponse(
        )
        """

    def testCloudTextResponse(self):
        """Test CloudTextResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
