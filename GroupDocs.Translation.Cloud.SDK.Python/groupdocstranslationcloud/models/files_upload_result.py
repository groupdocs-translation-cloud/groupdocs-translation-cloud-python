# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="files_upload_result.py">
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

from groupdocstranslationcloud.models import BaseModel


class FilesUploadResult(BaseModel):
    """
    Attributes:
      model_types (dict):   The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'uploaded': 'list[str]',
        'errors': 'list[Error]'
    }

    attribute_map = {
        'uploaded': 'uploaded',
        'errors': 'errors'
    }

    def __init__(self, uploaded=None, errors=None):

        self._uploaded = None
        self._errors = None

        if uploaded is not None:
            self.uploaded = uploaded
        if errors is not None:
            self.errors = errors

    @property
    def uploaded(self):
        """Gets the uploaded of this FilesUploadResult.

        List of uploaded file names

        :return: The uploaded of this FilesUploadResult.
        :rtype: list[str]
        """
        return self._uploaded

    @uploaded.setter
    def uploaded(self, uploaded):
        """Sets the uploaded of this FilesUploadResult.

        List of uploaded file names

        :param uploaded: The uploaded of this FilesUploadResult.
        :type: list[str]
        """

        self._uploaded = uploaded

    @property
    def errors(self):
        """Gets the errors of this FilesUploadResult.

        List of errors.

        :return: The errors of this FilesUploadResult.
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this FilesUploadResult.

        List of errors.

        :param errors: The errors of this FilesUploadResult.
        :type: list[Error]
        """

        self._errors = errors
