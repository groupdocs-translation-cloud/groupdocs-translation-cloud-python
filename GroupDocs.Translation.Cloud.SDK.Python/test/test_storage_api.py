# coding: utf-8

# """
# --------------------------------------------------------------------------------------------------------------------
#  <copyright company="Aspose" file="test_storage_api.py">
#    Copyright (c) 2020 GroupDocs.Translation for Cloud
#  </copyright>
#  <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# --------------------------------------------------------------------------------------------------------------------
# """

from __future__ import absolute_import
import os
import unittest
import datetime
from test_helper import TestHelper


class TestStorageApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = TestHelper.storage

    # **************************************************
    #                  Test storage Api
    # **************************************************

    def test_get_disc_usage(self):
        """Test case for get_disc_usage

        Check the disk usage of the current account
        """
        res = self.api.get_disc_usage()
        res = res.to_dict()
        print(res)

        self.assertTrue('total_size' in res)
        self.assertTrue('used_size' in res)

        self.assertTrue(isinstance(res['total_size'], int))
        self.assertTrue(isinstance(res['used_size'], int))
        

    def test_object_exists(self):
        """Test case for object_exists

        Check if a specific file or folder exists
        """
        exist_folder = TestHelper.get_folder()

        res = self.api.object_exists(exist_folder)
        res = res.to_dict()

        self.assertTrue('exists' in res)
        self.assertTrue('is_folder' in res)

        self.assertTrue(isinstance(res['exists'], bool))
        self.assertTrue(isinstance(res['is_folder'], bool))

        self.assertTrue(res['exists'])
        self.assertTrue(res['is_folder'])

        non_exist_file = TestHelper.get_folder() + 'non_exist_file.gif'

        res = self.api.object_exists(non_exist_file)
        res = res.to_dict()

        self.assertFalse(res['exists'])
        self.assertFalse(res['is_folder'])

    def test_storage_exist(self):
        """Test case for storage_exist

        Check if storage exists
        """
        not_exist = "Not_exist_storage"
        res = self.api.storage_exists(not_exist)
        res = res.to_dict()

        self.assertTrue('exists' in res)
        self.assertTrue(isinstance(res['exists'], bool))

        self.assertFalse(res['exists'])

    def test_get_file_versions(self):
        """Test case for get_file_versions

        Get the file's versions list
        """
        # Prepare
        file_name = "test_file.docx"
        src = TestHelper.get_local_folder() + "/" + file_name
        dst = TestHelper.get_folder() + "/" + file_name

        res = self.api.upload_file(dst, src)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)

        res = self.api.upload_file(dst, src)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)

        res = self.api.upload_file(dst, src)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)

        res = self.api.get_file_versions(dst)
        self.assertTrue(isinstance(res.value, list))

        dictionary = res.to_dict()
        self.assertTrue(isinstance(dictionary, dict))


    # **************************************************
    #                  Test file Api
    # **************************************************

    def test_upload_file(self):
        """Test case for upload_file

        Upload a specific file
        """
        file_name = "test_file.docx"
        src = TestHelper.get_local_folder() + "/" + file_name
        dst = TestHelper.get_folder() + "/" + file_name

        result = self.api.upload_file(dst, src)
        self.assertTrue(len(result.uploaded) == 1)
        self.assertTrue(len(result.errors) == 0)

        # check file exists
        res = self.api.object_exists(dst)
        res = res.to_dict()

        self.assertTrue(res['exists'])
        self.assertFalse(res['is_folder'])

    def test_delete_file(self):
        """Test case for delete_file

        Remove a specific file
        """

        # upload file to storage
        file_name = "test_file.docx"
        src = TestHelper.get_local_folder() + "/" + file_name
        dst = TestHelper.get_folder() + "/" + file_name

        res = self.api.upload_file(dst, src)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)

        # delete file in the storage
        self.api.delete_file(dst)

    def test_download_file(self):
        """Test case for download_file

        Download a specific file
        """
        file_name = "test_file.docx"
        size = TestHelper.get_file_size(file_name)

        # put file to storage
        res = TestHelper.upload_file(file_name)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)

        download_file = TestHelper.get_folder() + "/" + file_name
        save_file = TestHelper.get_local_dest_folder() + "/" + "test_file.docx"

        src = self.api.download_file(download_file)

        TestHelper.move_file(src, save_file)

        self.assertTrue(os.path.getsize(save_file) == size)

    def test_copy_file(self):
        """Test case for copy_file

        Move a specific file
        """
        file_name = "test_file.docx"
        src = TestHelper.get_local_folder() + "/" + file_name
        remote_src = TestHelper.get_folder() + "/" + file_name

        # Put to the storage
        res = self.api.upload_file(remote_src, src)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)

        remote_dst = TestHelper.get_folder() + "/" + "test_file.docx"

        # Copy in the storage
        self.api.copy_file(remote_src, remote_dst)

        # Test dst file exist
        res = self.api.object_exists(remote_dst)
        self.assertTrue(res.exists)
        self.assertFalse(res.is_folder)

        # clear src and dst files
        self.api.delete_file(remote_src)
        self.api.delete_file(remote_dst)

    def test_move_file(self):
        """Test case for move_file

        Move a specific file
        """
        file_name = "test_file.docx"
        src = TestHelper.get_local_folder() + "/" + file_name
        remote_src = TestHelper.get_folder() + "/" + file_name

        # Put to the storage
        res = self.api.upload_file(remote_src, src)
        self.assertTrue(len(res.uploaded) == 1)
        self.assertTrue(len(res.errors) == 0)

        remote_dst = TestHelper.get_folder() + "/" + "test_file.docx"

        # Move in the storage
        self.api.move_file(remote_src, remote_dst)

        # Test dst file exist
        res = self.api.object_exists(remote_dst)
        self.assertTrue(res.exists)
        self.assertFalse(res.is_folder)

        # Test src file not exist
        res = self.api.object_exists(remote_src)
        self.assertFalse(res.exists)
        self.assertFalse(res.is_folder)

        # clear dst files
        self.api.delete_file(remote_dst)

    # **************************************************
    #                  Test folder Api
    # **************************************************

    def test_create_folder(self):
        """Test case for create_folder

        Create the folder
        """
        folder_name = "test_folder"
        self.api.create_folder(folder_name)

        # Checking if the folder has been created
        res = self.api.object_exists(folder_name)
        self.assertTrue(res.exists)
        self.assertTrue(res.is_folder)

        # Delete folder
        self.api.delete_folder(folder_name)

        # Checking if the folder has been deleted
        res = self.api.object_exists(folder_name)
        self.assertFalse(res.exists)
        self.assertFalse(res.is_folder)

    def test_delete_folder(self):
        """Test case for delete_folder

        Remove a specific folder
        """
        # Create test folder
        folder_name = "tmp_folder"
        self.api.create_folder(folder_name)

        # Checking if the folder has been created
        res = self.api.object_exists(folder_name)
        self.assertTrue(res.exists)
        self.assertTrue(res.is_folder)

        # Delete folder
        self.api.delete_folder(folder_name)

        # Checking if the folder has been deleted
        res = self.api.object_exists(folder_name)
        self.assertFalse(res.exists)
        self.assertFalse(res.is_folder)

    def test_get_files_list(self):
        """Test case for get_files_list

        Get the file listing of a specific folder
        """
        folder = TestHelper.get_folder()
        res = self.api.get_files_list(folder)
        self.assertTrue(isinstance(res.value, list))

        one_file = res.value[0]
        self.assertTrue(isinstance(one_file.name, str))
        self.assertTrue(isinstance(one_file.is_folder, bool))
        self.assertTrue(isinstance(one_file.modified_date, datetime.datetime))
        self.assertTrue(isinstance(one_file.size, int))
        self.assertTrue(isinstance(one_file.path, str))

    def test_copy_folder(self):
        """Test case for copy_folder

        Copy a specific folder
        """
        src_folder = "test_copy_folder"

        # Prepare test, create folder
        self.api.create_folder(src_folder)

        # Checking if the folder has been created
        res = self.api.object_exists(src_folder)
        self.assertTrue(res.exists)
        self.assertTrue(res.is_folder)

        dst_folder = 'test_copied_folder'

        # Copy folder
        self.api.copy_folder(src_folder, dst_folder)

        # Checking is copied folder exist
        res = self.api.object_exists(dst_folder)
        self.assertTrue(res.exists)
        self.assertTrue(res.is_folder)

        # Checking is old folder exists
        res = self.api.object_exists(src_folder)
        self.assertTrue(res.exists)
        self.assertTrue(res.is_folder)

        # Delete src folder (cleanup)
        self.api.delete_folder(src_folder)

        # Checking is src folder not exists
        res = self.api.object_exists(src_folder)
        self.assertFalse(res.exists)
        self.assertFalse(res.is_folder)

        # Delete dst folder (cleanup)
        self.api.delete_folder(dst_folder)

        # Checking is dst folder not exists
        res = self.api.object_exists(dst_folder)
        self.assertFalse(res.exists)
        self.assertFalse(res.is_folder)

    def test_move_folder(self):
        """Test case for move_folder

        Move a specific folder
        """
        old_folder = "test_move_folder"

        # Prepare test, create folder
        self.api.create_folder(old_folder)

        # Checking if the folder has been created
        res = self.api.object_exists(old_folder)
        self.assertTrue(res.exists)
        self.assertTrue(res.is_folder)

        new_folder = 'test_moved_folder'

        # Move folder
        self.api.move_folder(old_folder, new_folder)

        # Checking is moved folder exist
        res = self.api.object_exists(new_folder)
        self.assertTrue(res.exists)
        self.assertTrue(res.is_folder)

        # Checking is old folder not exists
        res = self.api.object_exists(old_folder)
        self.assertFalse(res.exists)
        self.assertFalse(res.is_folder)

        # Delete new folder (cleanup)
        self.api.delete_folder(new_folder)

        # Checking is new folder not exists
        res = self.api.object_exists(new_folder)
        self.assertFalse(res.exists)
        self.assertFalse(res.is_folder)


if __name__ == '__main__':
    unittest.main()
