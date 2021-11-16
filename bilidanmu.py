# ------------------------------------------------
# Author: McShin team
# © 2021-2021 McShin team. All rights reserved.
# ------------------------------------------------
# 请求头
import requests
import time
import re
import os
import sys
import random
stoptime = "1000"  # 按下的时间
stoptime2 = "1500"  # 按下的时间
stoptime3 = "2000"  # 按下的时间
stoptime4 = "2500"  # 按下的时间
stoptime5 = "3000"  # 按下的时间


def main():
    while True:
        time.sleep(0.1)
        getdanmu()  # 调用请求函数
        hasfile()  # 动态检测文件
        randomnum = random.randint(31, 37)
        namecolor = str(randomnum) + "m"
        response = requests.post(url=url, headers=headers, data=data)
        dic_data = response.json()
        # print(dic_data)
        if not dic_data['data']:
            print("无法获取直播间数据，即将切断程序后续进程")
            sys.exit(0)  # 直接切断
        connettime = [item['timeline'] for item in dic_data['data']['room']]
        connettime = connettime[-1]
        f = open("time.txt")
        lines = f.read()
        if (lines != connettime):
            with open("time.txt", 'w') as file_object:
                file_object.write(connettime)
            content = [item['text']
                       for item in dic_data['data']['room']]  # 解析获取的弹幕内容
            content = content[-1]  # 只获取弹幕的最后一个内容

            # 获取发送者的名字
            username = [item['nickname'] for item in dic_data['data']['room']]
            content = content.lower()  # 将弹幕中所有大写字母改成小写
            up = re.search("视角上|cu", content)  # 判断是否为相关字符
            down = re.search("视角下|cd", content)  # 判断是否为相关字符
            left = re.search("视角左|cl", content)  # 判断是否为相关字符
            right = re.search("视角右|cr", content)  # 判断是否为相关字符
            hit = re.search("攻击", content)  # 判断是否为相关字符
            hit2 = re.search("攻击2", content)  # 判断是否为相关字符
            hit3 = re.search("攻击3", content)  # 判断是否为相关字符
            bash = re.search("重击|k", content)  # 判断是否为相关字符
            p1 = re.search("角色1|p1", content)  # 判断是否为相关字符
            p2 = re.search("角色2|p2", content)  # 判断是否为相关字符
            p3 = re.search("角色3|p3", content)  # 判断是否为相关字符
            p4 = re.search("角色4|p4", content)  # 判断是否为相关字符
            p1q = re.search("p1q", content)  # 判断是否为相关字符
            p2q = re.search("p2q", content)  # 判断是否为相关字符
            p3q = re.search("p3q", content)  # 判断是否为相关字符
            p4q = re.search("p4q", content)  # 判断是否为相关字符
            jump = re.search("跳|空格", content)  # 判断是否为相关字符
            bag = re.search("背包|b", content)  # 判断是否为相关字符
            esc = re.search("退出|返回|esc", content)  # 判断是否为相关字符
            fall = re.search("落下|跳下|x", content)  # 判断是否为相关字符
            tools = re.search("小物品|z", content)  # 判断是否为相关字符
            keeprun = re.search("冲刺|右键", content)  # 判断是否为相关字符
            # 以下是判断指令是否相同，不相同不执行
            if content == "a":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"A\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"A\", 1\n")
            elif content == "w":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"W\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"W\", 1\n")
            elif content == "www":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"W\", 1\n")
                    file_object.write("Delay "+stoptime3+"\n")
                    file_object.write("KeyUp \"W\", 1\n")
            elif content == "wwww":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"W\", 1\n")
                    file_object.write("Delay "+stoptime4+"\n")
                    file_object.write("KeyUp \"W\", 1\n")
            elif content == "wwwww":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"W\", 1\n")
                    file_object.write("Delay "+stoptime5+"\n")
                    file_object.write("KeyUp \"W\", 1\n")
            elif content == "s":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"S\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"S\", 1\n")
            elif content == "sss":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"S\", 1\n")
                    file_object.write("Delay "+stoptime3+"\n")
                    file_object.write("KeyUp \"S\", 1\n")
            elif content == "ssss":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"S\", 1\n")
                    file_object.write("Delay "+stoptime4+"\n")
                    file_object.write("KeyUp \"S\", 1\n")
            elif content == "sssss":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"S\", 1\n")
                    file_object.write("Delay "+stoptime5+"\n")
                    file_object.write("KeyUp \"S\", 1\n")
            elif content == "d":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"D\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"D\", 1\n")
            elif content == "wa" or content == "aw":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"A\", 1\n")
                    file_object.write("KeyDown \"w\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"A\", 1\n")
                    file_object.write("KeyUp \"w\", 1\n")
            elif content == "wd" or content == "dw":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"W\", 1\n")
                    file_object.write("KeyDown \"D\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"W\", 1\n")
                    file_object.write("KeyUp \"D\", 1\n")
            elif content == "sa" or content == "as":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"S\", 1\n")
                    file_object.write("KeyDown \"A\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"S\", 1\n")
                    file_object.write("KeyUp \"A\", 1\n")
            elif content == "sd" or content == "ds":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"S\", 1\n")
                    file_object.write("KeyDown \"D\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"S\", 1\n")
                    file_object.write("KeyUp \"D\", 1\n")
            elif content == "aa" or content == "aw":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"A\", 1\n")
                    file_object.write("KeyDown \"Shift\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"A\", 1\n")
                    file_object.write("KeyUp \"Shift\", 1\n")
            elif content == "ww":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"Shift\", 1\n")
                    file_object.write("KeyDown \"W\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"Shift\", 1\n")
                    file_object.write("KeyUp \"W\", 1\n")
            elif content == "ss":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"S\", 1\n")
                    file_object.write("KeyDown \"Shift\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"S\", 1\n")
                    file_object.write("KeyUp \"Shift\", 1\n")
            elif content == "dd":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"D\", 1\n")
                    file_object.write("KeyDown \"Shift\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"D\", 1\n")
                    file_object.write("KeyUp \"Shift\", 1\n")
            elif content == "wwaa" or content == "aaww":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"W\", 1\n")
                    file_object.write("KeyDown \"A\", 1\n")
                    file_object.write("KeyDown \"Shift\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"W\", 1\n")
                    file_object.write("KeyUp \"A\", 1\n")
                    file_object.write("KeyUp \"Shift\", 1\n")
            elif content == "wwdd" or content == "ddww":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"W\", 1\n")
                    file_object.write("KeyDown \"D\", 1\n")
                    file_object.write("KeyDown \"Shift\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"W\", 1\n")
                    file_object.write("KeyUp \"D\", 1\n")
                    file_object.write("KeyUp \"Shift\", 1\n")
            elif content == "ssaa" or content == "aass":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"S\", 1\n")
                    file_object.write("KeyDown \"A\", 1\n")
                    file_object.write("KeyDown \"Shift\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"S\", 1\n")
                    file_object.write("KeyUp \"A\", 1\n")
                    file_object.write("KeyUp \"Shift\", 1\n")
            elif content == "ssdd" or content == "ddss":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"S\", 1\n")
                    file_object.write("KeyDown \"D\", 1\n")
                    file_object.write("KeyDown \"Shift\", 1\n")
                    file_object.write("Delay "+stoptime+"\n")
                    file_object.write("KeyUp \"S\", 1\n")
                    file_object.write("KeyUp \"D\", 1\n")
                    file_object.write("KeyUp \"Shift\", 1\n")
            elif content == "ee":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyDown \"E\", 1\n")
                    file_object.write("Delay 1000\n")
                    file_object.write("KeyUp \"E\", 1\n")
                    file_object.write("Delay 200\n")
            elif content == "q":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"Q\", 1\n")
                    file_object.write("Delay 200\n")
            elif content == "e":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"E\", 1\n")
                    file_object.write("Delay 200\n")
            elif content == "f":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("MouseWheel - 1 \n")
                    file_object.write("Delay 20\n")
                    file_object.write("MouseWheel - 1 \n")
                    file_object.write("Delay 20\n")
                    file_object.write("KeyPress \"F\", 1\n")
                    file_object.write("Delay 80\n")
                    file_object.write("KeyPress \"F\", 1\n")
                    file_object.write("Delay 80\n")
                    file_object.write("KeyPress \"F\", 1\n")
                    file_object.write("MouseWheel 2\n")
                    file_object.write("Delay 200\n")
            # 以上是判断指令是否相同，不相同不执行
            # 以下是正则判断指令，只要字符串有以下一个就触发
            elif up:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                with open(filename, 'w') as file_object:
                    file_object.write("MoveR 0, -200\n")
            elif down:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                with open(filename, 'w') as file_object:
                    file_object.write("MoveR 0, 200\n")
            elif left:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                with open(filename, 'w') as file_object:
                    file_object.write("MoveR 200, 0\n")
            elif right:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                with open(filename, 'w') as file_object:
                    file_object.write("MoveR -200, 0\n")
            elif hit or content == "j":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                with open(filename, 'w') as file_object:
                    file_object.write("LeftClick 1\n")
                    file_object.write("Delay 200\n")
            elif hit2 or content == "jj":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                with open(filename, 'w') as file_object:
                    file_object.write("LeftClick 1\n")
                    file_object.write("Delay 150\n")
                    file_object.write("LeftClick 1\n")
                    file_object.write("Delay 200\n")
            elif hit3 or content == "jjj":
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                with open(filename, 'w') as file_object:
                    file_object.write("LeftClick 1\n")
                    file_object.write("Delay 150\n")
                    file_object.write("LeftClick 1\n")
                    file_object.write("Delay 150\n")
                    file_object.write("LeftClick 1\n")
                    file_object.write("Delay 200\n")
            elif bash:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                with open(filename, 'w') as file_object:
                    file_object.write("LeftDown 1\n")
                    file_object.write("Delay 1000\n")
                    file_object.write("LeftUp 1\n")
                    file_object.write("Delay 200\n")
            elif p1:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"1\", 1\n")
                    file_object.write("Delay 200\n")
            elif p2:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"2\", 1\n")
                    file_object.write("Delay 200\n")
            elif p3:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"3\", 1\n")
                    file_object.write("Delay 200\n")
            elif p4:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"4\", 1\n")
                    file_object.write("Delay 200\n")
            elif p1q:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"1\", 1\n")
                    file_object.write("KeyPress  \"Alt\", 1\n")
                    file_object.write("Delay 200\n")
            elif p2q:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"2\", 1\n")
                    file_object.write("KeyPress  \"Alt\", 1\n")
                    file_object.write("Delay 200\n")
            elif p3q:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"3\", 1\n")
                    file_object.write("KeyPress  \"Alt\", 1\n")
                    file_object.write("Delay 200\n")
            elif p4q:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"4\", 1\n")
                    file_object.write("KeyPress  \"Alt\", 1\n")
                    file_object.write("Delay 200\n")
            elif jump:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"Space\", 1\n")
                    file_object.write("Delay 200\n")
            elif bag:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"B\", 1\n")
            elif esc:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"Esc\", 1\n")
            elif fall:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"X\", 1\n")
            elif tools:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                # 开始写入文件
                with open(filename, 'w') as file_object:
                    file_object.write("KeyPress  \"Z\", 1\n")
                    file_object.write("Delay 200\n")
            elif keeprun:
                print("\33["+namecolor+username[-1]+"\033[0m：\""+content +
                      "\"（收到命令"+content+"）\033[32m 成功！\033[0m")
                with open(filename, 'w') as file_object:
                    file_object.write("RightDown 1\n")
                    file_object.write("Delay 1000\n")
                    file_object.write("RightDown 1\n")
                    file_object.write("Delay 200\n")
            # 以上是正则判断指令，只要字符串有以下一个就触发
            else:
                print("\33["+namecolor+username[-1]+"\33[0m：\"" +
                      content+"\"")
                # open(filename, 'w').close()
        else:
            0
            # open(filename, 'w').close()


