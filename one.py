import urllib2
import threading
import time
import urllib
import re

def select_class(classname):
    global cookie
    url = 'url'
    headers = {
        'Host' : 'ip',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding' : 'gzip, deflate',
        'DNT' : '1',
        'Referer' : 'url',
        'Cookie' : cookie + classname
        }
    url_request = urllib2.Request(url,headers = headers)
    url_open = urllib2.urlopen(url_request)
    html = url_open.geturl()
#    print url_open.read().decode('UTF-8').encode('GBK')
    if html == 'url':
        print 'please renew your cookie'
    if html != 'url':
        try :
            getclassname =  urllib.unquote(classname)
            print '                ' + getclassname.decode('UTF-8').encode('GBK')
        except :
            print ''
def multi_threading_start(classname):
    thread = []
    thread.append(threading.Thread(target=select_class,args=(classname,)))
    for t in thread :
        t.setDaemon(True)
        t.start()
def func_main(type_class_name):
    num = 0
    get_num = 0
    while(1):
        num = num + 1
        get_num = get_num + 1
        print 'NO.' + str(num) + ' times for select class'
        try:
            line = open(type_class_name).readlines()
            for read_line in line:
                multi_threading_start(read_line.strip())
        except:
            print '                process get error'
        time.sleep(3)
        if get_num == 60 :
            get_num = 0
            time.sleep(60)

def cookie_deal(user_cookie):
    cookie_result = ''
    re_for_cookie = r'.*XZKC='
    get_cookie_result = re.findall(re_for_cookie,user_cookie)
    if get_cookie_result == []:
        get_user_number = raw_input('please input your number of school: ')
        user_cookie = user_cookie +';' + get_user_number + '_XZKC=XZKC='
        return user_cookie
    for every_result in get_cookie_result:
        cookie_result = cookie_result + every_result
    return cookie_result


def start_print():
    print     '               ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    '
    print     '              @                                                                        @   '
    print     '              @                                                                        @   '
    print     '              @          IIIIIIIII   D  D         O O O   B B B B  Y         Y         @   '
    print     '              @              I       D     D    O       O B      B  Y       Y          @   '
    print     '              @              I       D       D  O       O B      B   Y     Y           @   '
    print     '              @              I       D       D  O       O B      B    Y   Y            @   '
    print     '              @              I       D       D  O       O B B B B       Y              @   '
    print     '              @              I       D       D  O       O B      B      Y              @   '
    print     '              @              I       D      D   O       O B      B      Y              @   '
    print     '              @              I       D     D    O       O B      B      Y              @   '
    print     '              @          IIIIIIIIII  D  D         O O O   B B B B       Y              @   '
    print     '              @                                                                        @   '
    print     '              @                                                                        @   '
    print     '               ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    '
    print     '               @@version:3.0                                                              '
    print     '               POWER BY IDOBY                                                              '
    print     '               Contact:(QQ)1318385771                                                     '
    print     '               doby@2017.2.27                                                            '
    print     '               please read the document at first when you want to know how to use this process'

def main_inter():
    select_class_name = raw_input('''which type of class do you want to select,
                                    key the word \'a\' for the art,
                                    key the word \'e\' for economy,
                                    key the word \'h\' for humanity,
                                    key the word \'n\' for nature\n
                                    ''')
    if select_class_name == 'a' :
        type_class_name = 'art.txt'
        func_main(type_class_name)
    if select_class_name == 'e' :
        type_class_name = 'economy.txt'
        func_main(type_class_name)
    if select_class_name == 'h' :
        type_class_name = 'humanity.txt'
        func_main(type_class_name)
    if select_class_name == 'n' :
        type_class_name = 'nature.txt'
        func_main(type_class_name)

if __name__ == '__main__':
    start_print()
    user_cookie = raw_input('               please input your cookie:')
    cookie = cookie_deal(user_cookie)
    main_inter()
