# HealthCheckStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[HealthCheckEntity]**](HealthCheckEntity.md) |  | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.health_check_status import HealthCheckStatus

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckStatus from a JSON string
health_check_status_instance = HealthCheckStatus.from_json(json)
# print the JSON string representation of the object
print(HealthCheckStatus.to_json())

# convert the object into a dict
health_check_status_dict = health_check_status_instance.to_dict()
# create an instance of HealthCheckStatus from a dict
health_check_status_from_dict = HealthCheckStatus.from_dict(health_check_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


