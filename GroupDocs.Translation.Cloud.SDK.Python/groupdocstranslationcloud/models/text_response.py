# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="text_response.py">
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


class TextResponse(BaseModel):
    """
    Attributes:
      model_types (dict):   The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'status': 'str',
        'message': 'str',
        'translation': 'str'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'translation': 'translation'
    }

    def __init__(self, status="", message="", translation=""):
        """

        :type status: str
        :type message: str
        :type translation: str
        """
        self._status = status  # type: str
        self._message = message  # type: str
        self._translation = translation #type: str

    @property
    def status(self):
        """Operation status
        :return: status.
        :type: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Operation status
        :param status: status.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def message(self):
        """Gets response message
        :return: message.
        :type: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets rersponse message.
        :param message: message.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def translation(self):
        """
        Gets translated text
        :return: translated text
        :type: str
        """
        return self._translation

    @translation.setter
    def translation(self, translation):
        """
        Sets translated text
        :param translation: translated text
        :type: str
        """
        if translation is None:
            raise ValueError("Invalid value for `translation`, must not be `None`")
        self._translation = translation

