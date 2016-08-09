# -*- coding:utf-8 -*-
import os

from urllib import request


class DownPhotos(object):
    def __init__(self, urls, path):
        self.urls = urls
        self.path = path
    def storePath(self,url):
        self.filePath='./'+self.path+url.split('/')[-1]
        #return self.filePath
    def save(self):
        for imgUrl in self.urls:
            self.storePath(imgUrl)
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            if not os.path.exists(self.filePath):
                request.urlretrieve(imgUrl, self.filePath)
            else:
                print('File Exist')
