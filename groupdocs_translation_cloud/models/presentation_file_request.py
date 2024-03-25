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

class PresentationFileRequest(BaseModel):
    """
    Request for presentation files like ppt, pptx, pptm, odp
    """
    source_language: Optional[constr(strict=True, min_length=1)] = Field('en', alias="sourceLanguage", description="Language of original file")
    target_languages: Optional[conlist(StrictStr)] = Field(None, alias="targetLanguages", description="List of target languages")
    file: Optional[Union[StrictBytes, StrictStr]] = Field(None, description="File as byte array")
    original_file_name: Optional[StrictStr] = Field(None, alias="originalFileName", description="Type in the file name. If null will be as request ID.")
    url: Optional[StrictStr] = Field(None, description="Link to file for translation. Ignore, if \"file\" property not null")
    origin: Optional[StrictStr] = Field(None, description="Url or name of application using this SDK. Not required.")
    saving_mode: Optional[StrictStr] = Field(None, alias="savingMode", description="Toggle file saving mode for storage.  Is Files by default.")
    format: Optional[StrictStr] = Field('Pptx', description="Input file format")
    output_format: Optional[constr(strict=True, min_length=1)] = Field(None, alias="outputFormat", description="Output file format")
    masters: Optional[StrictBool] = Field(False, description="If translate master slides")
    slides: Optional[conlist(StrictInt)] = Field(None, description="List of slides to translate (1-based index). If not present, translate all slides")
    __properties = ["sourceLanguage", "targetLanguages", "file", "originalFileName", "url", "origin", "savingMode", "format", "outputFormat", "masters", "slides"]

    @validator('saving_mode')
    def saving_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Files', 'Archive', 'Both'):
            raise ValueError("must be one of enum values ('Files', 'Archive', 'Both')")
        return value

    @validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Unknown', 'Ppt', 'Pptx', 'Pptm', 'Odp'):
            raise ValueError("must be one of enum values ('Unknown', 'Ppt', 'Pptx', 'Pptm', 'Odp')")
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
    def from_json(cls, json_str: str) -> PresentationFileRequest:
        """Create an instance of PresentationFileRequest from a JSON string"""
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

        # set to None if original_file_name (nullable) is None
        # and __fields_set__ contains the field
        if self.original_file_name is None and "original_file_name" in self.__fields_set__:
            _dict['originalFileName'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if origin (nullable) is None
        # and __fields_set__ contains the field
        if self.origin is None and "origin" in self.__fields_set__:
            _dict['origin'] = None

        # set to None if slides (nullable) is None
        # and __fields_set__ contains the field
        if self.slides is None and "slides" in self.__fields_set__:
            _dict['slides'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PresentationFileRequest:
        """Create an instance of PresentationFileRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PresentationFileRequest.parse_obj(obj)

        _obj = PresentationFileRequest.parse_obj({
            "source_language": obj.get("sourceLanguage") if obj.get("sourceLanguage") is not None else 'en',
            "target_languages": obj.get("targetLanguages"),
            "file": obj.get("file"),
            "original_file_name": obj.get("originalFileName"),
            "url": obj.get("url"),
            "origin": obj.get("origin"),
            "saving_mode": obj.get("savingMode"),
            "format": obj.get("format") if obj.get("format") is not None else 'Pptx',
            "output_format": obj.get("outputFormat"),
            "masters": obj.get("masters") if obj.get("masters") is not None else False,
            "slides": obj.get("slides")
        })
        return _obj

