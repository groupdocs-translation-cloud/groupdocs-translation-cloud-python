# SpreadsheetFileRequest

Request for spreadsheet files, like xls, xlsx, xlsm, ods

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** | Language of original file | [default to 'en']
**target_languages** | **List[str]** | List of target languages | 
**original_file_name** | **str** | Type in the file name. If null will be as request ID. | [optional] 
**url** | **str** | Link to file for translation. Ignore, if \&quot;file\&quot; property not null | [optional] 
**origin** | **str** | Url or name of application using this SDK. Not required. | [optional] 
**saving_mode** | **str** | Toggle file saving mode for storage.  Is Files by default. | [optional] 
**format** | **str** | Input file format | [default to 'Xlsx']
**output_format** | **str** | output file format | 
**worksheets** | **List[int]** | List of Worksheets to translate by sequence number (1-based index). If not present, translate all worksheets | [optional] 
**ranges** | [**Dict[str, WorksheetData]**](WorksheetData.md) | Dictionary of ranges in Excel workbooks | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.spreadsheet_file_request import SpreadsheetFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SpreadsheetFileRequest from a JSON string
spreadsheet_file_request_instance = SpreadsheetFileRequest.from_json(json)
# print the JSON string representation of the object
print(SpreadsheetFileRequest.to_json())

# convert the object into a dict
spreadsheet_file_request_dict = spreadsheet_file_request_instance.to_dict()
# create an instance of SpreadsheetFileRequest from a dict
spreadsheet_file_request_from_dict = SpreadsheetFileRequest.from_dict(spreadsheet_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


