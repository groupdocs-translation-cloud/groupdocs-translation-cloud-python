# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="document_response.py">
# Copyright (c) 2022 GroupDocs.Translation for Cloud
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


class HugoResponse(BaseModel):
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
        'frontmatter': 'str',
        'shortcode': 'str'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'frontmatter': 'frontmatter',
        'shortcode': 'shortcode'
    }

    def __init__(self, status="", message="", frontmatter={}, shortcode={}):
        """

        :type status: str
        :type message: str
        :type frontmatter: dict[int: list(list(str)))]
        :type shortcode: dict[int: list(str)}]
        """
        self._status = status  # type: str
        self._message = message  # type: str
        self._frontmatter = frontmatter   # type: dict[int: list(list(str)))]
        self._shortcode = shortcode   # type: dict[int: list(str)}]

    @property
    def status(self):
        """Gets status
        :return: status.
        :type: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets status
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
        """Sets response message.
        :param message: message.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def frontmatter(self):
        """Gets frontmatter
        :return: frontmatter.
        :type: dict
        """
        return self._frontmatter

    @frontmatter.setter
    def frontmatter(self, frontmatter):
        """Sets frontmatter.
        :param frontmatter: frontmatter.
        :type: dict
        """
        # if frontmatter is None:
        #     raise ValueError("Invalid value for `frontmatter`, must not be `None`")

        self._frontmatter = frontmatter

    @property
    def shortcode(self):
        """Gets shortcode
        :return: shortcode.
        :type: dict
        """
        return self._shortcode

    @shortcode.setter
    def shortcode(self, shortcode):
        """Sets shortcode.
        :param shortcode: shortcode.
        :type: dict
        """
        # if shortcode is None:
        #     raise ValueError("Invalid value for `shortcode`, must not be `None`")

        self._shortcode = shortcode
