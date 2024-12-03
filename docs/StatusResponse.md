# StatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.status_response import StatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatusResponse from a JSON string
status_response_instance = StatusResponse.from_json(json)
# print the JSON string representation of the object
print(StatusResponse.to_json())

# convert the object into a dict
status_response_dict = status_response_instance.to_dict()
# create an instance of StatusResponse from a dict
status_response_from_dict = StatusResponse.from_dict(status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


