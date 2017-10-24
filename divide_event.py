import pandas as pd
import numpy as np
#数据预处理
data=pd.read_excel("original_data.xls")
data=data[["发生时间","开关机状态","加热中","保温中","实际温度","热水量","水流量","加热剩余时间","当前设置温度"]]
# data=data[-((data["开关机状态"]=="关")&(data["水流量"]==0))]
# data=data[(data["开关机状态"]=="开")|(data["水流量"]!=0)]
data=data[data.notnull()]
#划分一次用水事件
#用水事件阈值寻优模型，由于不同地区或不同季节使用热水器停顿时长可能不同
n=4
data=data[data["水流量"]>0]
data["发生时间"]=pd.to_datetime(data["发生时间"],format="%Y%m%d%H%M%S")
dt=[pd.Timedelta(minutes=i) for i in  np.arange(1,9,0.25)]
def event(ts):
    d=data["发生时间"].diff()>ts
    return d.sum()+1
h=pd.DataFrame(dt,columns=["阈值"])
h["事件数"]=h["阈值"].apply(event)
h["斜率"]=h["事件数"].diff()/0.25
h["斜率指标"]=pd.rolling_mean(h["斜率"].abs(),n)
ts=h["阈值"][h["斜率指标"].idxmin()-n]
threshold=pd.Timedelta(minutes=5)#专家值
if ts>threshold:
    ts=pd.Timedelta(minutes=4)
d=data["发生时间"].diff()>ts
data["事件编号"]=d.cumsum()+1
# outputfile="dividesequence.xls"
# data.to_excle(outputfile)
#属性构造


print (data)