#调用库
import random
import linecache
#随机挑选单词
#依据有行数找单词数量
with open("word.txt", 'r',encoding="utf-8") as word:
    line_number = 0
    for line in word:
        line_number = line_number +1
#查看判定
print("欢迎回来，单词本内有" + str(line_number) + "个单词")
question = input("做点什么？学习点击1，查询教材点击2，了解项目情况点击3")
if question == "1":
    continue_ok = False
    while not continue_ok:
        a = (random.randint(1, line_number))
        theline = linecache.getline(r'word.txt', a)
        English, Chinese = theline.strip().split("=")
        print("好的，单词是"+Chinese)
        answer = input("这个单词的英文是？")
        if answer == English:
            print("cool做对力ヽ(´▽｀)/")
        else:
            print("被撅力(ノ`Д´)ノ正确答案是"+English)
        choice = input("是否要继续学习？(y/n): ")
        if choice.lower() != "y":
            continue_learning = True
            break
elif question == "2":
    print("正在为您寻找所能找到的教材")
    print("功能仍未开放，由于未找到教材中的单词")
else:
    print("而又着急上传，感谢您的支持，下次我们将带来更加重磅的更新与内容，如需更多消息请关注wp.janezh.cn或者www.janezh.cn谢谢")