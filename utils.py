#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# name: utils
# author: 王曦（ Wang Xi ）
# author_email: buaawangxi@buaa.edu.cn
# date: 2018/3/16
# time: 8:25
import os


consumption_path = 'F:\\DataFun\\DataBase\\Consumption_Data\\Source_Data\\Combined'


class Solution:
    def change_file_name(self, path):
        """

        :param path: string
        :return:
        """
        file_list = os.listdir(path)
        for file in file_list:
            os.rename(path+'\\'+file,
                      path+'\\'+file[:10])
        print('Done')
        return None

    def create_symlink(self, src, dist):
        """

        :param src: string
        :param dist: string
        :return: None
        """
        file_list = os.listdir(src)
        for file in file_list:
            os.symlink(src+'\\'+file, dist+'\\'+file)
        print('Done')
        return None