# TextDocumentFileRequest

Request for files with textual content (doc, docx, docm, rtf, odt, txt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** | Language of original file | [default to 'en']
**target_languages** | **List[str]** | List of target languages | 
**file** | **bytearray** | File as byte array | [optional] 
**original_file_name** | **str** | Type in the file name. If null will be as request ID. | [optional] 
**url** | **str** | Link to file for translation. Ignore, if \&quot;file\&quot; property not null | [optional] 
**saving_mode** | **str** | Toggle file saving mode for storage.  Is Files by default. | [optional] 
**format** | **str** | Input file format | [default to 'Docx']
**output_format** | **str** | output file format | 
**preserve_formatting** | **bool** | If document&#39;s formatting should be preserved, default true | [optional] [default to True]
**origin** | **str** | for analysis only | [optional] 
**pages** | **List[int]** | Choose pages for translation (1-based index). If not present, translate all pages | [optional] 

## Example

```python
from groupdocs_translation_cloud.models.text_document_file_request import TextDocumentFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TextDocumentFileRequest from a JSON string
text_document_file_request_instance = TextDocumentFileRequest.from_json(json)
# print the JSON string representation of the object
print TextDocumentFileRequest.to_json()

# convert the object into a dict
text_document_file_request_dict = text_document_file_request_instance.to_dict()
# create an instance of TextDocumentFileRequest from a dict
text_document_file_request_form_dict = text_document_file_request.from_dict(text_document_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


