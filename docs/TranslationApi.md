# groupdocs-translation-cloud.TranslationApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/translation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auto_post**](TranslationApi.md#auto_post) | **POST** /auto | Translate any supported file
[**csv_post**](TranslationApi.md#csv_post) | **POST** /csv | Translate CSV and TSV files
[**document_post**](TranslationApi.md#document_post) | **POST** /document | Translate Microsoft Word documents, rtf, txt, odt
[**document_request_id_get**](TranslationApi.md#document_request_id_get) | **GET** /document/{requestId} | Return document translation status.  Also return URLs for downloading of translated document if translation was successful
[**document_trial_post**](TranslationApi.md#document_trial_post) | **POST** /document/trial | Trial translate Microsoft Word documents, rtf, txt, odt without conversation. Translate only first page or 1000 symbols.
[**hc_get**](TranslationApi.md#hc_get) | **GET** /hc | Health check for all services.
[**html_post**](TranslationApi.md#html_post) | **POST** /html | Translate HTML files
[**hugo_get**](TranslationApi.md#hugo_get) | **GET** /hugo | Get hugo syntax structure from markdown file
[**hugo_post**](TranslationApi.md#hugo_post) | **POST** /hugo | Run hugo syntax structure analyzing from markdown file
[**image_to_file_post**](TranslationApi.md#image_to_file_post) | **POST** /image-to-file | Translate image or scanned pdf and return file
[**image_to_text_post**](TranslationApi.md#image_to_text_post) | **POST** /image-to-text | Translate text on image or scanned pdf
[**languages_get**](TranslationApi.md#languages_get) | **GET** /languages | Return list of available language pairs
[**markdown_post**](TranslationApi.md#markdown_post) | **POST** /markdown | Translate Markdown files
[**pdf_post**](TranslationApi.md#pdf_post) | **POST** /pdf | Translate pdf files
[**pdf_trial_post**](TranslationApi.md#pdf_trial_post) | **POST** /pdf/trial | Trial pdf translation. Translate only first page without conversion to another format.
[**presentation_post**](TranslationApi.md#presentation_post) | **POST** /presentation | Translate Microsoft PowerPoint presentations, odp
[**resx_post**](TranslationApi.md#resx_post) | **POST** /resx | Translate RESX files
[**spreadsheet_post**](TranslationApi.md#spreadsheet_post) | **POST** /spreadsheet | Translate Microsoft Excel workbooks, ods
[**text_post**](TranslationApi.md#text_post) | **POST** /text | Translate text
[**text_request_id_get**](TranslationApi.md#text_request_id_get) | **GET** /text/{requestId} | Return text translation status.  Also return translated text if translation was successful
[**text_trial_post**](TranslationApi.md#text_trial_post) | **POST** /text/trial | Trial translate text. Translate only 1000 symbols.


# **auto_post**
> StatusResponse auto_post(file_request=file_request)

Translate any supported file

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.file_request import FileRequest
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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    file_request = groupdocs-translation-cloud.FileRequest() # FileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate any supported file
        api_response = api_instance.auto_post(file_request=file_request)
        print("The response of TranslationApi->auto_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->auto_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_request** | [**FileRequest**](FileRequest.md)| String in body of request, containing JSON with parameters for translation. | [optional] 

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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    csv_file_request = groupdocs-translation-cloud.CsvFileRequest() # CsvFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate CSV and TSV files
        api_response = api_instance.csv_post(csv_file_request=csv_file_request)
        print("The response of TranslationApi->csv_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->csv_post: %s\n" % e)
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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    text_document_file_request = groupdocs-translation-cloud.TextDocumentFileRequest() # TextDocumentFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate Microsoft Word documents, rtf, txt, odt
        api_response = api_instance.document_post(text_document_file_request=text_document_file_request)
        print("The response of TranslationApi->document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->document_post: %s\n" % e)
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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/translation/document response

    try:
        # Return document translation status.  Also return URLs for downloading of translated document if translation was successful
        api_response = api_instance.document_request_id_get(request_id)
        print("The response of TranslationApi->document_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->document_request_id_get: %s\n" % e)
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

# **document_trial_post**
> StatusResponse document_trial_post(text_document_file_request=text_document_file_request)

Trial translate Microsoft Word documents, rtf, txt, odt without conversation. Translate only first page or 1000 symbols.

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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    text_document_file_request = groupdocs-translation-cloud.TextDocumentFileRequest() # TextDocumentFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Trial translate Microsoft Word documents, rtf, txt, odt without conversation. Translate only first page or 1000 symbols.
        api_response = api_instance.document_trial_post(text_document_file_request=text_document_file_request)
        print("The response of TranslationApi->document_trial_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->document_trial_post: %s\n" % e)
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

# **hc_get**
> HealthCheckStatus hc_get()

Health check for all services.

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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)

    try:
        # Health check for all services.
        api_response = api_instance.hc_get()
        print("The response of TranslationApi->hc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->hc_get: %s\n" % e)
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
> StatusResponse html_post(html_file_request=html_file_request)

Translate HTML files

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.html_file_request import HtmlFileRequest
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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    html_file_request = groupdocs-translation-cloud.HtmlFileRequest() # HtmlFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate HTML files
        api_response = api_instance.html_post(html_file_request=html_file_request)
        print("The response of TranslationApi->html_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->html_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **html_file_request** | [**HtmlFileRequest**](HtmlFileRequest.md)| String in body of request, containing JSON with parameters for translation. | [optional] 

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

# **hugo_get**
> CloudHugoResponse hugo_get(id=id)

Get hugo syntax structure from markdown file

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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    id = 'id_example' # str | id from PostHugo> (optional)

    try:
        # Get hugo syntax structure from markdown file
        api_response = api_instance.hugo_get(id=id)
        print("The response of TranslationApi->hugo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->hugo_get: %s\n" % e)
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
> StatusResponse hugo_post(hugo_request=hugo_request)

Run hugo syntax structure analyzing from markdown file

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.hugo_request import HugoRequest
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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    hugo_request = groupdocs-translation-cloud.HugoRequest() # HugoRequest |  (optional)

    try:
        # Run hugo syntax structure analyzing from markdown file
        api_response = api_instance.hugo_post(hugo_request=hugo_request)
        print("The response of TranslationApi->hugo_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->hugo_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hugo_request** | [**HugoRequest**](HugoRequest.md)|  | [optional] 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_to_file_post**
> StatusResponse image_to_file_post(image_to_file_request=image_to_file_request)

Translate image or scanned pdf and return file

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.image_to_file_request import ImageToFileRequest
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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    image_to_file_request = groupdocs-translation-cloud.ImageToFileRequest() # ImageToFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate image or scanned pdf and return file
        api_response = api_instance.image_to_file_post(image_to_file_request=image_to_file_request)
        print("The response of TranslationApi->image_to_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->image_to_file_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_to_file_request** | [**ImageToFileRequest**](ImageToFileRequest.md)| String in body of request, containing JSON with parameters for translation. | [optional] 

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
> StatusResponse image_to_text_post(image_to_text_request=image_to_text_request)

Translate text on image or scanned pdf

### Example

* OAuth Authentication (JWT):
```python
import time
import os
import groupdocs-translation-cloud
from groupdocs-translation-cloud.models.image_to_text_request import ImageToTextRequest
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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    image_to_text_request = groupdocs-translation-cloud.ImageToTextRequest() # ImageToTextRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate text on image or scanned pdf
        api_response = api_instance.image_to_text_post(image_to_text_request=image_to_text_request)
        print("The response of TranslationApi->image_to_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->image_to_text_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_to_text_request** | [**ImageToTextRequest**](ImageToTextRequest.md)| String in body of request, containing JSON with parameters for translation. | [optional] 

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

# **languages_get**
> List[LanguagePairData] languages_get()

Return list of available language pairs

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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)

    try:
        # Return list of available language pairs
        api_response = api_instance.languages_get()
        print("The response of TranslationApi->languages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->languages_get: %s\n" % e)
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

Translate Markdown files

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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    markdown_file_request = groupdocs-translation-cloud.MarkdownFileRequest() # MarkdownFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate Markdown files
        api_response = api_instance.markdown_post(markdown_file_request=markdown_file_request)
        print("The response of TranslationApi->markdown_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->markdown_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **markdown_file_request** | [**MarkdownFileRequest**](MarkdownFileRequest.md)| String in body of request, containing JSON with parameters for translation. | [optional] 

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

Translate pdf files

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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    pdf_file_request = groupdocs-translation-cloud.PdfFileRequest() # PdfFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate pdf files
        api_response = api_instance.pdf_post(pdf_file_request=pdf_file_request)
        print("The response of TranslationApi->pdf_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->pdf_post: %s\n" % e)
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

# **pdf_trial_post**
> StatusResponse pdf_trial_post(pdf_file_request=pdf_file_request)

Trial pdf translation. Translate only first page without conversion to another format.

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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    pdf_file_request = groupdocs-translation-cloud.PdfFileRequest() # PdfFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Trial pdf translation. Translate only first page without conversion to another format.
        api_response = api_instance.pdf_trial_post(pdf_file_request=pdf_file_request)
        print("The response of TranslationApi->pdf_trial_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->pdf_trial_post: %s\n" % e)
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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    presentation_file_request = groupdocs-translation-cloud.PresentationFileRequest() # PresentationFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate Microsoft PowerPoint presentations, odp
        api_response = api_instance.presentation_post(presentation_file_request=presentation_file_request)
        print("The response of TranslationApi->presentation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->presentation_post: %s\n" % e)
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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    resx_file_request = groupdocs-translation-cloud.ResxFileRequest() # ResxFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate RESX files
        api_response = api_instance.resx_post(resx_file_request=resx_file_request)
        print("The response of TranslationApi->resx_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->resx_post: %s\n" % e)
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

# **spreadsheet_post**
> StatusResponse spreadsheet_post(spreadsheet_file_request=spreadsheet_file_request)

Translate Microsoft Excel workbooks, ods

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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    spreadsheet_file_request = groupdocs-translation-cloud.SpreadsheetFileRequest() # SpreadsheetFileRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate Microsoft Excel workbooks, ods
        api_response = api_instance.spreadsheet_post(spreadsheet_file_request=spreadsheet_file_request)
        print("The response of TranslationApi->spreadsheet_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->spreadsheet_post: %s\n" % e)
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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    text_request = groupdocs-translation-cloud.TextRequest() # TextRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Translate text
        api_response = api_instance.text_post(text_request=text_request)
        print("The response of TranslationApi->text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->text_post: %s\n" % e)
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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/translation/text response

    try:
        # Return text translation status.  Also return translated text if translation was successful
        api_response = api_instance.text_request_id_get(request_id)
        print("The response of TranslationApi->text_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->text_request_id_get: %s\n" % e)
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

# **text_trial_post**
> StatusResponse text_trial_post(text_request=text_request)

Trial translate text. Translate only 1000 symbols.

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
    api_instance = groupdocs-translation-cloud.TranslationApi(api_client)
    text_request = groupdocs-translation-cloud.TextRequest() # TextRequest | String in body of request, containing JSON with parameters for translation. (optional)

    try:
        # Trial translate text. Translate only 1000 symbols.
        api_response = api_instance.text_trial_post(text_request=text_request)
        print("The response of TranslationApi->text_trial_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranslationApi->text_trial_post: %s\n" % e)
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

