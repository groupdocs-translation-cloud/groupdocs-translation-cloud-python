# coding: utf-8

"""
    GroupDocs.Translation SDK

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 24.3.0
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr

class UrlFileInfo(BaseModel):
    """
    UrlFileInfo
    """
    url: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    __properties = ["url", "size"]

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
    def from_json(cls, json_str: str) -> UrlFileInfo:
        """Create an instance of UrlFileInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UrlFileInfo:
        """Create an instance of UrlFileInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UrlFileInfo.parse_obj(obj)

        _obj = UrlFileInfo.parse_obj({
            "url": obj.get("url"),
            "size": obj.get("size")
        })
        return _obj

