# ImageToFileRequest


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
**format** | **str** | Original file format | [optional] [default to 'Unknown']
**ocrformat** | **str** | File format after recognition | [default to 'Pdf']
**output_format** | **str** | output file format | 
**rotation_angle** | **int** | Left to write angle to rotate scanned image / pdf | [optional] 
**formatting** | **bool** | If document&#39;s formatting should be preserved, default true | [optional] [default to True]
**route** | **str** | endpoints route | [optional] 
**pages** | **List[int]** | List of pages to translate for scanned pdf | [optional] 

## Example

```python
from groupdocs-translation-cloud.models.image_to_file_request import ImageToFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageToFileRequest from a JSON string
image_to_file_request_instance = ImageToFileRequest.from_json(json)
# print the JSON string representation of the object
print ImageToFileRequest.to_json()

# convert the object into a dict
image_to_file_request_dict = image_to_file_request_instance.to_dict()
# create an instance of ImageToFileRequest from a dict
image_to_file_request_form_dict = image_to_file_request.from_dict(image_to_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


