# ImageToTextRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | Originnal file format | [optional] [default to 'Unknown']
**source** | **str** | Language of original file | [optional] [default to 'en']
**targets** | **List[str]** | List of target languages | [optional] 
**file** | **bytearray** | File for translation | [optional] 
**url** | **str** | Link to file for translation | [optional] 
**rotate** | **int** | Left to write angle to rotate scanned image / pdf | [optional] 
**ishandwritten** | **bool** | is handwritten text | [optional] 
**origin** | **str** | for analysis only | [optional] 
**route** | **str** | endpoints route | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.image_to_text_request import ImageToTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageToTextRequest from a JSON string
image_to_text_request_instance = ImageToTextRequest.from_json(json)
# print the JSON string representation of the object
print ImageToTextRequest.to_json()

# convert the object into a dict
image_to_text_request_dict = image_to_text_request_instance.to_dict()
# create an instance of ImageToTextRequest from a dict
image_to_text_request_form_dict = image_to_text_request.from_dict(image_to_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


