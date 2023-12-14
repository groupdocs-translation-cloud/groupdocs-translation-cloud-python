# HugoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | File as byte array | [optional] 
**url** | **str** | Link to file for translation | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.hugo_request import HugoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HugoRequest from a JSON string
hugo_request_instance = HugoRequest.from_json(json)
# print the JSON string representation of the object
print HugoRequest.to_json()

# convert the object into a dict
hugo_request_dict = hugo_request_instance.to_dict()
# create an instance of HugoRequest from a dict
hugo_request_form_dict = hugo_request.from_dict(hugo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


