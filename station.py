from selenium import webdriver
from selenium .webdriver.common.keys import Keys
import pandas
import time
#PhantomJSのWebDriverオブジェクトを作成する
driver = webdriver.PhantomJS()
#Yahoo乗り換え案内時刻表のトップ画面を開く
driver.get('https://transit.yahoo.co.jp/station/time')
#検索語を入力して送信する
#検索ボックス画面
input_element = driver.find_element_by_name('q')
input_element.send_keys('南林間駅')
input_element.send_keys(Keys.RETURN)
#時刻表路線案内一覧
url=driver.current_url
element=driver.find_elements_by_partial_link_text("方面")

#時刻表表示画面
for i in range(len(element)):
	url2=element[i].get_attribute("href")
	times_df = pandas.io.html.read_html(url2)#時刻表データ取得
	direction=element[i].text#方面のデータを取得
	print(direction)
	print(times_df[0])
	time.sleep(5)	
#times_df[0].to_csv('output.csv')#csv出力
