# FileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** | Language of original file | [optional] [default to 'en']
**target_languages** | **List[str]** | List of target languages | [optional] 
**original_file_name** | **str** | Type in the file name. If null will be as request ID. | [optional] 
**url** | **str** | Link to file for translation. Ignore, if \&quot;file\&quot; property not null | [optional] 
**origin** | **str** | Url or name of the application using this SDK. Not required. | [optional] 
**is_need_alignment** | **bool** | Do result formating like the source. This option needs more expensive requests. | [optional] 
**translation_dictionary** | **Dict[str, Optional[str]]** | Set a specific translation between source and target words. | [optional] 
**saving_mode** | **str** | Toggle file saving mode for storage.  Is Files by default. | [optional] 
**format** | **str** | Input file format | [optional] [default to 'Unknown']
**output_format** | **str** | output file format | [optional] 
**masters** | **bool** | If translate master slides | [optional] [default to False]
**formatting** | **bool** | If document&#39;s formatting should be preserved, default true | [optional] [default to True]
**route** | **str** | Endpoint route | [optional] 
**separator** | **str** | Separator in files | [optional] 
**elements** | **List[int]** | List of slides to translate (1-based index). If not present, translate all elements (page, slide, worksheet) | [optional] 
**ranges** | [**Dict[str, WorksheetData]**](WorksheetData.md) | Dictionary of ranges in Excel workbooks | [optional] 
**shortcodedict** | **Dict[str, Optional[List[str]]]** | Dictionary of short code names and parameters names to translate | [optional] 
**front_matter_list** | **List[List[str]]** | Dictionary where key is zero-based front matter index and value is list of lists of front matter paths | [optional] 
**ignore_list** | **List[str]** | List of elements for Xml, Json and Yaml formats. Determines which items should be blacklisted or whitelisted for processing depending on GroupDocs.Translation.ApiGateway.DTO.FileRequest.IsWhiteList. | [optional] 
**is_white_list** | **bool** | Determines to which list the items in GroupDocs.Translation.ApiGateway.DTO.FileRequest.IgnoreList should be allocated. The default is the black list. | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.file_request import FileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileRequest from a JSON string
file_request_instance = FileRequest.from_json(json)
# print the JSON string representation of the object
print(FileRequest.to_json())

# convert the object into a dict
file_request_dict = file_request_instance.to_dict()
# create an instance of FileRequest from a dict
file_request_from_dict = FileRequest.from_dict(file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


