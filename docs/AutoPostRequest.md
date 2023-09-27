# AutoPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | [default to 'Unknown']
**output_format** | **str** |  | 
**masters** | **bool** |  | [optional] [default to False]
**formatting** | **bool** |  | [optional] [default to True]
**route** | **str** |  | [optional] 
**separator** | **str** |  | [optional] 
**elements** | **List[int]** |  | [optional] 
**ranges** | [**Dict[str, WorksheetData]**](WorksheetData.md) |  | [optional] 
**short_code_list** | **Dict[str, List[List[str]]]** |  | [optional] 
**front_matter_list** | **List[List[str]]** |  | [optional] 
**source_language** | **str** |  | [default to 'en']
**target_languages** | **List[str]** |  | 
**file** | **bytearray** |  | [optional] 
**original_file_name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**origin** | **str** |  | [optional] 
**saving_mode** | **str** |  | [optional] 

## Example

```python
from groupdocs-translation-cloud.models.auto_post_request import AutoPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutoPostRequest from a JSON string
auto_post_request_instance = AutoPostRequest.from_json(json)
# print the JSON string representation of the object
print AutoPostRequest.to_json()

# convert the object into a dict
auto_post_request_dict = auto_post_request_instance.to_dict()
# create an instance of AutoPostRequest from a dict
auto_post_request_form_dict = auto_post_request.from_dict(auto_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


