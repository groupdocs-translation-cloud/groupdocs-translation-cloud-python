# CloudTextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | If file was translated correctly or text of error | [optional] 
**translations** | **Dict[str, Optional[List[str]]]** | Translated texts | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.cloud_text_response import CloudTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudTextResponse from a JSON string
cloud_text_response_instance = CloudTextResponse.from_json(json)
# print the JSON string representation of the object
print(CloudTextResponse.to_json())

# convert the object into a dict
cloud_text_response_dict = cloud_text_response_instance.to_dict()
# create an instance of CloudTextResponse from a dict
cloud_text_response_from_dict = CloudTextResponse.from_dict(cloud_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