def hasfile():
    global filename
    if(os.path.exists("./A.txt")):
        if(os.path.exists("./B.txt")):
            if(os.path.exists("./C.txt")):
                if(os.path.exists("./D.txt")):
                    if(os.path.exists("./E.txt")):
                        if(os.path.exists("./F.txt")):
                            if(os.path.exists("./G.txt")):
                                filename = "./H.txt"  # 脚本路径，建议使用相对路径
                            else:
                                filename = "./G.txt"  # 脚本路径，建议使用相对路径
                        else:
                            filename = "./F.txt"  # 脚本路径，建议使用相对路径
                    else:
                        filename = "./E.txt"  # 脚本路径，建议使用相对路径
                else:
                    filename = "./D.txt"  # 脚本路径，建议使用相对路径
            else:
                filename = "./C.txt"  # 脚本路径，建议使用相对路径
        else:
            filename = "./B.txt"  # 脚本路径，建议使用相对路径
    else:
        filename = "./A.txt"  # 脚本路径，建议使用相对路径


def getdanmu():
    global headers, data, url
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://live.bilibili.com',
        'Referer': 'https://live.bilibili.com/483983?spm_id_from=333.334.b_62696c695f6c697665.5',   # 请求直播间地址
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    }
    # 请求体
    data = {
        'roomid': '483983',
        'csrf_token': 'fa56950667934cf5a3479ca94abc1f9a',
        'csrf': 'fa56950667934cf5a3479ca94abc1f9a',
        'visit_id': '',
    }
    url = 'https://api.live.bilibili.com/ajax/msg'
    # 实时请求数据
    response = requests.post(url=url, headers=headers, data=data)
    with open("./test.txt", 'w') as file_object:
        file_object.write(str(response))
    if str(response) != '<Response [200]>':
        print("无法获取直播间数据，即将切断程序后续进程")
        sys.exit(0)
    return response


if __name__ == '__main__':
    hasfile()
    getdanmu()
    main()
