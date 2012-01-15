#!-*- coding:utf-8 -*-"
'''
Created on 2011/12/29

@author: aqui_at_pocket
'''
import twitter
import httplib
import twitterDao

class twi(object):
    '''
    APIを取得する。
    '''
    def getApi(self):
#        ckey = '4T9j3uYDQKYvjYkUxa1bPw'
#        csec = 'fVsdPZTkmwPiGgqvdu5uajWTff1mABrlg6Jj8fCFdg'
#        akey = '389801060-czBx2H2XZ5PULb2PV6tNzRTbCrvQG8CKJ2wJr51k'
#        asec = 'QpMgnUubXNFFsLpMmCe2gx4CA0UMv5G5EQDFh29RTA'
#        api = twitter.Api(
#                          consumer_key=ckey,
#                          consumer_secret=csec,
#                          access_token_key=akey,
#                          access_token_secret=asec)
        api = twitter.Api(cache=None)
        return api
    '''
    前回取得時のIDを取得する。
    '''
    def getPrevId(self, key):
        dao = twitterDao.TwitterIdEntityDao()
        t = dao.SelectTweetId(key)
        if t is not None:
            return t.tweetId
        
        return None
    '''
    取得したIDを登録する。
    '''
    def setId(self, twitterid, key):
        dao = twitterDao.TwitterIdEntityDao()
        dao.InsertTweetId(twitterid, key)
    
    '''
    タイムラインを取得する。
    '''
    def getTimeLine(self, key):
        sid = self.getPrevId(key)
        print 'SinceId'
        print sid
        search = self.getApi().GetSearch(term=key,
                               per_page=10,
                               lang="ja",
                               since_id=sid)
        return search
    
    '''
    URLの取得と短縮URLの解読を行う
    '''
    def anaUrl(self):
        # http://t.co/2OFTLJi のレスポンスを取得する。
        conn = httplib.HTTPConnection("t.co")
        conn.request("GET", "/2OFTLJi")
        res = conn.getresponse()

        # レスポンスのヘッダーを全部ファイルに書き出す。
        print res.getheader("location")
        conn.close()
        
        return 'urlDebug'
    '''
    URLからそのページのタイトル情報を取得する
    '''
    def getTitle(self):
        return 'titleDebug'
    
    '''
    Tweetから☆の評価情報を取得する。
    '''
    def anaStar(self):
        return 5

'''
ここからバッチスタート
'''
key = 'revtter'
twitterapi = twi() #インスタンスを作成
search = twitterapi.getTimeLine(key) #タイムラインを取得
if len(search) != 0:
    twitterapi.setId(search[0].id, key) #IDを登録する。

for s in search:
    print s.user.screen_name
    print s.id
    #urlを取得する。
    url = twitterapi.anaUrl()

    #header情報を取得する。
    title = twitterapi.getTitle()
    
    #☆を評価する。
    star = twitterapi.anaStar()

    #データを登録する。
    tdao = twitterDao.TwitterEntityDao()
    tdao.InsertTweet(s, url, title, star)
