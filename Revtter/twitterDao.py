#!-*- coding:utf-8 -*-"
'''
Created on 2012/01/03

@author: aqui_at_pocket
'''
import twitter
import datetime
from google.appengine.ext import db

'''
バッチ起動時に最後に取得したIDとキーを保持するEntity
'''
class TweetIdEntity(db.Model):
    '''
    ★DBに保存する情報
    ID
    Key
    バッチ実行時刻
    '''
    tweetKey = db.StringProperty(required=True)
    tweetId = db.IntegerProperty(required=True)
    batchTime = db.DateTimeProperty(required=True)

'''
TwitterEntity用のdaoクラス
'''
class TwitterIdEntityDao():
    def __init__(self,
                tweetId = None,
                tweetKey = None,
                batchTime = None):
        self.tweetId = tweetId
        self.tweetKey = tweetKey
        self.batchTime = batchTime
    
    '''
    保存用
    '''
    def InsertTweetId(self, tid, key):
        self.tweetId = tid
        self.tweetKey = key
        self.batchTime = datetime.datetime.now()

        t = TweetIdEntity(
                tweetId = self.tweetId,
                tweetKey = self.tweetKey,
                batchTime = self.batchTime)
        t.put()
        
    '''
    選択用
    '''
    def SelectTweetId(self, key):
        try:
            tweetIdList = db.GqlQuery("select * from TwitterIdEntity where tweetKey = :1 order by batchTime desc", key)
        except db.KindError:
            return None
        
        return tweetIdList[0]
    '''
    削除用
    '''
    def DeleteTweetId(self, idEntity):
        db.delete(idEntity)

'''
Twitterのタイムラインを保存する用のエンティティ
'''
class TweetEntity(db.Model):
    '''
    ★DBに保存する情報
    ・URL
    ・ページ名 (URLよりHTTPヘッダ情報を取得)
    ・Tweet本文
    ・時刻
    ・星(評価)
    ・ユーザ名
    '''
    tweetId = db.IntegerProperty(required=True)
    url = db.URLProperty()
    pageTitle = db.StringProperty()
    tweetText = db.StringProperty()
    tweetAt = db.DateTimeProperty()
    star = db.IntegerProperty()
    account = db.StringProperty()
    account_image = db.URLProperty()

'''
TwitterEntity用のdaoクラス
'''
class TwitterEntityDao():
    def __init__(self,
                search = None,
                url = None,
                title = None,
                star = 0):
        self.search = search
        self.url = url
        self.title = title
        self.star = star
    
    '''
    保存用
    '''
    def InsertTweet(self, search, url, title, star):
        self.search = search
        # ツイート時間をstringからdatetimeに変換
        ttime = datetime.datetime.strptime(self.search.created_at,
                                                '%a, %d %b %Y %H:%M:%S +0000')
        # ツイートの改行コードを削除
        ttext = self.search.text.replace('\r','')
        ttext = ttext.replace('\n','')

        t = TweetEntity(
                tweetId = self.search.id,
                url = self.url,
                pageTitle = self.title,
                tweetText = ttext,
                tweetAt = ttime,
                star = self.star,
                account = self.search.user.screen_name,
                account_image = self.search.user.profile_image_url)
        t.put()

    '''
    選択用
    '''
    def SelectTweet(self, tweetId):
        try:
            tweet = db.GqlQuery("select * from TweetEntity where tweetId = :1", tweetId)
        except db.KindError:
            return None
        return tweet[0]

    '''
    古いTweet検索用
    '''
    def SelectOldTweets(self, storageTerm):
        d = datetime.datetime.today() - datetime.timedelta(days=storageTerm)
        try:
            oldTweets = db.GqlQuery("select __key__ from TweetEntity where tweetAt < :1", d)
        except db.KindError:
            return None
        return oldTweets

    '''
    削除用
    '''
    def DeleteTweet(self, tEntity):
        db.delete(tEntity)
        