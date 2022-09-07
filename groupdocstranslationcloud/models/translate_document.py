# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="translate_document.py">
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

"""
Represents information about strict regions to recognize text
"""
import json

class TranslateDocument:
    """
        Attributes:
          model_types (dict):   The key is attribute name
                                and the value is attribute type.
          attribute_map (dict): The key is attribute name
                                and the value is json key in definition.
        """
    model_types = {
        'Pair': 'str',
        'Format': 'str',
        'Outformat': 'str',
        'Storage': 'str',
        'Name': 'str',
        'Folder': 'str',
        'Savepath': 'str',
        'Savefile': 'str',
        'Masters':  'bool',
        'Elements': 'list',
        'Separator': 'str',
        'Codelist': 'list',
        'Frontlists': 'list'
    }

    attribute_map = {
        'Pair': 'pair',
        'Format': 'format',
        'Outformat': 'outformat',
        'Storage': 'storage',
        'Name': 'name',
        'Folder': 'folder',
        'Savepath': 'savepath',
        'Savefile': 'savefile',
        'Masters': 'masters',
        'Elements': 'elements',
        'Separator': 'separator',
        'Codelist': 'codelist',
        'Frontlists': 'frontlists'
    }

    def __init__(self, pair, _format, outformat, storage, name, folder, savepath, savefile, masters, elements, separator=",", codelist = null, frontlists = null):
        """
        :param str Pair: language pair
        :param str Format: document format, put file extension here
        :param str Outformat: translated document format, put file extension of desired format here
        :param str Storage: storage name, keep empty or put First Storage if default is used
        :param str Name: file name to translate
        :param str Folder: folder(s) where file is saved
        :param str Savepath: folder(s) where to save translated file
        :param str Savefile: translated file name
        :param bool Masters: if master slides in presentation should be translated
        :param list Elements: to translate only selected slides 
        """
        self.Pair = pair            
        self.Format = _format
        self.Outformat = outformat
        self.Storage = storage
        self.Name = name
        self.Folder = folder
        self.Savepath = savepath
        self.Savefile = savefile
        self.Masters = masters
        self.Elements = elements
        self.Separator = separator

    def to_string(self):
        request = [{"pair": self.Pair, "format": self.Format, "outformat": self.Outformat, "storage": self.Storage, 
                    "name": self.Name, "folder": self.Folder, "savepath": self.Savepath, "savefile": self.Savefile, 
                    "masters": self.Masters, "elements": self.Elements}]
        return  json.dumps(request)         
