import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re
def vcds_dealer(path,time_name="记录值"):
    """
    path : 指定的路径
    return：经过处理可以直接用的df
    """
    with open(path, "r+") as file:
        a = file.readlines()
        a = a[5:]
        units = a[1:2]
        del a[1:2]
        dflist = [i.strip(",,,,,\n").split(",") for i in a]
        try:
            df = pd.DataFrame(dflist, columns=dflist[0])
        except:
            df = pd.DataFrame(dflist)
            df.drop(df.columns[-1], axis=1, inplace=True)
            df.columns = dflist[0]
        df.drop(0, axis=0, inplace=True)
        count = 0
        df = df.astype(float)
        newdf = pd.DataFrame()
    for i in range(0, df.shape[1], 2):
        testdf = df.iloc[:, i:i + 2].copy()

        testdf[time_name] = ((testdf[time_name]).astype(float) // 1).astype(int)
        testdf[time_name] = pd.to_timedelta(testdf[time_name], unit="s")

        testdf.set_index(testdf[time_name], inplace=True)

        testdf.drop(time_name, axis=1, inplace=True)

        resampled_df = testdf.resample('S').mean()

        newdf[resampled_df.columns[0]] = resampled_df[resampled_df.columns[0]]
        count += 1
    newdf = newdf.reset_index()
    newdf.drop(time_name, inplace=True, axis=1)
    return newdf

def result_fig(df, a=0, way="gps"):
    """
    :param df: 拼接好的df
    :param a: 移动步数，默认为0
    :param way: 移动方向，可调整gps往前移动或者是vcds往前移动。具体可在main中自行打印看效果
    :return: 无 绘制vcd的速度和gps的速度曲线
    """
    if way == "obd":
        plt.figure(dpi=100, figsize=(32, 16))
        plt.plot(np.arange(len(df) - a), df["车速"][a:], label="OBD")
        plt.plot(np.arange(len(df)), df["SPEED"], label="GPS")
        plt.legend()  # 从这张图上可以看出是OBD的滞后一些
        plt.show()
    #         plt.savefig("G:/Desktop/对齐.jpg")

    #         plt.savefig("G:/Desktop/对齐.jpg")
    elif way == "gps":
        plt.figure(dpi=100, figsize=(32, 16))
        plt.plot(np.arange(len(df)), df["车速"], label="OBD")
        plt.plot(np.arange(len(df) - a), df["SPEED"][a:], label="GPS")
        plt.legend()  # 从这张图上可以看出是OBD的滞后一些
        plt.show()
def alignment_obd_forward(df, parameter,gps_speed_name,vcds_speed_name):
    """
    df:merged_df
    parameter:迭代次数
    return:返回最小的。包括均残差值和平移格数
    注：这个函数是计算的obd的移动值
    """
    datadict = {}
    for n in range(1, parameter):
        x1 = df[gps_speed_name]
        x2 = df[vcds_speed_name]
        intermediate_df = pd.DataFrame()
        x1 = x1.reset_index()
        x1.drop("index", inplace=True, axis=1)
        x2 = x2.reset_index()
        x2.drop("index", inplace=True, axis=1)
        x2 = x2[n:].reset_index().drop("index", axis=1)
        intermediate_df["x1"] = x1
        intermediate_df["x2"] = x2
        intermediate_df = intermediate_df.dropna()
        sum = np.sum(np.square(intermediate_df["x1"] - intermediate_df["x2"])) / len(intermediate_df)
        datadict[n] = sum
    alist = []
    for i in datadict:
        alist.append([datadict[i], i])
    return min(alist)
def alignment_gps_forward(df, parameter,gps_speed_name,vcds_speed_name):
    """
    df:merged_df
    parameter:迭代次数
    return:返回最小的。包括均残差值和平移格数
    注：这个函数是计算的gps的移动值
    """
    datadict = {}
    for n in range(1, parameter):
        x1 = df[gps_speed_name]
        x2 = df[vcds_speed_name]
        intermediate_df = pd.DataFrame()
        x1 = x1.reset_index()
        x1.drop("index", inplace=True, axis=1)
        x2 = x2.reset_index()
        x2.drop("index", inplace=True, axis=1)
        x1 = x1[n:].reset_index().drop("index", axis=1)
        intermediate_df["x1"] = x1
        intermediate_df["x2"] = x2
        intermediate_df = intermediate_df.dropna()
        sum = np.sum(np.square(intermediate_df["x1"] - intermediate_df["x2"])) / len(intermediate_df)
        datadict[n] = sum
    alist = []
    for i in datadict:
        alist.append([datadict[i], i])
    return min(alist)

def Comparator(df,parameter):
    residual = np.sum(np.square(df["SPEED"] - df["车速"])) / df.shape[0]  # 残差
    alignment_gps = alignment_gps_forward(df, parameter)
    alignment_obd = alignment_obd_forward(df, parameter)

    min_value = min(residual, alignment_gps[0], alignment_obd[0])
    if min_value == residual:
        print("不用修改！", residual)
    if min_value == alignment_gps[0]:
        print("gps", str(alignment_gps[1]))
    if min_value == alignment_obd[0]:
        print("obd", str(alignment_obd[1]))

if __name__ == "__main__":
    vcdsdata = vcds_dealer(rf"D:\Forerunner\data\西宁数据\探歌汽油车\vcds\20230309-西宁-探歌-4-匹配vcds.CSV","记录值")
    gpsdata = pd.read_csv(r"D:\Forerunner\data\西宁数据\探歌汽油车\gps\20230309-西宁-探歌-4-匹配gps.CSV",
                          encoding="gbk")
    data = pd.concat([vcdsdata,gpsdata],axis=1)
