# HtmlFileRequest

Request for HTML files

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** | Language of original file | [optional] [default to 'en']
**target_languages** | **List[str]** | List of target languages | [optional] 
**original_file_name** | **str** | Type in the file name. If null will be as request ID. | [optional] 
**url** | **str** | Link to file for translation. Ignore, if \&quot;file\&quot; property not null | [optional] 
**origin** | **str** | Url or name of application using this SDK. Not required. | [optional] 
**saving_mode** | **str** | Toggle file saving mode for storage.  Is Files by default. | [optional] 
**output_format** | **str** | output file format | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.html_file_request import HtmlFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HtmlFileRequest from a JSON string
html_file_request_instance = HtmlFileRequest.from_json(json)
# print the JSON string representation of the object
print(HtmlFileRequest.to_json())

# convert the object into a dict
html_file_request_dict = html_file_request_instance.to_dict()
# create an instance of HtmlFileRequest from a dict
html_file_request_from_dict = HtmlFileRequest.from_dict(html_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


