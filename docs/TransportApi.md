# groupdocs-translation-cloud.TransportApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/translation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auto_post**](TransportApi.md#auto_post) | **POST** /auto | 
[**csv_post**](TransportApi.md#csv_post) | **POST** /csv | 
[**document_post**](TransportApi.md#document_post) | **POST** /document | 
[**document_request_id_get**](TransportApi.md#document_request_id_get) | **GET** /document/{requestId} | 
[**hc_get**](TransportApi.md#hc_get) | **GET** /hc | 
[**html_post**](TransportApi.md#html_post) | **POST** /html | 
[**hugo_get**](TransportApi.md#hugo_get) | **GET** /hugo | 
[**hugo_post**](TransportApi.md#hugo_post) | **POST** /hugo | 
[**image_to_file_post**](TransportApi.md#image_to_file_post) | **POST** /image-to-file | 
[**image_to_text_post**](TransportApi.md#image_to_text_post) | **POST** /image-to-text | 
[**languages_get**](TransportApi.md#languages_get) | **GET** /languages | 
[**markdown_post**](TransportApi.md#markdown_post) | **POST** /markdown | 
[**pdf_post**](TransportApi.md#pdf_post) | **POST** /pdf | 
[**presentation_post**](TransportApi.md#presentation_post) | **POST** /presentation | 
[**resx_post**](TransportApi.md#resx_post) | **POST** /resx | 
[**spreadsheets_post**](TransportApi.md#spreadsheets_post) | **POST** /spreadsheets | 
[**text_post**](TransportApi.md#text_post) | **POST** /text | 
[**text_request_id_get**](TransportApi.md#text_request_id_get) | **GET** /text/{requestId} | 


# **auto_post**
> StatusResponse auto_post(auto_post_request=auto_post_request)



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.auto_post_request import AutoPostRequest
from groupdocs-translation-cloud.models.status_response import StatusResponse
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    auto_post_request = groupdocs-translation-cloud.AutoPostRequest() # AutoPostRequest |  (optional)

    try:
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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.csv_file_request import CsvFileRequest
from groupdocs-translation-cloud.models.status_response import StatusResponse
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    csv_file_request = groupdocs-translation-cloud.CsvFileRequest() # CsvFileRequest |  (optional)

    try:
        api_response = api_instance.csv_post(csv_file_request=csv_file_request)
        print("The response of TransportApi->csv_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->csv_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csv_file_request** | [**CsvFileRequest**](CsvFileRequest.md)|  | [optional] 

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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.status_response import StatusResponse
from groupdocs-translation-cloud.models.text_document_file_request import TextDocumentFileRequest
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    text_document_file_request = groupdocs-translation-cloud.TextDocumentFileRequest() # TextDocumentFileRequest |  (optional)

    try:
        api_response = api_instance.document_post(text_document_file_request=text_document_file_request)
        print("The response of TransportApi->document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->document_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_document_file_request** | [**TextDocumentFileRequest**](TextDocumentFileRequest.md)|  | [optional] 

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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.cloud_file_response import CloudFileResponse
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    request_id = 'request_id_example' # str | 

    try:
        api_response = api_instance.document_request_id_get(request_id)
        print("The response of TransportApi->document_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->document_request_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  | 

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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.health_check_status import HealthCheckStatus
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)

    try:
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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.status_response import StatusResponse
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    source_language = 'en' # str |  (optional) (default to 'en')
    target_languages = ['target_languages_example'] # List[str] |  (optional)
    file = None # bytearray |  (optional)
    original_file_name = 'original_file_name_example' # str |  (optional)
    url = 'url_example' # str |  (optional)
    origin = 'origin_example' # str |  (optional)
    saving_mode = 'saving_mode_example' # str |  (optional)
    output_format = 'output_format_example' # str |  (optional)

    try:
        api_response = api_instance.html_post(source_language=source_language, target_languages=target_languages, file=file, original_file_name=original_file_name, url=url, origin=origin, saving_mode=saving_mode, output_format=output_format)
        print("The response of TransportApi->html_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->html_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_language** | **str**|  | [optional] [default to &#39;en&#39;]
 **target_languages** | [**List[str]**](str.md)|  | [optional] 
 **file** | **bytearray**|  | [optional] 
 **original_file_name** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 
 **origin** | **str**|  | [optional] 
 **saving_mode** | **str**|  | [optional] 
 **output_format** | **str**|  | [optional] 

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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.cloud_hugo_response import CloudHugoResponse
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    id = 'id_example' # str |  (optional)

    try:
        api_response = api_instance.hugo_get(id=id)
        print("The response of TransportApi->hugo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->hugo_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 

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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.status_response import StatusResponse
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    file = None # bytearray | 
    url = 'url_example' # str |  (optional)

    try:
        api_response = api_instance.hugo_post(file, url=url)
        print("The response of TransportApi->hugo_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->hugo_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **url** | **str**|  | [optional] 

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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.ocr_file_request import OcrFileRequest
from groupdocs-translation-cloud.models.status_response import StatusResponse
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    ocr_file_request = groupdocs-translation-cloud.OcrFileRequest() # OcrFileRequest |  (optional)

    try:
        api_response = api_instance.image_to_file_post(ocr_file_request=ocr_file_request)
        print("The response of TransportApi->image_to_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->image_to_file_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocr_file_request** | [**OcrFileRequest**](OcrFileRequest.md)|  | [optional] 

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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.status_response import StatusResponse
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    source = 'en' # str |  (default to 'en')
    targets = ['targets_example'] # List[str] | 
    format = 'Unknown' # str |  (optional) (default to 'Unknown')
    url = 'url_example' # str |  (optional)
    rotate = 56 # int |  (optional)
    is_handwritten = True # bool |  (optional)
    origin = 'origin_example' # str |  (optional)
    route = 'route_example' # str |  (optional)
    file = None # bytearray |  (optional)

    try:
        api_response = api_instance.image_to_text_post(source, targets, format=format, url=url, rotate=rotate, is_handwritten=is_handwritten, origin=origin, route=route, file=file)
        print("The response of TransportApi->image_to_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->image_to_text_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  | [default to &#39;en&#39;]
 **targets** | [**List[str]**](str.md)|  | 
 **format** | **str**|  | [optional] [default to &#39;Unknown&#39;]
 **url** | **str**|  | [optional] 
 **rotate** | **int**|  | [optional] 
 **is_handwritten** | **bool**|  | [optional] 
 **origin** | **str**|  | [optional] 
 **route** | **str**|  | [optional] 
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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.language_pair_data import LanguagePairData
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)

    try:
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
> StatusResponse markdown_post(markdown_file_request=markdown_file_request)



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.markdown_file_request import MarkdownFileRequest
from groupdocs-translation-cloud.models.status_response import StatusResponse
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    markdown_file_request = groupdocs-translation-cloud.MarkdownFileRequest() # MarkdownFileRequest |  (optional)

    try:
        api_response = api_instance.markdown_post(markdown_file_request=markdown_file_request)
        print("The response of TransportApi->markdown_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->markdown_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **markdown_file_request** | [**MarkdownFileRequest**](MarkdownFileRequest.md)|  | [optional] 

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

# **pdf_post**
> StatusResponse pdf_post(pdf_file_request=pdf_file_request)



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.pdf_file_request import PdfFileRequest
from groupdocs-translation-cloud.models.status_response import StatusResponse
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    pdf_file_request = groupdocs-translation-cloud.PdfFileRequest() # PdfFileRequest |  (optional)

    try:
        api_response = api_instance.pdf_post(pdf_file_request=pdf_file_request)
        print("The response of TransportApi->pdf_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->pdf_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pdf_file_request** | [**PdfFileRequest**](PdfFileRequest.md)|  | [optional] 

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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.presentation_file_request import PresentationFileRequest
from groupdocs-translation-cloud.models.status_response import StatusResponse
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    presentation_file_request = groupdocs-translation-cloud.PresentationFileRequest() # PresentationFileRequest |  (optional)

    try:
        api_response = api_instance.presentation_post(presentation_file_request=presentation_file_request)
        print("The response of TransportApi->presentation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->presentation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **presentation_file_request** | [**PresentationFileRequest**](PresentationFileRequest.md)|  | [optional] 

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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.resx_file_request import ResxFileRequest
from groupdocs-translation-cloud.models.status_response import StatusResponse
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    resx_file_request = groupdocs-translation-cloud.ResxFileRequest() # ResxFileRequest |  (optional)

    try:
        api_response = api_instance.resx_post(resx_file_request=resx_file_request)
        print("The response of TransportApi->resx_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->resx_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resx_file_request** | [**ResxFileRequest**](ResxFileRequest.md)|  | [optional] 

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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.spreadsheet_file_request import SpreadsheetFileRequest
from groupdocs-translation-cloud.models.status_response import StatusResponse
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    spreadsheet_file_request = groupdocs-translation-cloud.SpreadsheetFileRequest() # SpreadsheetFileRequest |  (optional)

    try:
        api_response = api_instance.spreadsheets_post(spreadsheet_file_request=spreadsheet_file_request)
        print("The response of TransportApi->spreadsheets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->spreadsheets_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_file_request** | [**SpreadsheetFileRequest**](SpreadsheetFileRequest.md)|  | [optional] 

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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.status_response import StatusResponse
from groupdocs-translation-cloud.models.text_request import TextRequest
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    text_request = groupdocs-translation-cloud.TextRequest() # TextRequest |  (optional)

    try:
        api_response = api_instance.text_post(text_request=text_request)
        print("The response of TransportApi->text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->text_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text_request** | [**TextRequest**](TextRequest.md)|  | [optional] 

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



### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.cloud_text_response import CloudTextResponse
from groupdocs-translation-cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Configure OAuth2 access token for authorization: JWT
configuration = groupdocs-translation-cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation",
    client_id = "YOUR_CLIENT_ID",
    client_secret = "YOUR_CLIENT_SECRET"
)

# Enter a context with an instance of the API client
with groupdocs-translation-cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs-translation-cloud.TransportApi(api_client)
    request_id = 'request_id_example' # str | 

    try:
        api_response = api_instance.text_request_id_get(request_id)
        print("The response of TransportApi->text_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportApi->text_request_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**|  | 

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

