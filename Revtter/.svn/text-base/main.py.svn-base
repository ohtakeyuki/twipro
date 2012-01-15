#!/usr/bin/env python
# -*- coding: utf-8 -*-

#GAEのインポート
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

#日時取得用
import datetime

#メインページの設定
class MainPage(webapp.RequestHandler):
    def get(self):
        
        #動作確認用ダミー変数
        datetm = datetime.datetime.today()
        urlname = '築地 すしざんまい'
        url = 'http://www.kiyomura.co.jp/'
        count = '56812433'
        rev1 = '芽ねぎがおいしかった'
        rev2 = 'ハマチがおいしかった'
        rev3 = 'ホイル焼きがおいしかった'
        rev4 = '一ノ蔵がおいしかった'
        rev5 = '生ビールがおいしかった'
        
        #htmlに渡す変数の設定
        template_values = {
                #動作確認要ダミー変数
                'datetm': datetm,
                'urlname': urlname,  
                'url': url,
                'count': count,
                'rev1': rev1,
                'rev2': rev2,
                'rev3': rev3,
                'rev4': rev4,
                'rev5': rev5,
            }

        #テンプレートのパスを指定
        path = os.path.join(os.path.dirname(__file__), 'html/template_main.html')
        self.response.out.write(template.render(path, template_values))


#WEBアプリケーション呼び出し
application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

#メインメソッド
def main():
    run_wsgi_app(application)

#おまじない（起点）
if __name__ == "__main__":
    main()