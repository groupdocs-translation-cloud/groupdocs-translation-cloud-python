# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="disc_usage.py">
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


class DiscUsage(BaseModel):

    """
    Attributes:
      model_types (dict):   The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    model_types = {
        'used_size': 'long',
        'total_size': 'long'
    }

    attribute_map = {
        'used_size': 'usedSize',
        'total_size': 'totalSize'
    }

    def __init__(self, used_size=None, total_size=None):

        self._used_size = None
        self._total_size = None

        self.used_size = used_size
        self.total_size = total_size

    @property
    def used_size(self):
        """Gets the used_size of this DiscUsage.

        Application used disc space.

        :return: The used_size of this DiscUsage.
        :rtype: long
        """
        return self._used_size

    @used_size.setter
    def used_size(self, used_size):
        """Sets the used_size of this DiscUsage.

        Application used disc space.

        :param used_size: The used_size of this DiscUsage.
        :type: long
        """
        if used_size is None:
            raise ValueError("Invalid value for `used_size`, must not be `None`")

        self._used_size = used_size

    @property
    def total_size(self):
        """Gets the total_size of this DiscUsage.

        Total disc space.

        :return: The total_size of this DiscUsage.
        :rtype: long
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this DiscUsage.

        Total disc space.

        :param total_size: The total_size of this DiscUsage.
        :type: long
        """
        if total_size is None:
            raise ValueError("Invalid value for `total_size`, must not be `None`")

        self._total_size = total_size
