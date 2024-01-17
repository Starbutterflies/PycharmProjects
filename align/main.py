from  utils import vcds_dealer,result_fig
import pandas as pd
import numpy as np
import re
class data_dealer:
    def __init__(self,gps_data,vcds_data):
        self.vcds_data = vcds_data
        self.gps_data = gps_data

    def align_segment(self,vcds_df,gpsdf, gps_name="SPEED",vcds_name="车速",keyscale=100):
        """
        vcds_df:需要对齐的vcds数据。
        gpsdf:需要对齐的gpsdf数据
        retun: 0:经过一步对齐的数据。1:100个哥们的均残差 2：新数据最高峰的位置。
        """
        id1 = vcds_df[vcds_name].idxmax()
        # print("id1是",id1)
        keyscale = int(keyscale)
        # print("keyscale是",keyscale)

        if keyscale/2 >= id1:
            keyscale = 0.3 * (id1)
            keyscale = int(keyscale)
        elif vcds_df.shape[0] <= id1 + keyscale / 2:
            keyscale = int((vcds_df.shape[0] - id1)*2)
        featuredf = vcds_df[int(id1 - keyscale / 2):int(id1 + keyscale / 2)]
        # print(vcds_df.index)
        # print("切割点位1",int(id1 - keyscale / 2))
        # print("切割点位2", int(id1 + keyscale / 2))
        # print("featuredf的形状：",featuredf.shape[0])
        residual_list = []

        for i in range(len(gpsdf) - keyscale - 1):
            mean_residual = np.nanmean((np.square(np.array(featuredf[vcds_name]) - np.array(gpsdf[i:i + keyscale][gps_name]))))

            residual_list.append(mean_residual)

        index = residual_list.index(min(residual_list))  # 三个相邻的，非常完美。

        if index + int(keyscale / 2) > id1:

            needed_gps_df = gpsdf[
                            index - id1 + int(keyscale / 2):index + len(np.array(vcds_df[id1:])) + int(keyscale / 2)]

            needed_gps_df.reset_index(inplace=True)
            intermediate_df = vcds_df.copy()
            for name in needed_gps_df:
                intermediate_df[name] = needed_gps_df[name]
            return [intermediate_df, min(residual_list), index]

        elif id1 - index >= int(keyscale / 2):
            needed_vcds_df = vcds_df[id1 - index - int(keyscale / 2):]
            needed_vcds_df.reset_index(inplace=True)
            intermediate_df = gpsdf.copy()
            for name in needed_vcds_df:
                intermediate_df[name] = needed_vcds_df[name]
            obdname = [name for name in intermediate_df.columns if re.search('[\u4e00-\u9fa5]', name)]
            gpsname = [name for name in intermediate_df.columns if re.search('^[^\u4e00-\u9fa5]+$', name)]
            dfname = obdname + gpsname
            intermediate_df = intermediate_df[dfname]
            #         print(locals()["featuredf"])
            return [intermediate_df[0:vcds_df.shape[0] - id1 + index], min(residual_list),id1 + len(vcds_df) - len(gpsdf)]  # 这下返回的位置是对的了。

    def judge_and_calculate_position(self,vcds_df,gpsdf,n, gps_name="SPEED",vcds_name="车速",keyscale=100):
        """
        result:这个东西是上一个函数的输出。
        0:经过一步对齐的数据。1:100个哥们的均残差 2：新数据最高峰的位置。
        return:返回的切割位置
        """
        df, min_square_value, max_index = self.align_segment(vcds_df,gpsdf,keyscale=keyscale)
        residual_series = np.square(df[gps_name] - df[vcds_name])
        possible_position = residual_series[residual_series > n * min_square_value]
        negative_value = [-i for i in possible_position.index - max_index if i < 0]  # 这下才对嘛
        negative_value.reverse()  # 好像似乎不该进行翻转
        positive_value = [i for i in possible_position.index - max_index if i > 0]  # 这下才对嘛
        #     print(negative_value)
        j = 1

        negative_list = []  #
        for i in range(len(negative_value) - 7):  # 这个是为了防止报错
            j += 1
            if negative_value[j + 5] - negative_value[j] <= 10:  # 这个是为了找5个小于二倍的值，返回首先得那个值。
                negative_list.append(negative_value[j])
                break

        positive_list = []

        j = 1
        for i in range(len(positive_value) - 7):
            j += 1
            if positive_value[j + 5] - positive_value[j] <= 10:
                positive_list.append(positive_value[j])
                break
        # 然后进行检查。
        if len(negative_list) == 0:
            negative_position = max_index
            print("左边没有值！")
        else:
            negative_position = negative_list[0]

        if len(positive_list) == 0:
            print("右边没有值！")
            positive_position = df.shape[0] - max_index
        else:
            positive_position = positive_list[0]  # 这个东西需要
        return (max_index - negative_position, max_index + positive_position)
    def split_data(self,vcds_data,gps_data,n=9, keyscale=100,lowest_rmse=10):
        """
        :param n: 小于几倍的残差值，n即为倍数
        :param keyscale: 钥匙的大小，默认为100
        :return: 返回切割好的三个数据集 如果说左右都没有断点，那么就返回一个玩意
        """
        try:
            vcdsdata = vcds_data.reset_index().drop("index", axis=1)
            gpsdata = gps_data.reset_index().drop("index", axis=1)
            print(vcdsdata.shape)
        except:
            print("请去掉多余的index列！")

        try:
            result = self.align_segment(vcds_data,gps_data,keyscale = keyscale)

            position = self.judge_and_calculate_position(vcdsdata,gpsdata,n)

            datalist = [result[0][:position[0]], result[0][position[0]:position[1]], result[0][position[1]:]]  # 截止目前第一步循环结束
            returndf = [df_ for df_ in datalist if df_.shape[0] !=0]

            if any(self.rmse_calculate(df) <= lowest_rmse for df in returndf):
                return returndf
            else:
                print("这个方法无法对齐了，很可能是数据有问题或者是峰值无法对齐，请尝试其他方法，若是实在没办法就请另请高明吧。")
                return [pd.DataFrame()]
        except Exception as e:
            print(e)
            # result_fig(pd.concat([vcds_data,gps_data],axis=1))
    def rmse_calculate(self,df,gps_name="SPEED",vcds_name="车速"):

        if isinstance(df,pd.DataFrame):
            return np.sum(np.square(df[gps_name] - df[vcds_name])) / len(df)
        else:
            return 0
    def iteration(self, rmse = 10,n=9, keyscale=100):
        """
        rmse: 判断标准
        :return: 最终处理出来的数据
        """
        datalist = self.split_data(self.vcds_data,self.gps_data)
        print(len(datalist)) # 现在有三个

        while any(self.rmse_calculate(df) >= rmse for df in datalist):
            new_list = []
            for df in datalist:

                if self.rmse_calculate(df) >= rmse: # 还需要一个就是进行一个judge看看用不用把数丢掉
                    print(self.split_data(df[self.vcds_data.columns],df[self.gps_data.columns]))

                else:
                    new_list.append(df)
                    print(self.rmse_calculate(df))
            datalist = new_list
            print(len(new_list))
            break

