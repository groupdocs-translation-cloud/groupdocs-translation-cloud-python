# groupdocs_translation_cloud.SwaggerApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/translation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**swagger_spec_get**](SwaggerApi.md#swagger_spec_get) | **GET** /swagger/spec | 


# **swagger_spec_get**
> swagger_spec_get(is_yaml=is_yaml, serialaize_as_v2=serialaize_as_v2)



### Example

* OAuth Authentication (JWT):

```python
import groupdocs_translation_cloud
from groupdocs_translation_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/translation
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_translation_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/translation"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_translation_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_translation_cloud.SwaggerApi(api_client)
    is_yaml = False # bool |  (optional) (default to False)
    serialaize_as_v2 = False # bool |  (optional) (default to False)

    try:
        api_instance.swagger_spec_get(is_yaml=is_yaml, serialaize_as_v2=serialaize_as_v2)
    except Exception as e:
        print("Exception when calling SwaggerApi->swagger_spec_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_yaml** | **bool**|  | [optional] [default to False]
 **serialaize_as_v2** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

