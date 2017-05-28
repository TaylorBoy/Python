# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 抓取百度贴吧帖子
import urllib.request as urlq
import re

# 处理页面标签类
class ReplaceLabel:

    def __init__(self):
        # 去除img标签, 7位长空格
        self.removeImg = re.compile('<img.*?>| {7}|')
        # 去除超链接标签
        self.removeAddr = re.compile('<a.*?>|</a>')
        # 把换形标签转为换行\n
        self.replaceLine = re.compile('<tr>|<div>|</p>')
        # 将表格制表<td>替换为\t
        self.repalceTD = re.compile('<td>')
        # 把段落开头换为\n加两个空格
        self.replacePara = re.compile('<p.*?>')
        # 将换行符或双换行符替换为\n
        self.replaceBR = re.compile('<br><br>|<br>')
        # 将其余标签剔除
        self.removeExtraLabel = re.compile('<.*?>')

    def replaceLabel(self, x):
        x = re.sub(self.removeImg, '', x)
        x = re.sub(self.removeAddr, '', x)
        x = re.sub(self.replaceLine, '\n', x)
        x = re.sub(self.repalceTD, '\t', x)
        x = re.sub(self.replacePara, '\n    ', x)
        x = re.sub(self.replaceBR, '\n', x)
        x = re.sub(self.removeExtraLabel, '', x)
        # strip() 将首尾多余空白符删除
        return x.strip()

class TieBa:

    def __init__(self, baseURL, seeLZ, floorTag):
        self.baseURL = baseURL
        self.seeLZ   = '?see_lz=' + str(seeLZ)
        self.tool = ReplaceLabel()
        # 文件写入对象
        self.file = None
        # 楼层标号
        self.floor = 1
        # 默认标题, 如果没有成功获取到标题
        self.defaultTitle = '百度贴吧'
        # 是否写入楼层分割线
        self.floorTag = floorTag

    # 获取页面内容
    def getPage(self, pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            req = urlq.Request(url)
            with urlq.urlopen(req) as response:
                # print(response.read().decode('utf-8'))
                return response.read().decode('utf-8')
        except urlq.URLError as e:
            if hasattr(e, 'reason'):
                print('Connect tieba.baidu.com error: %s' % e.reason)
            return None

    # 获取帖子标题
    def getTitle(self, page):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        if result:
            # print(result.group(1).strip())
            return result.group(1).strip()
        else:
            return None

    # 抓取回帖页数
    def getPageNum(self, page):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            # print(result.group(1).strip())
            return result.group(1).strip()
        else:
            return None

    # 抓取正文内容
    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        # floor = 1
        contents = []
        for item in items:
            # print(floor, '楼----------------------------------------------'+
            #       '------------------------------------------------------\n')
            # print(self.tool.replaceLabel(item))
            # floor += 1
            content = '\n' + self.tool.replaceLabel(item) + '\n'
            contents.append(content)
        return contents

    # File
    def setFileTitle(self, title):
        if title:
            self.file = open(title + '.txt', 'w+')
        else:
            self.file = open(self.defaultTitle+'.txt', 'w+')

    def writeData(self, contents):
        # 把每个楼层的内容写到文件中
        for item in contents:
            if self.floorTag == '1':
                # + 分隔符
                floorLine = '\n' + str(self.floor) + \
                            '楼-------------------------------------------------\n'
                self.file.write(floorLine)
            self.file.write(str(item))
            self.floor += 1

    #################################
    def start(self):
        # 获取第一个页面
        indexPage = self.getPage(1)
        # 从第一个页面获取页数
        pageNum = self.getPageNum(indexPage)
        # 从第一个页面获取标题
        title = self.getTitle(indexPage)
        # 打开文件
        self.setFileTitle(title)

        if pageNum == None:
            print('URL is invalid !')
            return
        try:
            print ('The page number: %s' % str(pageNum))
            for i in range(1, int(pageNum) + 1):
                print('* Writing page', str(i), 'Data')
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        except IOError as e:
            print('Wrote error: ', e.message)
        finally:
            self.file.close()
            print('Wrote success !')




if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/'
    url_id = input('http://tieba.baidu.com/p/')
    baseUrl = url + str(url_id)
    seeLz = input('只看楼主? 1是, 0否\n')
    floorTag = input('记录楼数? 1是, 0否\n')
    page = TieBa(baseUrl, seeLz, floorTag)
    print(baseUrl)
    page.start()
