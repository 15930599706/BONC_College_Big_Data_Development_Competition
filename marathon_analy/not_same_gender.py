import csv
import matplotlib.pyplot as plt
def t2s(t):  # 时分秒转换成秒
    h, m, s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)
def s2m(seconds):  # 秒转换成分钟
    return int(seconds) / 60
def s2t(seconds):  # 秒转换成时分
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return str(round(h)) + ":" + str(round(m)) + ":" + str(round(s))
def avg(tmp_list,tep_num):#求平均值函数
    tem_all = 0
    for tmp_a in tmp_list:
        tem_all = tem_all + t2s(tmp_a)
    tem_avg = tem_all/tep_num
    return tem_avg
filename='marathon-data.csv'
with open(filename,'r')as file:
    reader=csv.reader(file)
    header_row=next(reader)
    ages=[]
    genders=[]
    split=[]
    final=[]
    final_man = []
    final_woman = []
    split_man = []
    split_woman = []
    WO = 0
    MA = 0
    for row in reader:
        ages.append(int(row[0]))
        genders.append(row[1])
        split.append(row[2])
        final.append(row[3])
        if (row[1] == 'M'):
            MA = MA + 1
            split_man.append(row[2])
            final_man.append(row[3])
        else:
            WO = WO + 1
            split_woman.append(row[2])
            final_woman.append(row[3])

    #绘制不同性别选手的全程平均时间差异图# #
    #计算男性用时的平均值
    finalManAll = 0
    for mymanfinal in final_man:
        finalManAll = finalManAll + t2s(mymanfinal)
    manseconds = finalManAll/MA

    splitManAll = 0
    for mymansplit in split_man:
        splitManAll = splitManAll + t2s(mymansplit)
    manseconds_split = splitManAll / MA
    # print(s2t(manseconds))

    # 计算女性用时的平均值
    finalWomanAll = 0
    for mywomanfinal in final_woman:
        finalWomanAll = finalWomanAll + t2s(mywomanfinal)
    womanseconds = finalWomanAll / WO

    splitWomanAll = 0
    for mywomansplit in split_woman:
        splitWomanAll = splitWomanAll + t2s(mywomansplit)
    womanseconds_split = splitWomanAll / WO
    # print(s2t(womanseconds))

    #使用matplotlab绘制不同性别全程成绩差异的饼状图
    labels = '男性平均完成时间：'+s2t(manseconds), '女性平均完成时间：'+s2t(womanseconds)
    sizes = [manseconds, womanseconds]
    explode = (0, 0.1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('不同性别选手全程的平均时间差异', fontsize=20)
    plt.show()
    #绘制不同性别选手的全程平均时间差异图# #

 #使用matplotlab绘制不同性别半程成绩差异的饼状图
    labels = '男性平均完成时间：'+s2t(manseconds_split), '女性半均完成时间：'+s2t(womanseconds_split)
    sizes = [manseconds_split, womanseconds_split]
    explode = (0, 0.1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    fig2, ax2 = plt.subplots()
    ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax2.axis('equal')
    plt.title('不同性别选手半程的平均时间差异', fontsize=20)
    plt.show()
    #绘制不同性别选手的半程平均时间差异图# #