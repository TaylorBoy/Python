# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import re

# 糗事百科爬虫类
class SQBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # Initial headers
        self.headers = {'User-Agent' : self.user_agent }
        # 存放段子, 每一个元素为每一页的段子
        self.storages = []
        # If continue running
        self.enable = False

    # 传入索引, 获取页面代码
    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            # 构建请求的 request
            reqst = urllib.request.Request(url, headers=self.headers)
            # 利用 urlopen 获取页面代码
            with urllib.request.urlopen(reqst) as response:
                # 将页面转化为 utf-8 编码
                pageCode = response.read().decode('utf-8')
                return pageCode

        except urllib.request.URLError as e:
            if hasattr(e, 'reason'):
                print('连接糗事百科失败, 错误原因: ', e.reason)
                return None

    # 传入索引, 获取本页段子列表
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print('页面加载失败...')
            return None
        pattern = re.compile('author.*?<h2>(.*?)</h2>.*?contentHerf.*?<span>(.*?)</span>' +
                             '.*?<div class="stats">.*?class="number">(.*?)</i>.*?</div>', re.S)
        items = re.findall(pattern, pageCode)
        # 存储每个获取到的段子
        pageStorage = []
        for item in items:
            # 替换段子内容中的换行符
            br = re.compile('<br/>')
            text = re.sub(br, '\n', item[1])
            # 去掉空白符加入 pageStorage
            pageStorage.append([ item[2].strip(), item[0].strip(), text.strip() ])
            # strip 默认删除头尾空白符（包括'\n', '\r',  '\t',  ' ')
        return pageStorage

    # 加载并提取页面内容, 放到 storages 列表中
    def loadPage(self):
        #如果当前未看的页数少于 2 页, 则加载新一页
        if self.enable == True:
            if len(self.storages) < 2:
                # 获取新的一页
                pageStorage = self.getPageItems(self.pageIndex)
                if pageStorage:
                    self.storages.append(pageStorage)
                    self.pageIndex += 1

    # 每次打印一个段子
    def getOneStory(self, pageStorage, page):
        for story in pageStorage:
            choose = input()
            # 加载新页面 ?
            self.loadPage()
            if 'Q' == choose:
                self.enable = False
                return
            print('第%d页 %s赞. %s: \n%s *\n' % (page, story[1], story[0], story[2]))

    # Start
    def start(self):
        print('糗事百科获取中... Q 结束')
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.storages) > 0:
                # 获取一页的段子
                pageStories = self.storages[0]
                nowPage += 1
                # 将 storages 第一个元素以取出的元素删除
                del self.storages[0]
                self.getOneStory(pageStories, nowPage)

if __name__ == '__main__':
    spider = SQBK( )
    spider.start()
