# OcrFileRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_language** | **str** |  | [default to 'en']
**target_languages** | **List[str]** |  | 
**file** | **bytearray** |  | [optional] 
**original_file_name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**origin** | **str** |  | [optional] 
**saving_mode** | **str** |  | [optional] 
**format** | **str** |  | [optional] [default to 'Unknown']
**ocrformat** | **str** |  | [default to 'Pdf']
**output_format** | **str** |  | 
**rotation_angle** | **int** |  | [optional] 
**formatting** | **bool** |  | [optional] [default to True]
**route** | **str** |  | [optional] 
**pages** | **List[int]** |  | [optional] 

## Example

```python
from groupdocs-translation-cloud.models.ocr_file_request import OcrFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OcrFileRequest from a JSON string
ocr_file_request_instance = OcrFileRequest.from_json(json)
# print the JSON string representation of the object
print OcrFileRequest.to_json()

# convert the object into a dict
ocr_file_request_dict = ocr_file_request_instance.to_dict()
# create an instance of OcrFileRequest from a dict
ocr_file_request_form_dict = ocr_file_request.from_dict(ocr_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


