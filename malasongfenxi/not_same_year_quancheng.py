import csv
import matplotlib.pyplot as plt
import numpy as np

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
    WO = 0
    MA = 0
    for row in reader:
        ages.append(int(row[0]))
        genders.append(row[1])
        split.append(row[2])
        final.append(row[3])
    # #绘制不同年龄选手的全程平均时间差异图# #
    #对数据中的重复年龄进行剔除，发现选手年龄集中在17-86岁，因此以十个年龄为一个跨度做柱状图#
    # tmp_list = []
    # for element in ages:
    #     if element not in tmp_list:
    #         tmp_list.append(element)
    # tmp_list.sort()
    # print(tmp_list)
    ageNum17_27 = 0
    ageNum27_37 = 0
    ageNum37_47 = 0
    ageNum47_57 = 0
    ageNum57_67 = 0
    ageNum67_77 = 0
    ageNum77_87 = 0
    final17_27 = []
    final27_37 = []
    final37_47 = []
    final47_57 = []
    final57_67 = []
    final67_77 = []
    final77_87 = []
    split17_27 = []
    split27_37 = []
    split37_47 = []
    split47_57 = []
    split57_67 = []
    split67_77 = []
    split77_87 = []
    #统计各年龄段对应的人数并将全程时间分类#
    for (nowAge,nowFinal) in zip(ages,final):
         if(nowAge < 27):
             ageNum17_27 = ageNum17_27 + 1
             final17_27.append(nowFinal)
         else:
             if (nowAge < 37):
                 ageNum27_37 = ageNum27_37 + 1
                 final27_37.append(nowFinal)
             else:
                 if (nowAge < 47):
                     ageNum37_47 = ageNum37_47 + 1
                     final37_47.append(nowFinal)
                 else:
                     if (nowAge < 57):
                         ageNum47_57 = ageNum47_57 + 1
                         final47_57.append(nowFinal)
                     else:
                         if (nowAge < 67):
                             ageNum57_67 = ageNum57_67 +1
                             final57_67.append(nowFinal)
                         else:
                             if (nowAge < 77):
                                 ageNum67_77 = ageNum67_77 + 1
                                 final67_77.append(nowFinal)
                             else:
                                 if (nowAge < 87):
                                     ageNum77_87 = ageNum77_87 + 1
                                     final77_87.append(nowFinal)

    for (nowAges,tem) in zip(ages,split):
         if(nowAges < 27):
             split17_27.append(tem)
         else:
             if (nowAges < 37):
                 split27_37.append(tem)
             else:
                 if (nowAges < 47):
                     split37_47.append(tem)
                 else:
                     if (nowAges < 57):
                         split47_57.append(tem)
                     else:
                         if (nowAges < 67):
                             split57_67.append(tem)
                         else:
                             if (nowAges < 77):
                                 split67_77.append(tem)
                             else:
                                 if (nowAges < 87):
                                     split77_87.append(tem)
    #全程#
    name_list = ['17-27岁', '27-37岁', '37-47岁', '47-57岁', '57-67岁', '67-77岁', '77-87岁']
    num_list = [round(s2m(avg(final17_27, ageNum17_27))), round(s2m(avg(final27_37, ageNum27_37))),
                            round(s2m(avg(final37_47, ageNum37_47))), round(s2m(avg(final47_57, ageNum47_57))),
                            round(s2m(avg(final57_67, ageNum57_67))),round(s2m(avg(final67_77, ageNum67_77))),
                            round(s2m(avg(final77_87, ageNum77_87)))]
    plt.figure(figsize=(10, 6))
    # 设置x轴柱子的个数
    x = np.arange(7) + 1
    y = np.array(num_list)
    xticks1 = list(name_list)
    plt.bar(x, y, width=0.8, align='center', color='c', alpha=0.8)
    plt.xticks(x, xticks1, size='small', rotation=30)
    # x、y轴标签与图形标题
    plt.xlabel('不同年龄段')
    plt.ylabel('完成时间(单位：分钟)')
    plt.title('不同年龄选手的全程平均时间差异图')
    # 设置数字标签
    for a, b in zip(x, y):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)
    # 设置y轴的范围
    plt.ylim(250, 450)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()
    # 全程#

    # 半程#
    num_list_split = [round(s2m(avg(split17_27, ageNum17_27))), round(s2m(avg(split27_37, ageNum27_37))),
                round(s2m(avg(split37_47, ageNum37_47))), round(s2m(avg(split47_57, ageNum47_57))),
                round(s2m(avg(split57_67, ageNum57_67))), round(s2m(avg(split67_77, ageNum67_77))),
                round(s2m(avg(split77_87, ageNum77_87)))]
    plt.figure(figsize=(10, 6))
    x = np.arange(7) + 1
    y = np.array(num_list_split)
    xticks2 = list(name_list)
    plt.bar(x, y, width=0.8, align='center', color='c', alpha=0.8)
    plt.xticks(x, xticks2, size='small', rotation=30)
    plt.xlabel('不同年龄段')
    plt.ylabel('完成时间(单位：分钟)')
    plt.title('不同年龄选手的半程平均时间差异图')
    for c, d in zip(x, y):
        plt.text(c, d + 0.05, '%.0f' % d, ha='center', va='bottom', fontsize=10)
    plt.ylim(0, 250)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.show()
    # 半程#
