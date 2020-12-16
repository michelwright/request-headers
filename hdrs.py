from bs4 import BeautifulSoup
import re
import requests

class Headers:
    def __init__(self):
        self.url = "https://www.whatismybrowser.com/detect/"
        self.headers = ""
        self.chrome_win10 = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        self.mobile_ios = {'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        self.ie_win7 = {'user-agent':'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
        self.safari_mac = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

    def info(self):
        print('------------')
        print('chrome_win10')
        print('mobile_ios')
        print('ie_win7')
        print('safari_mac')
        print('------------')

    def test(self, headers):
        r = requests.get(self.url+'what-http-headers-is-my-browser-sending', headers=headers)   
        self.soup = BeautifulSoup(r.text, 'html.parser')   
        browser_info = self.soup.body.find_all(string=re.compile('ACCEPT-ENCODING'))[0].parent.parent.parent
        for th in browser_info.find_all('th'):
            print('-------------------------')
            print('')
            print(th.get_text()+' : ' + th.next_sibling.next_sibling.get_text())
            print('')


