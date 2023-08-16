# AutoPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | Input file format | [default to 'Unknown']
**output_format** | **str** | output file format | 
**masters** | **bool** | If translate master slides | [optional] [default to False]
**formatting** | **bool** | If document&#39;s formatting should be preserved, default true | [optional] [default to True]
**route** | **str** | Endpoint route | [optional] 
**separator** | **str** | Separator in files | [optional] 
**elements** | **List[int]** | List of slides to translate | [optional] 
**ranges** | [**Dict[str, WorksheetData]**](WorksheetData.md) | Dictionary of ranges in Excel workbooks | [optional] 
**short_code_list** | **Dict[str, List[List[str]]]** | Dictionary of short code names and parameters names to translate | [optional] 
**front_matter_list** | **List[List[str]]** | Dictionary where key is zero-based front matter index and value is list of lists of front matter paths | [optional] 
**source_language** | **str** | Language of original file | [default to 'en']
**target_languages** | **List[str]** | List of target languages | 
**file** | **bytearray** | File as byte array | [optional] 
**original_file_name** | **str** | Type in the file name. If null will be as request ID. | [optional] 
**url** | **str** | Link to file for translation. Ignore, if \&quot;file\&quot; property not null | [optional] 
**origin** | **str** | Url or name of application using this SDK. Not required. | [optional] 
**saving_mode** | **str** | Toggle file saving mode for storage.  Is Files by default. | [optional] 

## Example

```python
from GroupDocs.Translation.Api.models.auto_post_request import AutoPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutoPostRequest from a JSON string
auto_post_request_instance = AutoPostRequest.from_json(json)
# print the JSON string representation of the object
print AutoPostRequest.to_json()

# convert the object into a dict
auto_post_request_dict = auto_post_request_instance.to_dict()
# create an instance of AutoPostRequest from a dict
auto_post_request_form_dict = auto_post_request.from_dict(auto_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


