from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://www.amazon.co.jp/dp/480261179X')
driver.save_screenshot('amazon.png')
driver.quit()
# 結果:本のままdocker上で実行しようとするとchromedriverへのパスが通っておらず動かない
# これならPlaywriteでやればいいかな…という気になる
