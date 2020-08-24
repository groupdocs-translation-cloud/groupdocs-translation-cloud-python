# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="error_details.py">
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


class ErrorDetails(BaseModel):
    """
    Attributes:
      model_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'request_id': 'str',
        '_date': 'datetime'
    }

    attribute_map = {
        'request_id': 'RequestId',
        '_date': 'Date'
    }

    def __init__(self, request_id=None, _date=None):

        self._request_id = None
        self.__date = None

        if request_id is not None:
            self.request_id = request_id
        self._date = _date

    @property
    def request_id(self):
        """Gets the request_id of this ErrorDetails.

        The request id

        :return: The request_id of this ErrorDetails.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ErrorDetails.

        The request id

        :param request_id: The request_id of this ErrorDetails.
        :type: str
        """

        self._request_id = request_id

    @property
    def _date(self):
        """Gets the _date of this ErrorDetails.

        Date

        :return: The _date of this ErrorDetails.
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ErrorDetails.

        Date

        :param _date: The _date of this ErrorDetails.
        :type: datetime
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")

        self.__date = _date
