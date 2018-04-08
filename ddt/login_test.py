#coding: utf-8
import ddt
import unittest
from case import ExcelUtil
filepath = "D:\\reg.xlsx"
sheetName = "Sheet1"
data = ExcelUtil(filepath, sheetName)


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.11.199:8089")
        self.driver.maximize_window()
        self.driver.find_element_by_id("toReg").click()

    def login(self,email,account,psw,phone,company):

        js = 'var q=document.getElementById("scroll").scrollTop = 100000;'
        # js = "var q=document.documentElement.scrollTop=100000"
        # 操作弹出框滚动条
        self.driver.execute_script(js)
        time.sleep(3)
        self.driver.find_element_by_id("email").clear()
        self.driver.find_element_by_id("email").send_keys(email)

        self.driver.find_element_by_id("account").clear()
        self.driver.find_element_by_id("account").send_keys(account)

        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(psw)

        self.driver.find_element_by_id("phone").clear()
        self.driver.find_element_by_id("phone").send_keys(phone)

        self.driver.find_element_by_id("company").clear()
        self.driver.find_element_by_id("company").send_keys(company)
        time.sleep(5)

        self.driver.find_element_by_xpath("//*[@id='register']/form/div[8]/button").click()

        time.sleep(5)

    @ddt.data
    def ll(self,data):
        u'''登陆案列'''
        print "当前测试数据%s"%data
        self.login(data["email"],data["account"],data["psw"],data["phone"],data["company"])
        # 判断结果
        result=self.is_login_sucess()
        self.assertTrue(result)


    def tearDown(self):
        self.driver.quit()


if __name__ =="__main__":
    unittest.main()