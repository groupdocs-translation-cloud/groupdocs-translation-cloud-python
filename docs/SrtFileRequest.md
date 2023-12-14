# SrtFileRequest


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

## Example

```python
from groupdocs_translation_cloud.models.srt_file_request import SrtFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SrtFileRequest from a JSON string
srt_file_request_instance = SrtFileRequest.from_json(json)
# print the JSON string representation of the object
print SrtFileRequest.to_json()

# convert the object into a dict
srt_file_request_dict = srt_file_request_instance.to_dict()
# create an instance of SrtFileRequest from a dict
srt_file_request_form_dict = srt_file_request.from_dict(srt_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


