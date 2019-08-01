from appium import webdriver
from threading import Thread
from time import sleep
import time
import unittest
import gspread
import os.path
from oauth2client.service_account import ServiceAccountCredentials


#object
class TestStringMethods(object):
    global setting
    def setting(self, platformVersion, udid, port):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = platformVersion
        desired_caps['deviceName'] = udid
        desired_caps['udid'] = udid
        desired_caps['app'] = "/Users/jojin-ug/Downloads/blogtest-release.apk"
        desired_caps['appPackage'] = 'product.dp.io.ab180blog'
        desired_caps['appActivity'] = 'product.dp.io.ab180blog.MainActivity'

        self.driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' % port, desired_caps)
        logcat = 'adb -s {0} logcat -s -d "AirBridge" > {1}.txt'.format(udid, platformVersion)

        # scope = ['https://spreadsheets.google.com/feeds',
        #          'https://www.googleapis.com/auth/drive']
        #
        # credentials = ServiceAccountCredentials.from_json_keyfile_name(
        #     '/Users/jojin-ug/Downloads/Android-89aedfc5e2fa.json', scope)
        
        # global gc
        # gc = gspread.authorize(credentials)
        #
        # global copy_of_spreadsheet
        # copy_of_spreadsheet = gc.copy(
        #     file_id='14sme1nYlI0SlcoCBFavMd7L_wwvW_DaRlxb6Ome0Pcw',
        #     title='Normal auto QA'
        # )
        #
        # sleep(3)
        #
        # copy_of_spreadsheet.share('jjw@ab180.co', perm_type='user', role='writer')
        # table = copy_of_spreadsheet.get_worksheet(0)
        # sleep(5)
        # table.update_acell('E4', "F4", "G4", "9161 or 9163")
        # table.update_acell('E2', "S10")

        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            '/Users/jojin-ug/Downloads/Android-89aedfc5e2fa.json', scope)
        gc = gspread.authorize(credentials)
        global list
        list = gc.open("Normal auto QA").sheet1
        sleep(1)

        cell_list = list.range('E5:G5')
        for cell in cell_list:
            cell.value = '9161 or 9163'
        list.update_cells(cell_list)

        driver = self.driver

        time.sleep(3)
        for i in range(0, 11):
            driver.find_element_by_class_name(
                "android.widget.ImageView").click()

        driver.find_element_by_class_name('android.widget.ImageButton').click()

        driver.find_elements_by_class_name('android.support.v7.widget.at')[4].click()

        driver.find_element_by_id("product.dp.io.ab180blog:id/event_button_signup").click()
        cell_list = list.range('E6:G6')
        for cell in cell_list:
            cell.value = '9360'
        list.update_cells(cell_list)
        # table.update_acell('E6', "9360")

        driver.find_element_by_id("product.dp.io.ab180blog:id/event_button_purchase").click()
        cell_list = list.range('E7:G7')
        for cell in cell_list:
            cell.value = '9360'
        list.update_cells(cell_list)
        # table.update_acell('E7', "9360")

        driver.background_app(5)

        # table.update_acell('E8', "9269")
        # table.update_acell('E9', "9165")

        driver.background_app(15)
        # table.update_acell('E10', "9269")
        # table.update_acell('E11', "9166")

        a = 0
        for a in range(0, 5):
            driver.back();
            # table.update_acell('E12', "9260")

        sleep(2)

        ablog = "adb -s %s shell am start -n 'product.dp.io.ab180blog/product.dp.io.ab180blog.MainActivity'" % udid
        os.system(ablog)
        # table.update_acell('E13', "9167")

        sleep(10)

        for a in range(0, 4):
            driver.back();
            # table.update_acell('E14', "9260")

        sleep(15)
        os.system(ablog)

        sleep(3)

        driver.background_app(-1)  # 0+ 은 백그라운드로 갓다가 자동 포그라운드, -1은 백그라운드만
        # table.update_acell('E18', "9269")

        driver.find_element_by_accessibility_id("Chrome").click()
        sleep(1)
        driver.find_element_by_id("com.android.chrome:id/url_bar").send_keys("https://jojinwook.tistory.com",
                                                                             "\n")
        driver.implicitly_wait(15)

        # link1 = self.driver.find_elements_by_class_name("android.view.View")[19]
        # link1.click()
        self.driver.find_element_by_id("mArticle").click()
        sleep(2)
        self.driver.find_elements_by_class_name("android.view.View")[22].click()

        # table.update_acell('E19', "9162")
        driver.background_app(-1)  # 0+ 은 백그라운드로 갓다가 자동 포그라운드, -1은 백그라운드만
        # table.update_acell('E16', "9269")

        self.driver.find_element_by_accessibility_id("Chrome").click()

        self.driver.find_elements_by_class_name("android.view.View")[22].click()
        # table.update_acell('E17', "9168")
        # for a in range(0, 3):
        #     driver.back();
        driver.back();
        # table.update_acell('E20', "9260")

        self.driver.find_elements_by_class_name("android.view.View")[22].click()

        # table.update_acell('E21', "9168")
        sleep(7)
        driver.back();
        # table.update_acell('E22', "9260")
        sleep(15)
        self.driver.find_elements_by_class_name("android.view.View")[22].click()
        # table.update_acell('E23', "9162")
        # table.update_acell('E2', "S10")
        sleep(8)

        os.system(logcat)

        self.driver.remove_app("product.dp.io.ab180blog");

    def set_excel(self):
        now = date.today()
        test_date = str(now)

        url = str(copy_of_spreadsheet)
        last = url.split(':')

        list = gc.open_by_key("1NLuIwENMprN8oo8W2uBL8UUs45gH3lVGhWAiaxErU4Q")
        log = list.get_worksheet(0)

        log.update_acell('A5', test_date)
        log.update_acell('B5', "https://docs.google.com/spreadsheets/d/{}/edit#gid=0".format(last[1].replace(">", "")))

        self.driver.remove_app("product.dp.io.ab180blog");

    def tearDown(self):
        self.driver.quit()


# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
#     unittest.TextTestRunner(verbosity=2).run(suite)

class MyThread(Thread):
    def __init__(self, platformVersion, deviceName, port):
        super(MyThread, self).__init__()
        self.platformVersion = platformVersion
        self.deviceName = deviceName
        self.port = port

    def run(self):
        setting(self, self.platformVersion, self.deviceName, self.port)


# t1 = MyThread('9', 'R39M304WPXN', '4723' )
# t2 = MyThread('7.0', '03157df3c08eea3b', '5000')
# t3 = MyThread('8.0.0', 'LGF800Ka5526cb2', '4000')
t3 = MyThread('8.0', 'ce091609a85ea23104', '4000')

# t1.start()
# t2.start()
t3.start()
