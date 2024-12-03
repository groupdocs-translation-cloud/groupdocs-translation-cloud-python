# CloudFileResponseWithAdditionalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** |  | [optional] 
**urls** | [**Dict[str, UrlFileInfo]**](UrlFileInfo.md) |  | [optional] 
**scores** | **Dict[str, Optional[float]]** |  | [optional] 
**request** | [**CloudFileRequest**](CloudFileRequest.md) |  | [optional] 
**details** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.cloud_file_response_with_additional_info import CloudFileResponseWithAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CloudFileResponseWithAdditionalInfo from a JSON string
cloud_file_response_with_additional_info_instance = CloudFileResponseWithAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(CloudFileResponseWithAdditionalInfo.to_json())

# convert the object into a dict
cloud_file_response_with_additional_info_dict = cloud_file_response_with_additional_info_instance.to_dict()
# create an instance of CloudFileResponseWithAdditionalInfo from a dict
cloud_file_response_with_additional_info_from_dict = CloudFileResponseWithAdditionalInfo.from_dict(cloud_file_response_with_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


