# coding: utf-8

"""
    GroupDocs.Translation SDK

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 24.11.0
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from groupdocs_translation_cloud.models.worksheet_data import WorksheetData
from typing import Optional, Set
from typing_extensions import Self

class SpreadsheetFileRequest(BaseModel):
    """
    Request for spreadsheet files, like xls, xlsx, xlsm, ods
    """ # noqa: E501
    source_language: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Language of original file", alias="sourceLanguage")
    target_languages: List[StrictStr] = Field(description="List of target languages", alias="targetLanguages")
    original_file_name: Optional[StrictStr] = Field(default=None, description="Type in the file name. If null will be as request ID.", alias="originalFileName")
    url: Optional[StrictStr] = Field(default=None, description="Link to file for translation. Ignore, if \"file\" property not null")
    origin: Optional[StrictStr] = Field(default=None, description="Url or name of application using this SDK. Not required.")
    saving_mode: Optional[StrictStr] = Field(default=None, description="Toggle file saving mode for storage.  Is Files by default.", alias="savingMode")
    format: StrictStr = Field(description="Input file format")
    output_format: StrictStr = Field(description="output file format", alias="outputFormat")
    worksheets: Optional[List[StrictInt]] = Field(default=None, description="List of Worksheets to translate by sequence number (1-based index). If not present, translate all worksheets")
    ranges: Optional[Dict[str, WorksheetData]] = Field(default=None, description="Dictionary of ranges in Excel workbooks")
    __properties: ClassVar[List[str]] = ["sourceLanguage", "targetLanguages", "originalFileName", "url", "origin", "savingMode", "format", "outputFormat", "worksheets", "ranges"]

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
        if value not in set(['Unknown', 'Xls', 'Xlsx', 'Xlsm', 'Ods']):
            raise ValueError("must be one of enum values ('Unknown', 'Xls', 'Xlsx', 'Xlsm', 'Ods')")
        return value

    @field_validator('output_format')
    def output_format_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Xls', 'Xlsx', 'Xlsm', 'Xlsb', 'Html', 'Pdf', 'Xps', 'Ods', 'Md', 'Docx', 'Pptx', 'Tiff']):
            raise ValueError("must be one of enum values ('Xls', 'Xlsx', 'Xlsm', 'Xlsb', 'Html', 'Pdf', 'Xps', 'Ods', 'Md', 'Docx', 'Pptx', 'Tiff')")
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
        """Create an instance of SpreadsheetFileRequest from a JSON string"""
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
        # set to None if original_file_name (nullable) is None
        # and model_fields_set contains the field
        if self.original_file_name is None and "original_file_name" in self.model_fields_set:
            _dict['originalFileName'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if origin (nullable) is None
        # and model_fields_set contains the field
        if self.origin is None and "origin" in self.model_fields_set:
            _dict['origin'] = None

        # set to None if worksheets (nullable) is None
        # and model_fields_set contains the field
        if self.worksheets is None and "worksheets" in self.model_fields_set:
            _dict['worksheets'] = None

        # set to None if ranges (nullable) is None
        # and model_fields_set contains the field
        if self.ranges is None and "ranges" in self.model_fields_set:
            _dict['ranges'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SpreadsheetFileRequest from a dict"""
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
            "savingMode": obj.get("savingMode"),
            "format": obj.get("format") if obj.get("format") is not None else 'Xlsx',
            "outputFormat": obj.get("outputFormat"),
            "worksheets": obj.get("worksheets"),
            "ranges": dict(
                (_k, WorksheetData.from_dict(_v))
                for _k, _v in obj["ranges"].items()
            )
            if obj.get("ranges") is not None
            else None
        })
        return _obj


