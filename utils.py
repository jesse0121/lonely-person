#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# name: utils
# author: 王曦（ Wang Xi ）
# author_email: buaawangxi@buaa.edu.cn
# date: 2018/3/16
# time: 8:25
import os


path = 'F:\\DataFun\\DataBase\\Consuption_Data\\Source_Data\\Combined'


class Solution():
    def change_file_name(self, path):
        file_list = os.listdir(path)
        for file in file_list:
            os.rename(path+'\\'+file,
                      path+'\\'+file[:10])
        print('Done')
        return None


    def create_symlink(self, src, dist):
        """

        :param src: string or list
        :param dist: string
        :return: None
        """
        if isinstance(src, str):
            self._create_string_symlink(src, dist)
        if isinstance(src, list):
            for file in src:
                self._create_string_symlink(file, dist)

    def _create_string_symlink(self, src, dist):
        pass

