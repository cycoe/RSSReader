#!/usr/bin/python
# -*- coding: utf-8 -*-

import feedparser
import os
import re

class RssFetcher():
    def getCon(self, rssSub):
        self.rssCon = feedparser.parse(rssSub)

    def outputer(self, num = 20):
        rssTitle = []
        rssSummary = []
        rssEntries = self.rssCon['entries']
        delPattern = re.compile("<a.*?>")
        for i in range(len(rssEntries)):
            rssTitle.append(rssEntries[i]['title'])
            reSummary = re.sub("<img.*?>", '', ''.join(rssEntries[i]['summary'].split('\n')))
            reSummary = re.sub("<a.*?>", '', reSummary)
            rssSummary.append(reSummary)
            if i >= num:
                break
        return rssTitle, rssSummary

class RssFetcher1():
    def getCon(self, rssSub):
        self.rssCon = feedparser.parse(rssSub)

    def outputer(self, num = 20):
        rssTitle = []
        rssSummary = []
        rssEntries = self.rssCon['entries']
        summary_pattern = re.compile("<p>(.*?)</p>", re.S)
        for i in range(len(rssEntries)):
            rssTitle.append(rssEntries[i]['title'])
            if not re.findall('<p>', rssEntries[i]['summary']) == []:
                reSummary = '{enter}'.join(summary_pattern.findall(rssEntries[i]['summary']))
            else: reSummary = rssEntries[i]['summary']
            rssSummary.append(reSummary)
            if i >= num:
                break
        return rssTitle, rssSummary

    def run(self):
        self.getCon()
        return self.outputer()
