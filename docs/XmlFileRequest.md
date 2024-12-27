# XmlFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** | Language of original file | [default to 'en']
**target_languages** | **List[str]** | List of target languages | 
**original_file_name** | **str** | Type in the file name. If null will be as request ID. | [optional] 
**url** | **str** | Link to file for translation. Ignore, if \&quot;file\&quot; property not null | [optional] 
**origin** | **str** | Url or name of application using this SDK. Not required. | [optional] 
**saving_mode** | **str** | Toggle file saving mode for storage.  Is Files by default. | [optional] 
**ignore_list** | **List[str]** | List of elements for Xml, Json and Yaml formats. Determines which items should be blacklisted or whitelisted for processing depending on GroupDocs.Translation.ApiGateway.DTO.XmlFileRequest.IsWhiteList. | [optional] 
**is_white_list** | **bool** | Determines to which list the items in GroupDocs.Translation.ApiGateway.DTO.XmlFileRequest.IgnoreList should be allocated. The default is the black list. | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.xml_file_request import XmlFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of XmlFileRequest from a JSON string
xml_file_request_instance = XmlFileRequest.from_json(json)
# print the JSON string representation of the object
print(XmlFileRequest.to_json())

# convert the object into a dict
xml_file_request_dict = xml_file_request_instance.to_dict()
# create an instance of XmlFileRequest from a dict
xml_file_request_from_dict = XmlFileRequest.from_dict(xml_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


