
import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
import pandas as pd

number=400
for pages in range(1,number):
    url = f'https://www.truecar.com/used-cars-for-sale/listings/?page={number}'
    myrequest=requests.get(url)
    soup=BeautifulSoup(myrequest.text,'html.parser')
    # print(soup.text)
    show_money=soup.select('div.vehicle-card-bottom-pricing-secondary')
    show_mile=soup.select('div.truncate.text-xs')
    show_model=soup.select('div.vehicle-card-header.w-full')
    pat=re.compile(r'(\d+,\d+) miles')
    my_model_money = []
    for money, model, mile in zip(show_money, show_model, show_mile):
        if pat.match(mile.text):
            my_model_money.append(( model.text, money.text, mile.text))
    # ساخت یک دیتا بیس
    my_head=['model car','money' ,'miles']
    df=pd.DataFrame(my_model_money, columns=my_head)
    df.to_csv('E:/.python and every thing/files/csv files/car-truecat/car_kharegi11.csv',header=True,index=False,mode='a')
    #        model car           money      miles
    # 0  Sponsored2020 BMW X5  $47,919  37,926 miles
    # 1     2019 BMW 5 Series  $41,489  61,164 miles
    # 2     2021 BMW 5 Series  $40,971  24,380 miles

# روش حذف ستون هایی که اضافه اومدند
df1=pd.read_csv('E:/.python and every thing/files/csv files/car-truecat/car_kharegi11.csv',delimiter=',')
# print(df1)
df2=df1[df1.money.str.contains('money')==False]
df2=df2.reset_index()
df2.to_csv('E:/.python and every thing/files/csv files/car-truecat/car_kharegi12.csv', index=False)






