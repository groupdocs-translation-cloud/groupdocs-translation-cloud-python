# MarkdownFileRequest

Request for markdown files or markdown files with Hugo syntax

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** | Language of original file | [default to 'en']
**target_languages** | **List[str]** | List of target languages | 
**file** | **bytearray** | File as byte array | [optional] 
**original_file_name** | **str** | Type in the file name. If null will be as request ID. | [optional] 
**url** | **str** | Link to file for translation. Ignore, if \&quot;file\&quot; property not null | [optional] 
**origin** | **str** | Url or name of application using this SDK. Not required. | [optional] 
**saving_mode** | **str** | Toggle file saving mode for storage.  Is Files by default. | [optional] 
**output_format** | **str** | output file format | 
**short_code_list** | **Dict[str, List[str]]** | Dictionary of short code names and parameters names to translate | [optional] 
**front_matter_list** | **List[List[str]]** | List of lists of frontmatter paths | [optional] 

## Example

```python
from groupdocs-translation-cloud.models.markdown_file_request import MarkdownFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MarkdownFileRequest from a JSON string
markdown_file_request_instance = MarkdownFileRequest.from_json(json)
# print the JSON string representation of the object
print MarkdownFileRequest.to_json()

# convert the object into a dict
markdown_file_request_dict = markdown_file_request_instance.to_dict()
# create an instance of MarkdownFileRequest from a dict
markdown_file_request_form_dict = markdown_file_request.from_dict(markdown_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


