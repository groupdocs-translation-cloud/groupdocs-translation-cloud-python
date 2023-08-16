# GroupDocs.Translation.Api.TransportApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/translation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auto_post**](TransportApi.md#auto_post) | **POST** /auto | Translate any supported file
[**csv_post**](TransportApi.md#csv_post) | **POST** /csv | Translate CSV and TSV files
[**document_post**](TransportApi.md#document_post) | **POST** /document | Translate Microsoft Word documents, rtf, txt, odt
[**document_request_id_get**](TransportApi.md#document_request_id_get) | **GET** /document/{requestId} | Return document translation status.  Also return URLs for downloading of translated document if translation was successful
[**hc_get**](TransportApi.md#hc_get) | **GET** /hc | Health check for all services.
[**html_post**](TransportApi.md#html_post) | **POST** /html | Translate HTML files
[**hugo_get**](TransportApi.md#hugo_get) | **GET** /hugo | Get hugo syntax structure from markdown file
[**hugo_post**](TransportApi.md#hugo_post) | **POST** /hugo | Run hugo syntax structure analyzing from markdown file
[**image_to_file_post**](TransportApi.md#image_to_file_post) | **POST** /image-to-file | Translate image or scanned pdf and return file
[**image_to_text_post**](TransportApi.md#image_to_text_post) | **POST** /image-to-text | Translate text on image or scanned pdf
[**languages_get**](TransportApi.md#languages_get) | **GET** /languages | Return list of available language pairs
[**markdown_post**](TransportApi.md#markdown_post) | **POST** /markdown | Translate Markdown files
[**pdf_post**](TransportApi.md#pdf_post) | **POST** /pdf | Translate pdf files
[**presentation_post**](TransportApi.md#presentation_post) | **POST** /presentation | Translate Microsoft PowerPoint presentations, odp
[**resx_post**](TransportApi.md#resx_post) | **POST** /resx | Translate RESX files
[**spreadsheets_post**](TransportApi.md#spreadsheets_post) | **POST** /spreadsheets | Translate Microsoft Excel workbooks, ods
[**text_post**](TransportApi.md#text_post) | **POST** /text | Translate text
[**text_request_id_get**](TransportApi.md#text_request_id_get) | **GET** /text/{requestId} | Return text translation status.  Also return translated text if translation was successful


# **auto_post**
> StatusResponse auto_post(auto_post_request=auto_post_request)

Translate any supported file

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.auto_post_request import AutoPostRequest
from GroupDocs.Translation.Api.models.status_response import StatusResponse
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    auto_post_request = GroupDocs.Translation.Api.AutoPostRequest() # AutoPostRequest |  (optional)

    try:
        # Translate any supported file
        api_response = api_instance.auto_post(auto_post_request=auto_post_request)
        print("The response of TransportApi->auto_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->auto_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_post_request** | [**AutoPostRequest**](AutoPostRequest.md)|  | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csv_post**
> StatusResponse csv_post(csv_file_request=csv_file_request)

Translate CSV and TSV files

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.csv_file_request import CsvFileRequest
from GroupDocs.Translation.Api.models.status_response import StatusResponse
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    csv_file_request = GroupDocs.Translation.Api.CsvFileRequest() # CsvFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate CSV and TSV files
        api_response = api_instance.csv_post(csv_file_request=csv_file_request)
        print("The response of TransportApi->csv_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->csv_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csv_file_request** | [**CsvFileRequest**](CsvFileRequest.md)| String in body of request, containing JSON with parameters for translation. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_post**
> StatusResponse document_post(text_document_file_request=text_document_file_request)

Translate Microsoft Word documents, rtf, txt, odt

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.status_response import StatusResponse
from GroupDocs.Translation.Api.models.text_document_file_request import TextDocumentFileRequest
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    text_document_file_request = GroupDocs.Translation.Api.TextDocumentFileRequest() # TextDocumentFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate Microsoft Word documents, rtf, txt, odt
        api_response = api_instance.document_post(text_document_file_request=text_document_file_request)
        print("The response of TransportApi->document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->document_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_document_file_request** | [**TextDocumentFileRequest**](TextDocumentFileRequest.md)| String in body of request, containing JSON with parameters for translation. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_request_id_get**
> CloudFileResponse document_request_id_get(request_id)

Return document translation status.  Also return URLs for downloading of translated document if translation was successful

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.cloud_file_response import CloudFileResponse
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/translation/document response

    try:
        # Return document translation status.  Also return URLs for downloading of translated document if translation was successful
        api_response = api_instance.document_request_id_get(request_id)
        print("The response of TransportApi->document_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->document_request_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID which got from /v3/translation/document response | 

### Return type

[**CloudFileResponse**](CloudFileResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hc_get**
> HealthCheckStatus hc_get()

Health check for all services.

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.health_check_status import HealthCheckStatus
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)

    try:
        # Health check for all services.
        api_response = api_instance.hc_get()
        print("The response of TransportApi->hc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->hc_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthCheckStatus**](HealthCheckStatus.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **html_post**
> StatusResponse html_post(source_language=source_language, target_languages=target_languages, file=file, original_file_name=original_file_name, url=url, origin=origin, saving_mode=saving_mode, output_format=output_format)

Translate HTML files

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.status_response import StatusResponse
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    source_language = 'en' # str | Language of original file (optional) (default to 'en')
    target_languages = ['target_languages_example'] # List[str] | List of target languages (optional)
    file = None # bytearray | File as byte array (optional)
    original_file_name = 'original_file_name_example' # str | Type in the file name. If null will be as request ID. (optional)
    url = 'url_example' # str | Link to file for translation. Ignore, if \\\"file\\\" property not null (optional)
    origin = 'origin_example' # str | Url or name of application using this SDK. Not required. (optional)
    saving_mode = 'saving_mode_example' # str | Toggle file saving mode for storage.  Is Files by default. (optional)
    output_format = 'output_format_example' # str | output file format (optional)

    try:
        # Translate HTML files
        api_response = api_instance.html_post(source_language=source_language, target_languages=target_languages, file=file, original_file_name=original_file_name, url=url, origin=origin, saving_mode=saving_mode, output_format=output_format)
        print("The response of TransportApi->html_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->html_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_language** | **str**| Language of original file | [optional] [default to &#39;en&#39;]
 **target_languages** | [**List[str]**](str.md)| List of target languages | [optional] 
 **file** | **bytearray**| File as byte array | [optional] 
 **original_file_name** | **str**| Type in the file name. If null will be as request ID. | [optional] 
 **url** | **str**| Link to file for translation. Ignore, if \\\&quot;file\\\&quot; property not null | [optional] 
 **origin** | **str**| Url or name of application using this SDK. Not required. | [optional] 
 **saving_mode** | **str**| Toggle file saving mode for storage.  Is Files by default. | [optional] 
 **output_format** | **str**| output file format | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hugo_get**
> CloudHugoResponse hugo_get(id=id)

Get hugo syntax structure from markdown file

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.cloud_hugo_response import CloudHugoResponse
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    id = 'id_example' # str | id from PostHugo> (optional)

    try:
        # Get hugo syntax structure from markdown file
        api_response = api_instance.hugo_get(id=id)
        print("The response of TransportApi->hugo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->hugo_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id from PostHugo&gt; | [optional] 

### Return type

[**CloudHugoResponse**](CloudHugoResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hugo_post**
> StatusResponse hugo_post(file, url=url)

Run hugo syntax structure analyzing from markdown file

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.status_response import StatusResponse
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    file = None # bytearray | File as byte array
    url = 'url_example' # str | Link to file for translation (optional)

    try:
        # Run hugo syntax structure analyzing from markdown file
        api_response = api_instance.hugo_post(file, url=url)
        print("The response of TransportApi->hugo_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->hugo_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| File as byte array | 
 **url** | **str**| Link to file for translation | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_to_file_post**
> StatusResponse image_to_file_post(ocr_file_request=ocr_file_request)

Translate image or scanned pdf and return file

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.ocr_file_request import OcrFileRequest
from GroupDocs.Translation.Api.models.status_response import StatusResponse
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    ocr_file_request = GroupDocs.Translation.Api.OcrFileRequest() # OcrFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate image or scanned pdf and return file
        api_response = api_instance.image_to_file_post(ocr_file_request=ocr_file_request)
        print("The response of TransportApi->image_to_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->image_to_file_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocr_file_request** | [**OcrFileRequest**](OcrFileRequest.md)| String in body of request, containing JSON with parameters for translation. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_to_text_post**
> StatusResponse image_to_text_post(source, targets, format=format, url=url, rotate=rotate, is_handwritten=is_handwritten, origin=origin, route=route, file=file)

Translate text on image or scanned pdf

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.status_response import StatusResponse
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    source = 'en' # str | Language of original file (default to 'en')
    targets = ['targets_example'] # List[str] | List of target languages
    format = 'Unknown' # str | Originnal file format (optional) (default to 'Unknown')
    url = 'url_example' # str | Link to file for translation (optional)
    rotate = 56 # int | Left to write angle to rotate scanned image / pdf (optional)
    is_handwritten = True # bool | is handwritten text (optional)
    origin = 'origin_example' # str | for analysis only (optional)
    route = 'route_example' # str | endpoints route (optional)
    file = None # bytearray |  (optional)

    try:
        # Translate text on image or scanned pdf
        api_response = api_instance.image_to_text_post(source, targets, format=format, url=url, rotate=rotate, is_handwritten=is_handwritten, origin=origin, route=route, file=file)
        print("The response of TransportApi->image_to_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->image_to_text_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Language of original file | [default to &#39;en&#39;]
 **targets** | [**List[str]**](str.md)| List of target languages | 
 **format** | **str**| Originnal file format | [optional] [default to &#39;Unknown&#39;]
 **url** | **str**| Link to file for translation | [optional] 
 **rotate** | **int**| Left to write angle to rotate scanned image / pdf | [optional] 
 **is_handwritten** | **bool**| is handwritten text | [optional] 
 **origin** | **str**| for analysis only | [optional] 
 **route** | **str**| endpoints route | [optional] 
 **file** | **bytearray**|  | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **languages_get**
> List[LanguagePairData] languages_get()

Return list of available language pairs

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.language_pair_data import LanguagePairData
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)

    try:
        # Return list of available language pairs
        api_response = api_instance.languages_get()
        print("The response of TransportApi->languages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->languages_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[LanguagePairData]**](LanguagePairData.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markdown_post**
> StatusResponse markdown_post(source_language, target_languages, output_format, file=file, original_file_name=original_file_name, url=url, origin=origin, saving_mode=saving_mode, front_matter_list=front_matter_list)

Translate Markdown files

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.status_response import StatusResponse
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    source_language = 'en' # str | Language of original file (default to 'en')
    target_languages = ['target_languages_example'] # List[str] | List of target languages
    output_format = 'output_format_example' # str | output file format
    file = None # bytearray | File as byte array (optional)
    original_file_name = 'original_file_name_example' # str | Type in the file name. If null will be as request ID. (optional)
    url = 'url_example' # str | Link to file for translation. Ignore, if \\\"file\\\" property not null (optional)
    origin = 'origin_example' # str | Url or name of application using this SDK. Not required. (optional)
    saving_mode = 'saving_mode_example' # str | Toggle file saving mode for storage.  Is Files by default. (optional)
    front_matter_list = [GroupDocs.Translation.Api.List[str]()] # List[List[str]] | List of lists of frontmatter paths (optional)

    try:
        # Translate Markdown files
        api_response = api_instance.markdown_post(source_language, target_languages, output_format, file=file, original_file_name=original_file_name, url=url, origin=origin, saving_mode=saving_mode, front_matter_list=front_matter_list)
        print("The response of TransportApi->markdown_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->markdown_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_language** | **str**| Language of original file | [default to &#39;en&#39;]
 **target_languages** | [**List[str]**](str.md)| List of target languages | 
 **output_format** | **str**| output file format | 
 **file** | **bytearray**| File as byte array | [optional] 
 **original_file_name** | **str**| Type in the file name. If null will be as request ID. | [optional] 
 **url** | **str**| Link to file for translation. Ignore, if \\\&quot;file\\\&quot; property not null | [optional] 
 **origin** | **str**| Url or name of application using this SDK. Not required. | [optional] 
 **saving_mode** | **str**| Toggle file saving mode for storage.  Is Files by default. | [optional] 
 **front_matter_list** | [**List[List[str]]**](List[str].md)| List of lists of frontmatter paths | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pdf_post**
> StatusResponse pdf_post(pdf_file_request=pdf_file_request)

Translate pdf files

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.pdf_file_request import PdfFileRequest
from GroupDocs.Translation.Api.models.status_response import StatusResponse
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    pdf_file_request = GroupDocs.Translation.Api.PdfFileRequest() # PdfFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate pdf files
        api_response = api_instance.pdf_post(pdf_file_request=pdf_file_request)
        print("The response of TransportApi->pdf_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->pdf_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_file_request** | [**PdfFileRequest**](PdfFileRequest.md)| String in body of request, containing JSON with parameters for translation. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **presentation_post**
> StatusResponse presentation_post(presentation_file_request=presentation_file_request)

Translate Microsoft PowerPoint presentations, odp

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.presentation_file_request import PresentationFileRequest
from GroupDocs.Translation.Api.models.status_response import StatusResponse
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    presentation_file_request = GroupDocs.Translation.Api.PresentationFileRequest() # PresentationFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate Microsoft PowerPoint presentations, odp
        api_response = api_instance.presentation_post(presentation_file_request=presentation_file_request)
        print("The response of TransportApi->presentation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->presentation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **presentation_file_request** | [**PresentationFileRequest**](PresentationFileRequest.md)| String in body of request, containing JSON with parameters for translation. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resx_post**
> StatusResponse resx_post(resx_file_request=resx_file_request)

Translate RESX files

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.resx_file_request import ResxFileRequest
from GroupDocs.Translation.Api.models.status_response import StatusResponse
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    resx_file_request = GroupDocs.Translation.Api.ResxFileRequest() # ResxFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate RESX files
        api_response = api_instance.resx_post(resx_file_request=resx_file_request)
        print("The response of TransportApi->resx_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->resx_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resx_file_request** | [**ResxFileRequest**](ResxFileRequest.md)| String in body of request, containing JSON with parameters for translation. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spreadsheets_post**
> StatusResponse spreadsheets_post(spreadsheet_file_request=spreadsheet_file_request)

Translate Microsoft Excel workbooks, ods

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.spreadsheet_file_request import SpreadsheetFileRequest
from GroupDocs.Translation.Api.models.status_response import StatusResponse
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    spreadsheet_file_request = GroupDocs.Translation.Api.SpreadsheetFileRequest() # SpreadsheetFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate Microsoft Excel workbooks, ods
        api_response = api_instance.spreadsheets_post(spreadsheet_file_request=spreadsheet_file_request)
        print("The response of TransportApi->spreadsheets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->spreadsheets_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_file_request** | [**SpreadsheetFileRequest**](SpreadsheetFileRequest.md)| String in body of request, containing JSON with parameters for translation. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_post**
> StatusResponse text_post(text_request=text_request)

Translate text

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.status_response import StatusResponse
from GroupDocs.Translation.Api.models.text_request import TextRequest
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    text_request = GroupDocs.Translation.Api.TextRequest() # TextRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate text
        api_response = api_instance.text_post(text_request=text_request)
        print("The response of TransportApi->text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->text_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_request** | [**TextRequest**](TextRequest.md)| String in body of request, containing JSON with parameters for translation. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_request_id_get**
> CloudTextResponse text_request_id_get(request_id)

Return text translation status.  Also return translated text if translation was successful

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import GroupDocs.Translation.Api
from GroupDocs.Translation.Api.models.cloud_text_response import CloudTextResponse
from GroupDocs.Translation.Api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = GroupDocs.Translation.Api.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with GroupDocs.Translation.Api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GroupDocs.Translation.Api.TransportApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/translation/text response

    try:
        # Return text translation status.  Also return translated text if translation was successful
        api_response = api_instance.text_request_id_get(request_id)
        print("The response of TransportApi->text_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->text_request_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID which got from /v3/translation/text response | 

### Return type

[**CloudTextResponse**](CloudTextResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

