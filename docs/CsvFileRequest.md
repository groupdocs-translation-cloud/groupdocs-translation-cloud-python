# CsvFileRequest

Request for comma / tab separated files like csv, tsv

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** | Language of original file | [default to 'en']
**target_languages** | **List[str]** | List of target languages | 
**original_file_name** | **str** | Type in the file name. If null will be as request ID. | [optional] 
**url** | **str** | Link to file for translation. Ignore, if \&quot;file\&quot; property not null | 
**origin** | **str** | Url or name of the application using this SDK. Not required. | [optional] 
**is_need_alignment** | **bool** | Do result formating like the source. This option needs more expensive requests. | [optional] 
**translation_dictionary** | **Dict[str, Optional[str]]** | Set a specific translation between source and target words. | [optional] 
**saving_mode** | **str** | Toggle file saving mode for storage.  Is Files by default. | [optional] 
**format** | **str** | Input file format | [optional] [default to 'Csv']
**output_format** | **str** | output file format | 
**separator** | **str** | Separator in files | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.csv_file_request import CsvFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CsvFileRequest from a JSON string
csv_file_request_instance = CsvFileRequest.from_json(json)
# print the JSON string representation of the object
print(CsvFileRequest.to_json())

# convert the object into a dict
csv_file_request_dict = csv_file_request_instance.to_dict()
# create an instance of CsvFileRequest from a dict
csv_file_request_from_dict = CsvFileRequest.from_dict(csv_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