if __name__ == '__main__':
    gps_data = pd.read_csv(r"D:\Forerunner\data\西宁数据\探歌汽油车\gps\20230309-西宁-探歌-4-匹配gps.CSV")
    vcds_data = vcds_dealer(rf"D:\Forerunner\data\西宁数据\探歌汽油车\vcds\20230309-西宁-探歌-4-匹配vcds.CSV")
    a = data_dealer(gps_data,vcds_data)
    # a.iteration()

    data0,data1,data2 = a.split_data(vcds_data,gps_data)
    new_gps_data = data2[gps_data.columns].reset_index(drop=True)
    new_vcds_data = data2[vcds_data.columns].reset_index(drop=True)
    new_new_df = a.split_data(new_vcds_data,new_gps_data)

    # print(new_new_df[0])
    # result_fig(new_new_df[0])
    # # print(new_new_df)
    # new_new_df0 = a.align_segment(new_new_df[vcds_data.columns],new_new_df[gps_data.columns],keyscale=20)[0]
    # print(a.judge_and_calculate_position(new_new_df0[vcds_data.columns],new_new_df0[gps_data.columns],9,keyscale=20))
    # new_new_newdf = new_new_df0[313:].reset_index(drop=True)
    # df_list = a.split_data(new_new_newdf[vcds_data.columns],new_new_newdf[gps_data.columns])
    # df = df_list[0].reset_index(drop=True)
    # result_fig(df)
    # print(a.split_data(df[vcds_data.columns],df[gps_data.columns])[0].shape)