# -*- coding: utf-8 -*-

"""
    auto rule template
    ~~~~
    :author:    LoRexxar <LoRexxar@gmail.com>
    :homepage:  https://github.com/LoRexxar/Kunlun-M
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2017 LoRexxar. All rights reserved
"""

from utils.api import *


class CVI_1007():
    """
    rule class
    """

    def __init__(self):

        self.svid = 1007
        self.language = "php"
        self.author = "LoRexxar/wufeifei"
        self.vulnerability = "RFI"
        self.description = "include等函数可能会导致任意文件包含，如果配置不当，甚至可能导致远程任意文件包含。"
        self.level = 8

        # status
        self.status = True

        # 部分配置
        self.match_mode = "function-param-regex"
        self.match = r"include|include_once|require|require_once|parsekit_compile_file|php_check_syntax|runkit_import|virtual"

        # for solidity
        self.match_name = None
        self.black_list = None

        # for chrome ext
        self.keyword = None

        # for regex
        self.unmatch = None

        self.vul_function = None

    def main(self, regex_string):
        """
        regex string input
        :regex_string: regex match string
        :return:
        """
        pass
