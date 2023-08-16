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
from GroupDocs.Translation.Api.models.cloud_file_response import CloudFileResponse  # noqa: E501
from GroupDocs.Translation.Api.rest import ApiException

class TestCloudFileResponse(unittest.TestCase):
    """CloudFileResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CloudFileResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CloudFileResponse`
        """
        model = GroupDocs.Translation.Api.models.cloud_file_response.CloudFileResponse()  # noqa: E501
        if include_optional :
            return CloudFileResponse(
                status = 100, 
                message = '', 
                urls = {
                    'key' : GroupDocs.Translation.Api.models.url_file_info.UrlFileInfo(
                        url = '', 
                        size = 56, )
                    }, 
                scores = {
                    'key' : 1.337
                    }
            )
        else :
            return CloudFileResponse(
        )
        """

    def testCloudFileResponse(self):
        """Test CloudFileResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
