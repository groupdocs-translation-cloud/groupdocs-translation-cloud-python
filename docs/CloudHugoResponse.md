# CloudHugoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | If file was parsed correctly or text of error | [optional] 
**frontmatters** | **List[List[str]]** | Structure of front matter syntax | [optional] 
**shortcodes** | **Dict[str, Optional[List[List[str]]]]** | Structure of short code syntax | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.cloud_hugo_response import CloudHugoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CloudHugoResponse from a JSON string
cloud_hugo_response_instance = CloudHugoResponse.from_json(json)
# print the JSON string representation of the object
print(CloudHugoResponse.to_json())

# convert the object into a dict
cloud_hugo_response_dict = cloud_hugo_response_instance.to_dict()
# create an instance of CloudHugoResponse from a dict
cloud_hugo_response_from_dict = CloudHugoResponse.from_dict(cloud_hugo_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


