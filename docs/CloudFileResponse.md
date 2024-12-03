# CloudFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** |  | [optional] 
**urls** | [**Dict[str, UrlFileInfo]**](UrlFileInfo.md) |  | [optional] 
**scores** | **Dict[str, Optional[float]]** |  | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.cloud_file_response import CloudFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudFileResponse from a JSON string
cloud_file_response_instance = CloudFileResponse.from_json(json)
# print the JSON string representation of the object
print(CloudFileResponse.to_json())

# convert the object into a dict
cloud_file_response_dict = cloud_file_response_instance.to_dict()
# create an instance of CloudFileResponse from a dict
cloud_file_response_from_dict = CloudFileResponse.from_dict(cloud_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


