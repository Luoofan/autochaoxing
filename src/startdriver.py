from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from publicfunc import COLOR
from os import popen as os_popen

class StartDriver(object):

    def __enter__(self):
        self.driver = StartDriver.startchrome()
        driver_pid = self.driver.service.process.pid
        self.chrome_pid = driver_pid
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os_popen('taskkill /F /T /PID '+str(self.chrome_pid))
        '''
        try:
            self.driver.quit()
        except KeyboardInterrupt:
            self.driver.quit()      
        '''

        if exc_type in [SystemExit, KeyboardInterrupt]:
            print(COLOR.NOTE, "QUIT!", COLOR.END)
        elif exc_type != None:
            print('程序遇到错误,请分析处理:')
            print('TYPE:'+str(exc_type))
            print('VAL: '+str(exc_val))
            print('TB:  '+str(exc_tb))
        return True

    # 启动chrome
    # debugarg:拓展启动选项
    @staticmethod
    def startchrome(debugarg=''):
        # 初始化
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('log-level=3')
        chrome_options.add_argument('–incognito')  # 启动无痕/隐私模式
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument('--disable-background-networking')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--single-process')
        chrome_options.add_argument('--disable-plugins')
        if debugarg != '':
            chrome_options.add_argument(debugarg)
        ##  INFO = 0,
        ##  WARNING = 1,
        ##  LOG_ERROR = 2,
        ##  LOG_FATAL = 3
        ##  default is 0
        return webdriver.Chrome(options=chrome_options, executable_path=r"./chromedriver")
        # 在哪个目录执行就要在该目录下有chromedriver
