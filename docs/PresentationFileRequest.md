# PresentationFileRequest

Request for presentation files like ppt, pptx, pptm, odp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** | Language of original file | [optional] [default to 'en']
**target_languages** | **List[str]** | List of target languages | [optional] 
**original_file_name** | **str** | Type in the file name. If null will be as request ID. | [optional] 
**url** | **str** | Link to file for translation. Ignore, if \&quot;file\&quot; property not null | [optional] 
**origin** | **str** | Url or name of application using this SDK. Not required. | [optional] 
**saving_mode** | **str** | Toggle file saving mode for storage.  Is Files by default. | [optional] 
**format** | **str** | Input file format | [optional] [default to 'Pptx']
**output_format** | **str** | Output file format | [optional] 
**masters** | **bool** | If translate master slides | [optional] [default to False]
**slides** | **List[int]** | List of slides to translate (1-based index). If not present, translate all slides | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.presentation_file_request import PresentationFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PresentationFileRequest from a JSON string
presentation_file_request_instance = PresentationFileRequest.from_json(json)
# print the JSON string representation of the object
print(PresentationFileRequest.to_json())

# convert the object into a dict
presentation_file_request_dict = presentation_file_request_instance.to_dict()
# create an instance of PresentationFileRequest from a dict
presentation_file_request_from_dict = PresentationFileRequest.from_dict(presentation_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


