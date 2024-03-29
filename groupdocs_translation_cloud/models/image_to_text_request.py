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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictBytes, StrictInt, StrictStr, conlist, constr, validator

class ImageToTextRequest(BaseModel):
    """
    ImageToTextRequest
    """
    format: Optional[StrictStr] = Field('Unknown', description="Originnal file format")
    source: Optional[constr(strict=True, min_length=1)] = Field('en', description="Language of original file")
    targets: Optional[conlist(StrictStr)] = Field(None, description="List of target languages")
    file: Optional[Union[StrictBytes, StrictStr]] = Field(None, description="File for translation")
    url: Optional[StrictStr] = Field(None, description="Link to file for translation")
    rotate: Optional[StrictInt] = Field(None, description="Left to write angle to rotate scanned image / pdf")
    ishandwritten: Optional[StrictBool] = Field(None, description="is handwritten text")
    origin: Optional[StrictStr] = Field(None, description="for analysis only")
    route: Optional[StrictStr] = Field(None, description="endpoints route")
    __properties = ["format", "source", "targets", "file", "url", "rotate", "ishandwritten", "origin", "route"]

    @validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Unknown', 'Bmp', 'Jpg', 'Png', 'Svg', 'Gif', 'Pdf'):
            raise ValueError("must be one of enum values ('Unknown', 'Bmp', 'Jpg', 'Png', 'Svg', 'Gif', 'Pdf')")
        return value

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
    def from_json(cls, json_str: str) -> ImageToTextRequest:
        """Create an instance of ImageToTextRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if file (nullable) is None
        # and __fields_set__ contains the field
        if self.file is None and "file" in self.__fields_set__:
            _dict['file'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if origin (nullable) is None
        # and __fields_set__ contains the field
        if self.origin is None and "origin" in self.__fields_set__:
            _dict['origin'] = None

        # set to None if route (nullable) is None
        # and __fields_set__ contains the field
        if self.route is None and "route" in self.__fields_set__:
            _dict['route'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ImageToTextRequest:
        """Create an instance of ImageToTextRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ImageToTextRequest.parse_obj(obj)

        _obj = ImageToTextRequest.parse_obj({
            "format": obj.get("format") if obj.get("format") is not None else 'Unknown',
            "source": obj.get("source") if obj.get("source") is not None else 'en',
            "targets": obj.get("targets"),
            "file": obj.get("file"),
            "url": obj.get("url"),
            "rotate": obj.get("rotate"),
            "ishandwritten": obj.get("ishandwritten"),
            "origin": obj.get("origin"),
            "route": obj.get("route")
        })
        return _obj

