# MediaToFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** | Language of original file | [default to 'en']
**target_languages** | **List[str]** | List of target languages | 
**original_file_name** | **str** | Type in the file name. If null will be as request ID. | [optional] 
**url** | **str** | Link to file for translation. Ignore, if \&quot;file\&quot; property not null | [optional] 
**origin** | **str** | Url or name of application using this SDK. Not required. | [optional] 
**saving_mode** | **str** | Toggle file saving mode for storage.  Is Files by default. | [optional] 
**format** | **str** | Input file format | [default to 'Mp3']
**output_format** | **str** | output file format | 
**fragments** | **List[str]** | Time fragments that require translation | [optional] 
**interval** | **int** | Define intervals of timestampts in the resulting file | [optional] 
**route** | **str** | endpoints route | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.media_to_file_request import MediaToFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MediaToFileRequest from a JSON string
media_to_file_request_instance = MediaToFileRequest.from_json(json)
# print the JSON string representation of the object
print(MediaToFileRequest.to_json())

# convert the object into a dict
media_to_file_request_dict = media_to_file_request_instance.to_dict()
# create an instance of MediaToFileRequest from a dict
media_to_file_request_from_dict = MediaToFileRequest.from_dict(media_to_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


