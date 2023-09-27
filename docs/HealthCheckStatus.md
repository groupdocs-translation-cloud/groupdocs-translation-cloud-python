# HealthCheckStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kafka_delivery_status** | **str** |  | [optional] 
**cloud_status** | **str** |  | [optional] 

## Example

```python
from groupdocs-translation-cloud.models.health_check_status import HealthCheckStatus

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckStatus from a JSON string
health_check_status_instance = HealthCheckStatus.from_json(json)
# print the JSON string representation of the object
print HealthCheckStatus.to_json()

# convert the object into a dict
health_check_status_dict = health_check_status_instance.to_dict()
# create an instance of HealthCheckStatus from a dict
health_check_status_form_dict = health_check_status.from_dict(health_check_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


