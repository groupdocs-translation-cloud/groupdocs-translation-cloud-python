# HealthCheckEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**is_healthy** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.health_check_entity import HealthCheckEntity

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckEntity from a JSON string
health_check_entity_instance = HealthCheckEntity.from_json(json)
# print the JSON string representation of the object
print(HealthCheckEntity.to_json())

# convert the object into a dict
health_check_entity_dict = health_check_entity_instance.to_dict()
# create an instance of HealthCheckEntity from a dict
health_check_entity_from_dict = HealthCheckEntity.from_dict(health_check_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


