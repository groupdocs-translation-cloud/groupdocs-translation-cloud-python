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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictBytes, StrictInt, StrictStr, conlist, constr, validator

class OcrFileRequest(BaseModel):
    """
    OcrFileRequest
    """
    source_language: constr(strict=True, min_length=1) = Field(..., alias="sourceLanguage", description="Language of original file")
    target_languages: conlist(StrictStr) = Field(..., alias="targetLanguages", description="List of target languages")
    file: Optional[Union[StrictBytes, StrictStr]] = Field(None, description="File as byte array")
    original_file_name: Optional[StrictStr] = Field(None, alias="originalFileName", description="Type in the file name. If null will be as request ID.")
    url: Optional[StrictStr] = Field(None, description="Link to file for translation. Ignore, if \"file\" property not null")
    origin: Optional[StrictStr] = Field(None, description="Url or name of application using this SDK. Not required.")
    saving_mode: Optional[StrictStr] = Field(None, alias="savingMode", description="Toggle file saving mode for storage.  Is Files by default.")
    format: Optional[StrictStr] = Field('Unknown', description="Original file format")
    ocrformat: StrictStr = Field(..., description="File format after recognition")
    output_format: constr(strict=True, min_length=1) = Field(..., alias="outputFormat", description="output file format")
    rotation_angle: Optional[StrictInt] = Field(None, alias="rotationAngle", description="Left to write angle to rotate scanned image / pdf")
    formatting: Optional[StrictBool] = Field(True, description="If document's formatting should be preserved, default true")
    route: Optional[StrictStr] = Field(None, description="endpoints route")
    pages: Optional[conlist(StrictInt)] = Field(None, description="List of pages to translate for scanned pdf")
    __properties = ["sourceLanguage", "targetLanguages", "file", "originalFileName", "url", "origin", "savingMode", "format", "ocrformat", "outputFormat", "rotationAngle", "formatting", "route", "pages"]

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

        if value not in ('Unknown', 'Bmp', 'Jpg', 'Png', 'Svg', 'Gif', 'Pdf'):
            raise ValueError("must be one of enum values ('Unknown', 'Bmp', 'Jpg', 'Png', 'Svg', 'Gif', 'Pdf')")
        return value

    @validator('ocrformat')
    def ocrformat_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Pdf', 'Xlsx', 'Csv'):
            raise ValueError("must be one of enum values ('Pdf', 'Xlsx', 'Csv')")
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
    def from_json(cls, json_str: str) -> OcrFileRequest:
        """Create an instance of OcrFileRequest from a JSON string"""
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

        # set to None if route (nullable) is None
        # and __fields_set__ contains the field
        if self.route is None and "route" in self.__fields_set__:
            _dict['route'] = None

        # set to None if pages (nullable) is None
        # and __fields_set__ contains the field
        if self.pages is None and "pages" in self.__fields_set__:
            _dict['pages'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OcrFileRequest:
        """Create an instance of OcrFileRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OcrFileRequest.parse_obj(obj)

        _obj = OcrFileRequest.parse_obj({
            "source_language": obj.get("sourceLanguage") if obj.get("sourceLanguage") is not None else 'en',
            "target_languages": obj.get("targetLanguages"),
            "file": obj.get("file"),
            "original_file_name": obj.get("originalFileName"),
            "url": obj.get("url"),
            "origin": obj.get("origin"),
            "saving_mode": obj.get("savingMode"),
            "format": obj.get("format") if obj.get("format") is not None else 'Unknown',
            "ocrformat": obj.get("ocrformat") if obj.get("ocrformat") is not None else 'Pdf',
            "output_format": obj.get("outputFormat"),
            "rotation_angle": obj.get("rotationAngle"),
            "formatting": obj.get("formatting") if obj.get("formatting") is not None else True,
            "route": obj.get("route"),
            "pages": obj.get("pages")
        })
        return _obj

