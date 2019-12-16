import os
import calmap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def heatmap_data(data1, data2, data3):

    value1 = []
    value2 = []
    value3 = []

    all_day = pd.date_range('01/01/2018', periods=365, freq='D')

    for i in range(365):
        value1.append(data1["Value"][i])
        value2.append(data2["Value"][i])
        value3.append(data3["Value"][i])

    events1 = pd.Series(value1, index=all_day)
    events2 = pd.Series(value2, index=all_day)
    events3 = pd.Series(value3, index=all_day)

    fig1 = plt.figure(figsize=(20,8))
    #fig2 = plt.figure(figsize=(20,8))
    #fig3 = plt.figure(figsize=(20,8))

    #plt.subplot(3, 1, 1)
    #cax1 = calmap.yearplot(events1, year = 2018)
    #fig1.suptitle('2018 Chaiyi Chaiyi', fontsize = 20, y = 0.65)
    
    #plt.subplot(3, 1, 2) 
    #cax2 = calmap.yearplot(events2, year = 2018)
    #fig1.suptitle('2018 Yulin Mailiao', fontsize = 20, y = 0.05)
    
    #plt.subplot(3, 1, 3)
    cax3 = calmap.yearplot(events3, year = 2018)
    #fig1.colorbar(cax1.get_children()[1], cax=cax1, ax=cax1)
    #plt.plot(fig1)
    #fig2.colorbar(cax1.get_children()[1], cax=cax2, ax=cax2)
    #plt.plot(fig2)
    fig1.colorbar(cax3.get_children()[1], cax=cax3, ax=cax3)
    #plt.plot(fig3)
    fig1.suptitle('2018 Taitung Taitung', fontsize = 20, y = 0.85)

    plt.show()



if __name__ == '__main__':

    import time
    start_time = time.time()
  
    main = ["107年嘉義站_20190315.xls", "107年麥寮站_20190315.xls", "107年臺東站_20190315.xls"]

    df1 = pd.read_excel(main[0])
    df2 = pd.read_excel(main[1])
    df3 = pd.read_excel(main[2])

    heatmap_data(df1, df2, df3)   
                
    print("--- %s seconds ---" % (time.time() - start_time))