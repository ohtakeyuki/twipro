#!/usr/bin/env python
# -*- coding:utf-8 -*-"

import twitterDao

# 保存期間(日)
storageTerm=180

dao = twitterDao.TwitterEntityDao()
q = dao.SelectOldTweets(storageTerm)
oldTweets = q.fetch(q.count())
dao.DeleteTweet(oldTweets)
