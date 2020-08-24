# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="storage_api.py">
# Copyright (c) 2020 GroupDocs.Translation for Cloud
# </copyright>
# <summary>
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
# python 2 and python 3 compatibility library
import six

from groupdocstranslationcloud.api_client import ApiClient


class StorageApi(object):

    def __init__(self, config=None):
        if config is None:
            api_client = ApiClient()
        else:
            api_client = ApiClient(config)
        self.api_client = api_client

    # **************************************************
    #                  Storage Api
    # **************************************************

    def get_disc_usage(self, **kwargs):
        """Get disc usage

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str storage_name: Storage name
        :return: DiscUsage. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_disc_usage_with_http_info(**kwargs)
        else:
            (data) = self.__get_disc_usage_with_http_info(**kwargs)
            return data

    def __get_disc_usage_with_http_info(self, **kwargs):
        """Get disc usage

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str storage_name: Storage name
        :return: DiscUsage. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['storage_name']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_disc_usage" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'storage_name' in params:
            query_params.append(('storageName', params['storage_name']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/storage/disc', 'GET', path_params, query_params, header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='DiscUsage', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def get_file_versions(self, path, **kwargs):
        """Get file versions

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: File path e.g. '/file.ext' (required)
        :param str storage_name: Storage name
        :return: FileVersions. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_file_versions_with_http_info(path, **kwargs)
        else:
            (data) = self.__get_file_versions_with_http_info(path, **kwargs)
            return data

    def __get_file_versions_with_http_info(self, path, **kwargs):
        """Get file versions

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: File path e.g. '/file.ext' (required)
        :param str storage_name: Storage name
        :return: FileVersions. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['path', 'storage_name']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file_versions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if ('path' not in params or
                params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `get_file_versions`")

        collection_formats = {}

        path_params = {}
        if 'path' in params:
            path_params['path'] = params['path']

        query_params = []
        if 'storage_name' in params:
            query_params.append(('storageName', params['storage_name']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/storage/version/{path}', 'GET', path_params, query_params, header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='FileVersions', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def object_exists(self, path, **kwargs):
        """Check if file or folder exists

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: File or folder path e.g. '/file.ext' or '/folder' (required)
        :param str storage_name: Storage name
        :param str version_id: File version ID
        :return: ObjectExist. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__object_exists_with_http_info(path, **kwargs)
        else:
            (data) = self.__object_exists_with_http_info(path, **kwargs)
            return data

    def __object_exists_with_http_info(self, path, **kwargs):
        """Check if file or folder exists

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: File or folder path e.g. '/file.ext' or '/folder' (required)
        :param str storage_name: Storage name
        :param str version_id: File version ID
        :return: ObjectExist. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['path', 'storage_name', 'version_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method object_exists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if ('path' not in params or
                params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `object_exists`")

        collection_formats = {}

        path_params = {}
        if 'path' in params:
            path_params['path'] = params['path']

        query_params = []
        if 'storage_name' in params:
            query_params.append(('storageName', params['storage_name']))
        if 'version_id' in params:
            query_params.append(('versionId', params['version_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/storage/exist/{path}', 'GET', path_params, query_params, header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='ObjectExist', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def storage_exists(self, storage_name, **kwargs):
        """Check if storage exists

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str storage_name: Storage name (required)
        :return: StorageExist. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__storage_exists_with_http_info(storage_name, **kwargs)
        else:
            (data) = self.__storage_exists_with_http_info(storage_name, **kwargs)
            return data

    def __storage_exists_with_http_info(self, storage_name, **kwargs):
        """Check if storage exists

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str storage_name: Storage name (required)
        :return: StorageExist. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['storage_name']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method storage_exists" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'storage_name' is set
        if ('storage_name' not in params or
                params['storage_name'] is None):
            raise ValueError("Missing the required parameter `storage_name` when calling `storage_exists`")

        collection_formats = {}

        path_params = {}
        if 'storage_name' in params:
            path_params['storageName'] = params['storage_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/storage/{storageName}/exist', 'GET', path_params, query_params,
                                        header_params, body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='StorageExist', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    # **************************************************
    #                  File Api
    # **************************************************

    def copy_file(self, src_path, dest_path, **kwargs):
        """Copy file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str src_path: Source file path e.g. '/folder/file.ext' (required)
        :param str dest_path: Destination file path (required)
        :param str src_storage_name: Source storage name
        :param str dest_storage_name: Destination storage name
        :param str version_id: File version ID to copy
        :return: None. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__copy_file_with_http_info(src_path, dest_path, **kwargs)
        else:
            (data) = self.__copy_file_with_http_info(src_path, dest_path, **kwargs)
            return data

    def __copy_file_with_http_info(self, src_path, dest_path, **kwargs):
        """Copy file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str src_path: Source file path e.g. '/folder/file.ext' (required)
        :param str dest_path: Destination file path (required)
        :param str src_storage_name: Source storage name
        :param str dest_storage_name: Destination storage name
        :param str version_id: File version ID to copy
        :return: None. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['src_path', 'dest_path', 'src_storage_name', 'dest_storage_name', 'version_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method copy_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'src_path' is set
        if ('src_path' not in params or
                params['src_path'] is None):
            raise ValueError("Missing the required parameter `src_path` when calling `copy_file`")
        # verify the required parameter 'dest_path' is set
        if ('dest_path' not in params or
                params['dest_path'] is None):
            raise ValueError("Missing the required parameter `dest_path` when calling `copy_file`")

        collection_formats = {}

        path_params = {}
        if 'src_path' in params:
            path_params['srcPath'] = params['src_path']

        query_params = []
        if 'dest_path' in params:
            query_params.append(('destPath', params['dest_path']))
        if 'src_storage_name' in params:
            query_params.append(('srcStorageName', params['src_storage_name']))
        if 'dest_storage_name' in params:
            query_params.append(('destStorageName', params['dest_storage_name']))
        if 'version_id' in params:
            query_params.append(('versionId', params['version_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/storage/file/copy/{srcPath}', 'PUT', path_params, query_params,
                                        header_params, body=body_params, post_params=form_params, files=local_var_files,
                                        response_type=None, async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def delete_file(self, path, **kwargs):
        """Delete file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: File path e.g. '/folder/file.ext' (required)
        :param str storage_name: Storage name
        :param str version_id: File version ID to delete
        :return: None. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__delete_file_with_http_info(path, **kwargs)
        else:
            (data) = self.__delete_file_with_http_info(path, **kwargs)
            return data

    def __delete_file_with_http_info(self, path, **kwargs):
        """Delete file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: File path e.g. '/folder/file.ext' (required)
        :param str storage_name: Storage name
        :param str version_id: File version ID to delete
        :return: None. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['path', 'storage_name', 'version_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if ('path' not in params or
                params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `delete_file`")

        collection_formats = {}

        path_params = {}
        if 'path' in params:
            path_params['path'] = params['path']

        query_params = []
        if 'storage_name' in params:
            query_params.append(('storageName', params['storage_name']))
        if 'version_id' in params:
            query_params.append(('versionId', params['version_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/storage/file/{path}', 'DELETE', path_params, query_params, header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type=None, async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def download_file(self, path, **kwargs):
        """Download file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: File path e.g. '/folder/file.ext' (required)
        :param str storage_name: Storage name
        :param str version_id: File version ID to download
        :return: file. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__download_file_with_http_info(path, **kwargs)
        else:
            (data) = self.__download_file_with_http_info(path, **kwargs)
            return data

    def __download_file_with_http_info(self, path, **kwargs):
        """Download file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: File path e.g. '/folder/file.ext' (required)
        :param str storage_name: Storage name
        :param str version_id: File version ID to download
        :return: file. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['path', 'storage_name', 'version_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if ('path' not in params or
                params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `download_file`")

        collection_formats = {}

        path_params = {}
        if 'path' in params:
            path_params['path'] = params['path']

        query_params = []
        if 'storage_name' in params:
            query_params.append(('storageName', params['storage_name']))
        if 'version_id' in params:
            query_params.append(('versionId', params['version_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/storage/file/{path}', 'GET', path_params, query_params, header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='file', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def move_file(self, src_path, dest_path, **kwargs):
        """Move file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str src_path: Source file path e.g. '/src.ext' (required)
        :param str dest_path: Destination file path e.g. '/dest.ext' (required)
        :param str src_storage_name: Source storage name
        :param str dest_storage_name: Destination storage name
        :param str version_id: File version ID to move
        :return: None. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__move_file_with_http_info(src_path, dest_path, **kwargs)
        else:
            (data) = self.__move_file_with_http_info(src_path, dest_path, **kwargs)
            return data

    def __move_file_with_http_info(self, src_path, dest_path, **kwargs):
        """Move file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str src_path: Source file path e.g. '/src.ext' (required)
        :param str dest_path: Destination file path e.g. '/dest.ext' (required)
        :param str src_storage_name: Source storage name
        :param str dest_storage_name: Destination storage name
        :param str version_id: File version ID to move
        :return: None. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['src_path', 'dest_path', 'src_storage_name', 'dest_storage_name', 'version_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method move_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'src_path' is set
        if ('src_path' not in params or
                params['src_path'] is None):
            raise ValueError("Missing the required parameter `src_path` when calling `move_file`")
        # verify the required parameter 'dest_path' is set
        if ('dest_path' not in params or
                params['dest_path'] is None):
            raise ValueError("Missing the required parameter `dest_path` when calling `move_file`")

        collection_formats = {}

        path_params = {}
        if 'src_path' in params:
            path_params['srcPath'] = params['src_path']

        query_params = []
        if 'dest_path' in params:
            query_params.append(('destPath', params['dest_path']))
        if 'src_storage_name' in params:
            query_params.append(('srcStorageName', params['src_storage_name']))
        if 'dest_storage_name' in params:
            query_params.append(('destStorageName', params['dest_storage_name']))
        if 'version_id' in params:
            query_params.append(('versionId', params['version_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/storage/file/move/{srcPath}', 'PUT', path_params, query_params,
                                        header_params, body=body_params, post_params=form_params, files=local_var_files,
                                        response_type=None, async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def upload_file(self, path, file, **kwargs):
        """Upload file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext If the content is multipart and path does not contains the file name it tries to get them from filename parameter from Content-Disposition header. (required)
        :param file file: File to upload (required)
        :param str storage_name: Storage name
        :return: FilesUploadResult. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__upload_file_with_http_info(path, file, **kwargs)
        else:
            (data) = self.__upload_file_with_http_info(path, file, **kwargs)
            return data

    def __upload_file_with_http_info(self, path, file, **kwargs):
        """Upload file

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext  If the content is multipart and path does not contains the file name it tries to get them from filename parameter  from Content-Disposition header. (required)
        :param file file: File to upload (required)
        :param str storage_name: Storage name
        :return: FilesUploadResult. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['path', 'file', 'storage_name']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if ('path' not in params or
                params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `upload_file`")
        # verify the required parameter 'file' is set
        if ('file' not in params or
                params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `upload_file`")

        collection_formats = {}

        path_params = {}
        if 'path' in params:
            path_params['path'] = params['path']

        query_params = []
        if 'storage_name' in params:
            query_params.append(('storageName', params['storage_name']))

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['File'] = params['file']

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['multipart/form-data'])

        return self.api_client.call_api('/storage/file/{path}', 'PUT', path_params, query_params, header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='FilesUploadResult', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    # **************************************************
    #                  Folder Api
    # **************************************************

    def copy_folder(self, src_path, dest_path, **kwargs):  # noqa: E501
        """Copy folder

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str src_path: Source folder path e.g. '/src' (required)
        :param str dest_path: Destination folder path e.g. '/dst' (required)
        :param str src_storage_name: Source storage name
        :param str dest_storage_name: Destination storage name
        :return: None. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__copy_folder_with_http_info(src_path, dest_path, **kwargs)
        else:
            (data) = self.__copy_folder_with_http_info(src_path, dest_path, **kwargs)
            return data

    def __copy_folder_with_http_info(self, src_path, dest_path, **kwargs):
        """Copy folder

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str src_path: Source folder path e.g. '/src' (required)
        :param str dest_path: Destination folder path e.g. '/dst' (required)
        :param str src_storage_name: Source storage name
        :param str dest_storage_name: Destination storage name
        :return: None. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['src_path', 'dest_path', 'src_storage_name', 'dest_storage_name']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method copy_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'src_path' is set
        if ('src_path' not in params or
                params['src_path'] is None):
            raise ValueError("Missing the required parameter `src_path` when calling `copy_folder`")
        # verify the required parameter 'dest_path' is set
        if ('dest_path' not in params or
                params['dest_path'] is None):
            raise ValueError("Missing the required parameter `dest_path` when calling `copy_folder`")

        collection_formats = {}

        path_params = {}
        if 'src_path' in params:
            path_params['srcPath'] = params['src_path']

        query_params = []
        if 'dest_path' in params:
            query_params.append(('destPath', params['dest_path']))
        if 'src_storage_name' in params:
            query_params.append(('srcStorageName', params['src_storage_name']))
        if 'dest_storage_name' in params:
            query_params.append(('destStorageName', params['dest_storage_name']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/storage/folder/copy/{srcPath}', 'PUT', path_params, query_params,
                                        header_params, body=body_params, post_params=form_params, files=local_var_files,
                                        response_type=None, async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def create_folder(self, path, **kwargs):
        """Create the folder

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: Folder path to create e.g. 'folder_1/folder_2/' (required)
        :param str storage_name: Storage name
        :return: None. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__create_folder_with_http_info(path, **kwargs)
        else:
            (data) = self.__create_folder_with_http_info(path, **kwargs)
            return data

    def __create_folder_with_http_info(self, path, **kwargs):
        """Create the folder

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: Folder path to create e.g. 'folder_1/folder_2/' (required)
        :param str storage_name: Storage name
        :return: None. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['path', 'storage_name']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if ('path' not in params or
                params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `create_folder`")

        collection_formats = {}

        path_params = {}
        if 'path' in params:
            path_params['path'] = params['path']

        query_params = []
        if 'storage_name' in params:
            query_params.append(('storageName', params['storage_name']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/storage/folder/{path}', 'PUT', path_params, query_params, header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type=None, async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def delete_folder(self, path, **kwargs):
        """Delete folder

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: Folder path e.g. '/folder' (required)
        :param str storage_name: Storage name
        :param bool recursive: Enable to delete folders, subfolders and files
        :return: None. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__delete_folder_with_http_info(path, **kwargs)
        else:
            (data) = self.__delete_folder_with_http_info(path, **kwargs)
            return data

    def __delete_folder_with_http_info(self, path, **kwargs):
        """Delete folder

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param async_req bool
        :param str path: Folder path e.g. '/folder' (required)
        :param str storage_name: Storage name
        :param bool recursive: Enable to delete folders, subfolders and files
        :return: None. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['path', 'storage_name', 'recursive']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if ('path' not in params or
                params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `delete_folder`")

        collection_formats = {}

        path_params = {}
        if 'path' in params:
            path_params['path'] = params['path']

        query_params = []
        if 'storage_name' in params:
            query_params.append(('storageName', params['storage_name']))
        if 'recursive' in params:
            query_params.append(('recursive', params['recursive']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/storage/folder/{path}', 'DELETE', path_params, query_params,
                                        header_params, body=body_params, post_params=form_params, files=local_var_files,
                                        response_type=None, async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def get_files_list(self, path, **kwargs):
        """Get all files and folders within a folder

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: Folder path e.g. '/folder' (required)
        :param str storage_name: Storage name
        :return: FilesList. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__get_files_list_with_http_info(path, **kwargs)
        else:
            (data) = self.__get_files_list_with_http_info(path, **kwargs)
            return data

    def __get_files_list_with_http_info(self, path, **kwargs):
        """Get all files and folders within a folder

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str path: Folder path e.g. '/folder' (required)
        :param str storage_name: Storage name
        :return: FilesList. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['path', 'storage_name']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_files_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'path' is set
        if ('path' not in params or
                params['path'] is None):
            raise ValueError("Missing the required parameter `path` when calling `get_files_list`")

        collection_formats = {}

        path_params = {}
        if 'path' in params:
            path_params['path'] = params['path']

        query_params = []
        if 'storage_name' in params:
            query_params.append(('storageName', params['storage_name']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/storage/folder/{path}', 'GET', path_params, query_params, header_params,
                                        body=body_params, post_params=form_params, files=local_var_files,
                                        response_type='FilesList', async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))

    def move_folder(self, src_path, dest_path, **kwargs):
        """Move folder

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str src_path: Folder path to move e.g. '/folder' (required)
        :param str dest_path: Destination folder path to move to e.g '/dst' (required)
        :param str src_storage_name: Source storage name
        :param str dest_storage_name: Destination storage name
        :return: None. If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.__move_folder_with_http_info(src_path, dest_path, **kwargs)
        else:
            (data) = self.__move_folder_with_http_info(src_path, dest_path, **kwargs)
            return data

    def __move_folder_with_http_info(self, src_path, dest_path, **kwargs):
        """Move folder

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        :param bool async_req: Asynchronous request
        :param str src_path: Folder path to move e.g. '/folder' (required)
        :param str dest_path: Destination folder path to move to e.g '/dst' (required)
        :param str src_storage_name: Source storage name
        :param str dest_storage_name: Destination storage name
        :return: None. If the method is called asynchronously, returns the request thread.
        """

        all_params = ['src_path', 'dest_path', 'src_storage_name', 'dest_storage_name']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method move_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'src_path' is set
        if ('src_path' not in params or
                params['src_path'] is None):
            raise ValueError("Missing the required parameter `src_path` when calling `move_folder`")
        # verify the required parameter 'dest_path' is set
        if ('dest_path' not in params or
                params['dest_path'] is None):
            raise ValueError("Missing the required parameter `dest_path` when calling `move_folder`")

        collection_formats = {}

        path_params = {}
        if 'src_path' in params:
            path_params['srcPath'] = params['src_path']

        query_params = []
        if 'dest_path' in params:
            query_params.append(('destPath', params['dest_path']))
        if 'src_storage_name' in params:
            query_params.append(('srcStorageName', params['src_storage_name']))
        if 'dest_storage_name' in params:
            query_params.append(('destStorageName', params['dest_storage_name']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        return self.api_client.call_api('/storage/folder/move/{srcPath}', 'PUT', path_params, query_params,
                                        header_params, body=body_params, post_params=form_params, files=local_var_files,
                                        response_type=None, async_req=params.get('async_req'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        collection_formats=collection_formats,
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'))
