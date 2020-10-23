from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge Beta\Application\MicrosoftWebDriver.exe')
driver.get('https://newids.seu.edu.cn/authserver/login?service=http%3A%2F%2Fehall.seu.edu.cn%2Fqljfwapp2%2Fsys%2FlwReportEpidemicSeu%2Findex.do%3Ft_s%3D1594447890898%26amp_sec_version_%3D1%26gid_%3DSTZiVXZjRnhVSS9VNERWaFNNT1hXb2VNY3FHTHFVVHMwRC9jdTdhUlllcXVkZDNrKzNEV1ZxeHVwSEloRVQ4NHZFVzRDdHRTVlZ1dEIvczVvdzVpVGc9PQ%26EMAP_LANG%3Dzh%26THEME%3Dindigo%23%2FdailyReport')
driver.maximize_window()
driver.find_element_by_id('username').send_keys('******')  #（输入一卡通号）
driver.find_element_by_id('password').send_keys('******')  #（输入密码）
driver.find_element_by_xpath('//*[@class="auth_login_btn primary full_width"]').click()        
print('登录成功')
WebDriverWait(driver,30,0.2).until(lambda x:x.find_element_by_xpath('//*[@class="bh-btn bh-btn-primary"]'))
driver.find_element_by_xpath('//*[@class="bh-btn bh-btn-primary"]').click()
driver.find_element_by_name('DZ_JSDTCJTW').send_keys('36.7')
driver.find_element_by_id('save').click()
WebDriverWait(driver,30,0.2).until(lambda x:x.find_element_by_xpath('//*[@class="bh-dialog-btn bh-bg-primary bh-color-primary-5"]'))
driver.find_element_by_xpath('//*[@class="bh-dialog-btn bh-bg-primary bh-color-primary-5"]').click()
print('打卡完成')
driver.close()