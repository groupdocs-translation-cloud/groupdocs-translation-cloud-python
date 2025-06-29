# coding: utf-8

"""
    GroupDocs.Translation SDK

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 25.3.0
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class MediaToFileRequest(BaseModel):
    """
    MediaToFileRequest
    """ # noqa: E501
    source_language: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Language of original file", alias="sourceLanguage")
    target_languages: List[StrictStr] = Field(description="List of target languages", alias="targetLanguages")
    original_file_name: Optional[StrictStr] = Field(default=None, description="Type in the file name. If null will be as request ID.", alias="originalFileName")
    url: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Link to file for translation. Ignore, if \"file\" property not null")
    origin: Optional[StrictStr] = Field(default=None, description="Url or name of the application using this SDK. Not required.")
    is_need_alignment: Optional[StrictBool] = Field(default=None, description="Do result formating like the source. This option needs more expensive requests.", alias="isNeedAlignment")
    translation_dictionary: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="Set a specific translation between source and target words.", alias="translationDictionary")
    saving_mode: Optional[StrictStr] = Field(default=None, description="Toggle file saving mode for storage.  Is Files by default.", alias="savingMode")
    format: StrictStr = Field(description="Input file format")
    output_format: Annotated[str, Field(min_length=1, strict=True)] = Field(description="output file format", alias="outputFormat")
    fragments: Optional[List[StrictStr]] = Field(default=None, description="Time fragments that require translation")
    interval: Optional[StrictInt] = Field(default=None, description="Define intervals of timestampts in the resulting file")
    route: Optional[StrictStr] = Field(default=None, description="endpoints route")
    __properties: ClassVar[List[str]] = ["sourceLanguage", "targetLanguages", "originalFileName", "url", "origin", "isNeedAlignment", "translationDictionary", "savingMode", "format", "outputFormat", "fragments", "interval", "route"]

    @field_validator('saving_mode')
    def saving_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Files', 'Archive', 'Both']):
            raise ValueError("must be one of enum values ('Files', 'Archive', 'Both')")
        return value

    @field_validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Unknown', 'Mp3', 'Wav', 'Flac', 'M4a', 'Aac', 'Wma', 'Flv', 'Mkv', 'Webm', 'Avi', 'Mov', 'Wmv', 'Rm', 'Mpg']):
            raise ValueError("must be one of enum values ('Unknown', 'Mp3', 'Wav', 'Flac', 'M4a', 'Aac', 'Wma', 'Flv', 'Mkv', 'Webm', 'Avi', 'Mov', 'Wmv', 'Rm', 'Mpg')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MediaToFileRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if original_file_name (nullable) is None
        # and model_fields_set contains the field
        if self.original_file_name is None and "original_file_name" in self.model_fields_set:
            _dict['originalFileName'] = None

        # set to None if origin (nullable) is None
        # and model_fields_set contains the field
        if self.origin is None and "origin" in self.model_fields_set:
            _dict['origin'] = None

        # set to None if translation_dictionary (nullable) is None
        # and model_fields_set contains the field
        if self.translation_dictionary is None and "translation_dictionary" in self.model_fields_set:
            _dict['translationDictionary'] = None

        # set to None if fragments (nullable) is None
        # and model_fields_set contains the field
        if self.fragments is None and "fragments" in self.model_fields_set:
            _dict['fragments'] = None

        # set to None if route (nullable) is None
        # and model_fields_set contains the field
        if self.route is None and "route" in self.model_fields_set:
            _dict['route'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MediaToFileRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sourceLanguage": obj.get("sourceLanguage") if obj.get("sourceLanguage") is not None else 'en',
            "targetLanguages": obj.get("targetLanguages"),
            "originalFileName": obj.get("originalFileName"),
            "url": obj.get("url"),
            "origin": obj.get("origin"),
            "isNeedAlignment": obj.get("isNeedAlignment"),
            "translationDictionary": obj.get("translationDictionary"),
            "savingMode": obj.get("savingMode"),
            "format": obj.get("format") if obj.get("format") is not None else 'Mp3',
            "outputFormat": obj.get("outputFormat"),
            "fragments": obj.get("fragments"),
            "interval": obj.get("interval"),
            "route": obj.get("route")
        })
        return _obj


