import pymongo
import re
from collections import Counter

# 使用mongodb数据库
client = pymongo.MongoClient()
db = client.jobs
collection = db.lg

lst = []
cities = []
positionLables = []
salary = []
workYear = []
avg_salary = []
avg0_salary = []
avg1_salary = []
avg2_salary = []
avg3_salary = []
companySize =[]
# 提取不同城市职位数量
def get_city():
    for data in collection.find():
        city = data.get('city')
        cities.append(city)
    most_lst = Counter(cities).most_common()
    print(most_lst)

# 提取职位标签
def get_Lable():
    for data in collection.find():
        positionLable = data.get('positionLables')
        for p in positionLable:
            positionLables.append(p)
    most_lst = Counter(positionLables).most_common()
    for item in most_lst:
        print("{\t\nname:'%s',\nvalue:%d\t\n}," % item)

# 提取薪水与城市|年限的关系
def get_salary():
    for data in collection.find():
        lst.append(data)
    l = [i for i in lst if i['city']== "北京"]
    print(len(l))

    def exp():
        for i in l:
            s = i.get('salary')
            s_lst = s.split('-')
            s_min = float(s_lst[0].strip('kK'))
            s_max = float(s_lst[1].strip('kK'))
            s_avg = float(s_min + s_max) / 2
            avg_salary.append(s_avg)
        most_lst = Counter(avg_salary).most_common()
        most_lst.sort()
    exp()
    # 年限不限
    def exp0():
        a = [i for i in l if i['workYear'] == "不限"]
        for data1 in a:
            s0 = data1.get('salary')
            s0_lst = s0.split('-')
            s0_min = float(s0_lst[0].strip('kK'))
            s0_max = float(s0_lst[1].strip('kK'))
            s0_avg = float(s0_min + s0_max) / 2
            avg0_salary.append(s0_avg)
        most_lst0 = Counter(avg0_salary).most_common()
        print('=====不限======')
        most_lst0.sort()
        print(most_lst0)
        #print(most_lst0)
    exp0()

    def exp1():
        b = [i for i in l if i['workYear'] == "1-3年"]
        for data1 in b:
            s1 = data1.get('salary')
            s1_lst = s1.split('-')
            s1_min = float(s1_lst[0].strip('kK'))
            s1_max = float(s1_lst[1].strip('kK'))
            s1_avg = float(s1_min + s1_max) / 2
            avg1_salary.append(s1_avg)
        most_lst1 = Counter(avg_salary).most_common()
        print('=====1-3年======')
        most_lst1.sort()
        print(most_lst1)
    exp1()

    def exp2():
        c = [i for i in l if i['workYear'] == "3-5年"]
        for data1 in c:
            s2 = data1.get('salary')
            s2_lst = s2.split('-')
            s2_min = float(s2_lst[0].strip('kK'))
            s2_max = float(s2_lst[1].strip('kK'))
            s2_avg = float(s2_min + s2_max) / 2
            avg2_salary.append(s2_avg)
        most_lst2 = Counter(avg2_salary).most_common()
        print('=====3-5年======')
        most_lst2.sort()
        print(most_lst2)
    exp2()

    def exp3():
        d = [i for i in l if i['workYear'] == "5-10年"]
        for data1 in d:
            s3 = data1.get('salary')
            s3_lst = s3.split('-')
            s3_min = float(s3_lst[0].strip('kK'))
            s3_max = float(s3_lst[1].strip('kK'))
            s3_avg = float(s3_min + s3_max) / 2
            avg3_salary.append(s3_avg)
        most_lst3 = Counter(avg3_salary).most_common()
        print('=====5-10年======')
        most_lst3.sort()
        print(most_lst3)
    exp3()

# 使用python的公司规模
def get_companySize():
    num = 0
    for data in collection.find():
        size= data.get('companySize')
        companySize.append(size)
    most_lst = Counter(companySize).most_common()
    print(most_lst)
    for item in most_lst:
        print("{name:'%s',value:%d}," % item)
    for item in most_lst:
        num += item[1]
    print(num)
get_companySize()



