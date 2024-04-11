# CloudFileRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | \&quot;doc(x|m)\&quot; if Word document, \&quot;xls(x|m)\&quot; if Excel workbook | [optional] 
**out_format** | **str** | output file format | [optional] 
**request_id** | **str** | id of request | [optional] 
**ids** | **List[int]** | Language pairs to translate | [optional] 
**url** | **str** | Link to file for translation | [optional] 
**size** | **int** | File size | [optional] 
**masters** | **bool** | If translate master slides | [optional] 
**formatting** | **bool** | If document&#39;s formatting should be preserved, default true | [optional] 
**origin** | **str** | for analysis only | [optional] 
**elements** | **List[int]** | List of slides to translate | [optional] 
**ranges** | [**Dict[str, WorksheetData]**](WorksheetData.md) | Dictionary of ranges in Excel workbooks | [optional] 
**short_code_dict** | **Dict[str, List[str]]** | Dictiory of short code names and parameters names to translate | [optional] 
**front_matter_list** | **List[List[str]]** | Dictionary where key is zero-based front matter index and value is list of lists of front matter paths | [optional] 
**original_file_name** | **str** | Original name of file | [optional] 
**separator** | **str** | Separator in files | [optional] 
**is_paid** | **bool** | Set true if paid user | [optional] 
**saving_mode** | **str** | Toggle files saving mode | [optional] 
**details** | **Dict[str, str]** | Details of the requests. Using for e2e tracking | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.cloud_file_request import CloudFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloudFileRequest from a JSON string
cloud_file_request_instance = CloudFileRequest.from_json(json)
# print the JSON string representation of the object
print CloudFileRequest.to_json()

# convert the object into a dict
cloud_file_request_dict = cloud_file_request_instance.to_dict()
# create an instance of CloudFileRequest from a dict
cloud_file_request_form_dict = cloud_file_request.from_dict(cloud_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


