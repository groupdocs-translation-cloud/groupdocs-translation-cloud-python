# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="translate_text.py">
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

"""
 * Creates body for text translation request
"""
import json


class TranslateText:
    """
        Attributes:
          model_types (dict):   The key is attribute name
                                and the value is attribute type.
          attribute_map (dict): The key is attribute name
                                and the value is json key in definition.
        """
    model_types = {
        'Pair': 'str',
        'Text': 'str',
        'Origin': 'str',
        'Type': 'str'
    }

    attribute_map = {
        'Pair': 'pair',
        'Text': 'text',
        'Origin': 'origin',
        'Type': 'type'
    }

    def __init__(self, pair, text="text", type ="", origin="text"):
        """
        :param str pair: language pair
        :param str text: text to translate
        :param str typr: use "md" if text contains markdown syntax
        :param str origin: text origin source
        """
        self.Pair = pair  # language pair
        self.Text = text  # text to translate
        self.Origin = origin  # text origin source
        self.Type = type  # use "md" if text contains markdown syntax

    def to_string(self):
        request = [{"pair": self.Pair, "text": self.Text, "type": self.Type, "origin": self.Origin}]
        return json.dumps(request)
