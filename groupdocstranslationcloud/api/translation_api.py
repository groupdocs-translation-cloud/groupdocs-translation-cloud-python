# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="translation_api.py">
# Copyright (c) 2020 GroupDocs.Translation for Cloud
# </copyright>
# <summary>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# </summary>
# --------------------------------------------------------------------------------------------------------------------
# """

from __future__ import absolute_import

from typing import List, Tuple

from groupdocstranslationcloud.models import DocumentResponse, TextResponse
from groupdocstranslationcloud.api_client import ApiClient

# python 2 and python 3 compatibility library
import six


class TranslationApi(object):

    def __init__(self, config=None):
        if config is None:
            api_client = ApiClient()
        else:
            api_client = ApiClient(config)
        self.api_client = api_client

    ##########################################################
    #                  Translation API
    ##########################################################

    def post_translate_text(self, body, **kwargs):
        """  Translate plain text provided in body's request

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :return: TextResponse . If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__post_translate_text(body, **kwargs)
        else:
            (data) = self.__post_translate_text(body, **kwargs)
            return data

    def __post_translate_text(self, body, **kwargs):
        #assert body is not None
        """ Translate plain text provided in body's request

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :return: TextResponse . If the method is called asynchronously, returns the request thread.
        """

        all_params = ['async_req', '_return_http_data_only', '_preload_content', '_request_timeout']

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_convert_document_to_image" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path_params = {}  # uri params #

        query_params = {}  # content query params

        header_params = {}
        form_params = {}
        local_var_files = {}
        body_params = body

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/text', 'POST', path_params, query_params, header_params,
                                        body=body, post_params=form_params, files=local_var_files,
                                        response_type='TextResponse', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def post_translate_document(self, body, **kwargs):
        """  Translate document on Aspose Cloud Storage and save it

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :return: DocumentResponse . If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__post_translate_document(body, **kwargs)
        else:
            (data) = self.__post_translate_document(body, **kwargs)
            return data

    def __post_translate_document(self, body, **kwargs):
        assert body is not None
        """ Translate document on Aspose Cloud Storage and save it

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :return: DocumentResponse . If the method is called asynchronously, returns the request thread.
        """

        all_params = ['async_req', '_return_http_data_only', '_preload_content', '_request_timeout']

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_convert_document_to_image" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path_params = {}  # uri params #
        query_params = {}  # content query params
        header_params = {}
        form_params = {}
        local_var_files = {}
        body_params = body

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/document', 'POST', path_params, query_params, header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='DocumentResponse', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def get_run_health_check(self, **kwargs):
        """ Run health check to test correct work of service

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :return: DocumentResponse . If the method is called asynchronously, returns the request thread.
        """

        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_run_health_check(**kwargs)
        else:
            (data) = self.__get_run_health_check(**kwargs)
            return data

    def __get_run_health_check (self, **kwargs):
        """ Run health check to test correct work of service

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :return: DocumentResponse . If the method is called asynchronously, returns the request thread.
        """
        all_params = ['async_req', '_return_http_data_only', '_preload_content', '_request_timeout']

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_convert_document_to_image" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}
        path_params = {}  # uri params #
        query_params = {}  # content query params
        header_params = {}
        form_params = {}
        local_var_files = {}
        body_params = {}

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/hc', 'GET', path_params, query_params, header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='DocumentResponse', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

