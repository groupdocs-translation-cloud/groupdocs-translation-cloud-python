# coding: utf-8
# """Copyright
# --------------------------------------------------------------------------------------------------------------------
# <copyright company="Aspose" file="translate_document.py">
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
* Creates body for document translation request
"""
import json
import ast


def list_coder(list_to_decode):
    tmp_list = []
    for i in list_to_decode:
        tmp_list.append(str(i) + ': ' + json.dumps(list_to_decode[0]))
    return "{" + ", ".join(tmp_list) + "}"


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
        'Masters': 'bool',
        'Elements': 'list',
        'Separator': 'str',
        'Codelist': 'str',
        'Frontlists': 'str',
        'Optimizepdffontsize': 'bool'
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
        'Frontlists': 'frontlists',
        'Optimizepdffontsize': 'optimizepdffontsize'
    }



    def __init__(self, pair, _format, outformat, storage, name, folder, savepath, savefile, masters, elements,
                 separator=",", codelist={}, frontlists={}, optimizepdffontsize=False):
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
        :param str Separator:  delimiter for CSV files
        :param dict {str: list(str)} Codelist: dictionary of short code syntax in Hugo to translate, where the key is short code name, and value is a list of parameters names that require translation
        :param dict {int: list(list(str))} Frontlists: dictionary of front matter syntax in Hugo to translate, where the key is zero based front matter index and value is list of paths to values that require translation, each path is also a list
        :param bool Optimizepdffontsize: if true, font size will be selected, that translation will fit paragraph rectangle
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
        self.Codelist = codelist
        self.Frontlists = frontlists
        self.Optimizepdffontsize = optimizepdffontsize

    def to_string(self):

        request = [{"pair": self.Pair, "format": self.Format, "outformat": self.Outformat, "storage": self.Storage,
                    "name": self.Name, "folder": self.Folder, "savepath": self.Savepath, "savefile": self.Savefile,
                    "masters": self.Masters, "elements": self.Elements, "separator": self.Separator, "optimizepdffontsize": self.Optimizepdffontsize}]
        codelist = '"shortcodedict": ' + list_coder(self.Codelist)
        frontlists = '"frontmatterdict": ' + list_coder(self.Frontlists)
        return ", ".join([json.dumps(request)[:-2], codelist, frontlists]) + "}]"
