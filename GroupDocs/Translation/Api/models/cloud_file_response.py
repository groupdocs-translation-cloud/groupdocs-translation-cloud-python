# coding: utf-8

"""
    GroupDocs.Translation.ApiGateway.Web

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Dict, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from GroupDocs.Translation.Api.models.http_status_code import HttpStatusCode
from GroupDocs.Translation.Api.models.url_file_info import UrlFileInfo

class CloudFileResponse(BaseModel):
    """
    CloudFileResponse
    """
    status: Optional[HttpStatusCode] = None
    message: Optional[StrictStr] = None
    urls: Optional[Dict[str, UrlFileInfo]] = None
    scores: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = None
    __properties = ["status", "message", "urls", "scores"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CloudFileResponse:
        """Create an instance of CloudFileResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in urls (dict)
        _field_dict = {}
        if self.urls:
            for _key in self.urls:
                if self.urls[_key]:
                    _field_dict[_key] = self.urls[_key].to_dict()
            _dict['urls'] = _field_dict
        # set to None if message (nullable) is None
        # and __fields_set__ contains the field
        if self.message is None and "message" in self.__fields_set__:
            _dict['message'] = None

        # set to None if urls (nullable) is None
        # and __fields_set__ contains the field
        if self.urls is None and "urls" in self.__fields_set__:
            _dict['urls'] = None

        # set to None if scores (nullable) is None
        # and __fields_set__ contains the field
        if self.scores is None and "scores" in self.__fields_set__:
            _dict['scores'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CloudFileResponse:
        """Create an instance of CloudFileResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CloudFileResponse.parse_obj(obj)

        _obj = CloudFileResponse.parse_obj({
            "status": obj.get("status"),
            "message": obj.get("message"),
            "urls": dict(
                (_k, UrlFileInfo.from_dict(_v))
                for _k, _v in obj.get("urls").items()
            )
            if obj.get("urls") is not None
            else None,
            "scores": obj.get("scores")
        })
        return _obj

