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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from GroupDocs.Translation.Api.models.http_status_code import HttpStatusCode

class CloudTextResponse(BaseModel):
    """
    CloudTextResponse
    """
    status: Optional[HttpStatusCode] = None
    message: Optional[StrictStr] = Field(None, description="If file was translated correctly or text of error")
    translations: Optional[Dict[str, conlist(StrictStr)]] = Field(None, description="Translated texts")
    __properties = ["status", "message", "translations"]

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
    def from_json(cls, json_str: str) -> CloudTextResponse:
        """Create an instance of CloudTextResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if message (nullable) is None
        # and __fields_set__ contains the field
        if self.message is None and "message" in self.__fields_set__:
            _dict['message'] = None

        # set to None if translations (nullable) is None
        # and __fields_set__ contains the field
        if self.translations is None and "translations" in self.__fields_set__:
            _dict['translations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CloudTextResponse:
        """Create an instance of CloudTextResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CloudTextResponse.parse_obj(obj)

        _obj = CloudTextResponse.parse_obj({
            "status": obj.get("status"),
            "message": obj.get("message"),
            "translations": obj.get("translations")
        })
        return _obj

