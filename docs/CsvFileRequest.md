# CsvFileRequest

Request for comma / tab separated files like csv, tsv

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** | Language of original file | [default to 'en']
**target_languages** | **List[str]** | List of target languages | 
**file** | **bytearray** | File as byte array | [optional] 
**original_file_name** | **str** | Type in the file name. If null will be as request ID. | [optional] 
**url** | **str** | Link to file for translation. Ignore, if \&quot;file\&quot; property not null | [optional] 
**origin** | **str** | Url or name of application using this SDK. Not required. | [optional] 
**saving_mode** | **str** | Toggle file saving mode for storage.  Is Files by default. | [optional] 
**format** | **str** | Input file format | [optional] [default to 'Csv']
**out_format** | **str** | output file format | 
**separator** | **str** | Separator in files | [optional] 

## Example

```python
from GroupDocs.Translation.Api.models.csv_file_request import CsvFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CsvFileRequest from a JSON string
csv_file_request_instance = CsvFileRequest.from_json(json)
# print the JSON string representation of the object
print CsvFileRequest.to_json()

# convert the object into a dict
csv_file_request_dict = csv_file_request_instance.to_dict()
# create an instance of CsvFileRequest from a dict
csv_file_request_form_dict = csv_file_request.from_dict(csv_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


