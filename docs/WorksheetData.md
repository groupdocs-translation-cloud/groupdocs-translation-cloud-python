# WorksheetData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | **List[int]** |  | [optional] 
**columns** | **List[int]** |  | [optional] 
**ranges** | [**List[StringStringTuple]**](StringStringTuple.md) |  | [optional] 

## Example

```python
from groupdocs-translation-cloud.models.worksheet_data import WorksheetData

# TODO update the JSON string below
json = "{}"
# create an instance of WorksheetData from a JSON string
worksheet_data_instance = WorksheetData.from_json(json)
# print the JSON string representation of the object
print WorksheetData.to_json()

# convert the object into a dict
worksheet_data_dict = worksheet_data_instance.to_dict()
# create an instance of WorksheetData from a dict
worksheet_data_form_dict = worksheet_data.from_dict(worksheet_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


