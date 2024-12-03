# TextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** | Language of original text | [optional] 
**target_languages** | **List[str]** | List of target languages | [optional] 
**texts** | **List[str]** | Text array to translate | [optional] 
**origin** | **str** | For analysis only | [optional] 
**contains_markdown** | **bool** | Set to true if you want to handle markdown in text | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.text_request import TextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TextRequest from a JSON string
text_request_instance = TextRequest.from_json(json)
# print the JSON string representation of the object
print(TextRequest.to_json())

# convert the object into a dict
text_request_dict = text_request_instance.to_dict()
# create an instance of TextRequest from a dict
text_request_from_dict = TextRequest.from_dict(text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


