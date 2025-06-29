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
from groupdocs_translation_cloud.models.worksheet_data import WorksheetData
from typing import Optional, Set
from typing_extensions import Self

class CloudFileRequest(BaseModel):
    """
    CloudFileRequest
    """ # noqa: E501
    format: Optional[StrictStr] = Field(default=None, description="\"doc(x|m)\" if Word document, \"xls(x|m)\" if Excel workbook")
    out_format: Optional[StrictStr] = Field(default=None, description="output file format", alias="outFormat")
    request_id: Optional[StrictStr] = Field(default=None, description="id of request", alias="requestId")
    ids: Optional[List[StrictInt]] = Field(default=None, description="Language pairs to translate")
    summarized: Optional[StrictBool] = Field(default=None, description="If summarization required")
    url: Optional[StrictStr] = Field(default=None, description="Link to file for translation")
    size: Optional[StrictInt] = Field(default=None, description="File size")
    masters: Optional[StrictBool] = Field(default=None, description="If translate master slides")
    formatting: Optional[StrictBool] = Field(default=None, description="If document's formatting should be preserved, default true")
    is_need_alignment: Optional[StrictBool] = Field(default=None, description="If need result like source formated text.", alias="isNeedAlignment")
    translation_dictionary: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="Set a specific translation between source and target words.", alias="translationDictionary")
    origin: Optional[StrictStr] = Field(default=None, description="for analysis only")
    elements: Optional[List[StrictInt]] = Field(default=None, description="List of slides to translate")
    ranges: Optional[Dict[str, WorksheetData]] = Field(default=None, description="Dictionary of ranges in Excel workbooks")
    short_code_dict: Optional[Dict[str, Optional[List[StrictStr]]]] = Field(default=None, description="Dictiory of short code names and parameters names to translate", alias="shortCodeDict")
    front_matter_list: Optional[List[List[StrictStr]]] = Field(default=None, description="Dictionary where key is zero-based front matter index and value is list of lists of front matter paths", alias="frontMatterList")
    original_file_name: Optional[StrictStr] = Field(default=None, description="Original name of file", alias="originalFileName")
    separator: Optional[StrictStr] = Field(default=None, description="Separator in files")
    is_paid: Optional[StrictBool] = Field(default=None, description="Set true if paid user", alias="isPaid")
    saving_mode: Optional[StrictStr] = Field(default=None, description="Toggle files saving mode", alias="savingMode")
    details: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="Details of the requests. Using for e2e tracking")
    model: Optional[StrictStr] = Field(default=None, description="Text array to translate")
    __properties: ClassVar[List[str]] = ["format", "outFormat", "requestId", "ids", "summarized", "url", "size", "masters", "formatting", "isNeedAlignment", "translationDictionary", "origin", "elements", "ranges", "shortCodeDict", "frontMatterList", "originalFileName", "separator", "isPaid", "savingMode", "details", "model"]

    @field_validator('saving_mode')
    def saving_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Files', 'Archive', 'Both']):
            raise ValueError("must be one of enum values ('Files', 'Archive', 'Both')")
        return value

    @field_validator('model')
    def model_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['General', 'Slang', 'Classification']):
            raise ValueError("must be one of enum values ('General', 'Slang', 'Classification')")
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
        """Create an instance of CloudFileRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in ranges (dict)
        _field_dict = {}
        if self.ranges:
            for _key in self.ranges:
                if self.ranges[_key]:
                    _field_dict[_key] = self.ranges[_key].to_dict()
            _dict['ranges'] = _field_dict
        # set to None if format (nullable) is None
        # and model_fields_set contains the field
        if self.format is None and "format" in self.model_fields_set:
            _dict['format'] = None

        # set to None if out_format (nullable) is None
        # and model_fields_set contains the field
        if self.out_format is None and "out_format" in self.model_fields_set:
            _dict['outFormat'] = None

        # set to None if request_id (nullable) is None
        # and model_fields_set contains the field
        if self.request_id is None and "request_id" in self.model_fields_set:
            _dict['requestId'] = None

        # set to None if ids (nullable) is None
        # and model_fields_set contains the field
        if self.ids is None and "ids" in self.model_fields_set:
            _dict['ids'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if translation_dictionary (nullable) is None
        # and model_fields_set contains the field
        if self.translation_dictionary is None and "translation_dictionary" in self.model_fields_set:
            _dict['translationDictionary'] = None

        # set to None if origin (nullable) is None
        # and model_fields_set contains the field
        if self.origin is None and "origin" in self.model_fields_set:
            _dict['origin'] = None

        # set to None if elements (nullable) is None
        # and model_fields_set contains the field
        if self.elements is None and "elements" in self.model_fields_set:
            _dict['elements'] = None

        # set to None if ranges (nullable) is None
        # and model_fields_set contains the field
        if self.ranges is None and "ranges" in self.model_fields_set:
            _dict['ranges'] = None

        # set to None if short_code_dict (nullable) is None
        # and model_fields_set contains the field
        if self.short_code_dict is None and "short_code_dict" in self.model_fields_set:
            _dict['shortCodeDict'] = None

        # set to None if front_matter_list (nullable) is None
        # and model_fields_set contains the field
        if self.front_matter_list is None and "front_matter_list" in self.model_fields_set:
            _dict['frontMatterList'] = None

        # set to None if original_file_name (nullable) is None
        # and model_fields_set contains the field
        if self.original_file_name is None and "original_file_name" in self.model_fields_set:
            _dict['originalFileName'] = None

        # set to None if separator (nullable) is None
        # and model_fields_set contains the field
        if self.separator is None and "separator" in self.model_fields_set:
            _dict['separator'] = None

        # set to None if details (nullable) is None
        # and model_fields_set contains the field
        if self.details is None and "details" in self.model_fields_set:
            _dict['details'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CloudFileRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "format": obj.get("format"),
            "outFormat": obj.get("outFormat"),
            "requestId": obj.get("requestId"),
            "ids": obj.get("ids"),
            "summarized": obj.get("summarized"),
            "url": obj.get("url"),
            "size": obj.get("size"),
            "masters": obj.get("masters"),
            "formatting": obj.get("formatting"),
            "isNeedAlignment": obj.get("isNeedAlignment"),
            "translationDictionary": obj.get("translationDictionary"),
            "origin": obj.get("origin"),
            "elements": obj.get("elements"),
            "ranges": dict(
                (_k, WorksheetData.from_dict(_v))
                for _k, _v in obj["ranges"].items()
            )
            if obj.get("ranges") is not None
            else None,
            "shortCodeDict": obj.get("shortCodeDict"),
            "frontMatterList": obj.get("frontMatterList"),
            "originalFileName": obj.get("originalFileName"),
            "separator": obj.get("separator"),
            "isPaid": obj.get("isPaid"),
            "savingMode": obj.get("savingMode"),
            "details": obj.get("details"),
            "model": obj.get("model")
        })
        return _obj


