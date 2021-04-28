import json

import requests


def str_middle(q: str, h: str, text: str) -> str:  # 取文本中间
    """

    :rtype: str
    """
    return text.split(q)[-1].split(h)[0]


class LanZou:
    def __init__(self, url, p=""):
        # 初始化
        self.user_url = url
        self.passw = p
        self.main_url = "https://www.lanzous.com/"
        self.zhilian_url = "https://www.lanzous.com/ajaxm.php?"
        self.password_url = "https://www.lanzous.com/filemoreajax.php?"
        self.h = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'referer': 'https://www.lanzous.com/'

        }

    def quzhilian(self):
        # 总接口
        str1 = "输入密码"
        str3 = "文件受密码保护，请输入密码继续下载"
        q = requests.get(self.user_url, headers=self.h)
        str2 = q.content.decode()
        zt = str2.find(str1)
        if zt == -1:
            if str2.find("显示更多文件") != -1:  # 多文件无密码
                return self.yes_password(str2)
            else:
                return self.no_password(str2)
        else:
            if str2.find(str3) != -1:
                # print("进入多文件分享")
                return self.yes_password(str2)
            else:
                print("进入单文件分享，单文件分享暂不支持")
                self.h['referer'] = self.user_url
                data = str_middle("data : '", "'", str2) + self.passw
                action = str_middle("action=", "&", data)
                sign = str_middle("sign=", "&", data)
                data1 = {'action': action, 'sign': sign, 'p': self.passw}
                q = requests.post(self.zhilian_url, headers=self.h, data=data1)
                file_list = {'info': "sucess", 't': q.json()['dom'] + "/file/" + str(q.json()['url']),
                             'name_all': q.json()['inf'], 'size': 'NULL'}
                if q.json()['inf'] == "密码不正确":
                    file_list['name_all'] = ""
                    file_list['t'] = ""
                    file_list['info'] = 0
                return file_list

    def no_password(self, text):
        # 无密码获取直链
        # print("进入无密码")
        text1 = text
        wz1 = text1.find("src=")  # 第一个src不正确
        wz1 = text1.find("src=", wz1 + 5) + 5  # 此src正确，+5去掉src
        wz2 = text1.find('"', wz1)  # 找到尾位置
        down_url_list = self.main_url + text1[wz1:wz2]  # 获取下载页面，此为链接
        q = requests.get(down_url_list, headers=self.h)
        text1 = q.content.decode()  # 获取下载页面，此为源码
        wz1 = text1.find("data : {") + 7
        wz2 = text1.find("}") + 1
        date = str(text1[wz1:wz2])
        wz1 = date.find("'signs':") + 8
        ls1 = date[:wz1]  # 获取前边常量
        wz1 = text1.find("ajaxdata = '") + 12  # 获取ajaxdata变量
        wz2 = text1.find("'", wz1)  # 获取ajaxdata变量
        ls = text1[wz1:wz2]  # 获取ajaxdata变量
        ls1 = ls1 + "'" + ls + "'"  # 第一个变量值
        wz1 = text1.find("pdownload = '") + 13  # 获取pdownload变量
        wz2 = text1.find("'", wz1)  # 获取pdownload变量
        ls = text1[wz1:wz2]  # 获取pdownload变量
        wz1 = date.find("'sign':") + 7
        wz2 = date.find(",", wz1)
        wz3 = wz2
        ls = date[wz1:wz2]  # 第二个变量值，有点恶心，有两个变量循环变,postdown，pdownload
        ls = "{} = '".format(ls)
        if len(ls) == 12:  # 为postdown
            wz1 = text1.find(ls) + 12
        else:  # 为pdwonload
            wz1 = text1.find(ls) + 13
        wz2 = text1.find("'", wz1)
        sign_bl = text1[wz1:wz2]
        ls1 = ls1 + ",'sign':'" + sign_bl + "'" + date[wz3:]  # 最终post字典
        # print(text1)
        # print(date)
        # print(ls1)
        # print(ls)
        title = str_middle("<title>", " - 蓝奏云</title>", text)
        size = str_middle("文件大小：</span>", "<br>", text)
        date = eval(ls1)  # 转换为字典
        file_date = {
            'info': '',
            't': '',
            'name_all': '',
            'size': ''
        }
        down_list = requests.post(self.zhilian_url, headers=self.h, data=date)
        if down_list.json()['inf'] == "已超时，请刷新" or down_list.content.decode() == "":
            file_date['info'] = '0'
            return file_date
        else:
            dom = down_list.json()['dom']
            dom_url = str(down_list.json()['url'])
            down = dom + "/file/" + dom_url
            file_date['info'] = "sucess"
            file_date['t'] = down
            file_date['name_all'] = title
            file_date['size'] = size
            return file_date

    def yes_password(self, text):
        #  多文件分享
        url_ym = text
        file_lx = str_middle("'lx':", ",", url_ym)
        file_fid = str_middle("'fid':", ",", url_ym)
        file_uid = str_middle("'uid':'", "'", url_ym)
        file_rep = str_middle("'rep':'", "'", url_ym)
        file_up = str_middle("'up':", ",", url_ym)
        file_ls = str_middle("'ls':", ",", url_ym)
        file_password = self.passw
        file_pgbl = str_middle("'pg':", ",", url_ym)
        file_pgs = str_middle("{} =".format(file_pgbl), ";", url_ym)
        file_tbl = str_middle("'t':", ",", url_ym)
        file_t = str_middle("var {} = '".format(file_tbl), "'", url_ym)
        file_kbl = str_middle("'k':", ",", url_ym)
        file_k = str_middle("var {} = '".format(file_kbl), "'", url_ym)
        zd = {
            'lx': file_lx,
            'fid': file_fid,
            'uid': file_uid,
            'pg': file_pgs,
            'rep': file_rep,
            't': file_t,
            'k': file_k,
            'up': file_up,
            'ls': file_lx,
            'pwd': file_password
        }
        url_ym1 = requests.post(self.password_url, headers=self.h, data=zd)
        q = json.loads(url_ym1.content.decode())
        if q['info'] == "密码不正确":
            file_list = {
                'info': 0
            }
            return file_list
        arr_list = len(q['text'])
        for i in range(0, arr_list):
            url = q['text'][i]['id']
            q['text'][i]['id'] = self.main_url + url
            nopassym = requests.get(q['text'][i]['id'], headers=self.h)
            q['text'][i]['t'] = self.no_password(nopassym.content.decode())['t']
        return q


if __name__ == "__main__":
    # text = input("请输入需要解析的蓝奏链接：")
    #text = "https://ximami.lanzous.com/ixjiFlaiogj"  #  此为无密码单文件
    #text = "https://www.lanzous.com/b00t3vkmb"  #  此为多文件密码 密码为：hgkw
    #text = "https://www.lanzous.com/i2imtwd"  #  此为单文件密码：66wa
    text = "https://wwx.lanzoui.com/b015qczoj"  #  多文件无密码
    zhilian = LanZou(text)  #  参数：链接, 密码。密码为可省参数，可不填,如要填：LanZou(链接, 密码)
    q = zhilian.quzhilian()
    print(q)
