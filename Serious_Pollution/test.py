import os
import calmap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def heatmap_data(data1, data2, data3):

    value1 = []

    all_day = pd.date_range('01/01/2017', periods=1095, freq='1D')

    for i in range(365):
        value1.append(data1["Value"][i])

    for i in range(365):
        value1.append(data2["Value"][i])

    for i in range(365):
        value1.append(data3["Value"][i])

    events = pd.Series(value1, index=all_day)

    fig, ax=calmap.calendarplot(events, linewidth=0, fig_kws=dict(figsize=(17,8))) 

    fig.colorbar(ax[0].get_children()[1], ax=ax.ravel().tolist()) 
    plt.show(fig)


if __name__ == '__main__':

    import time
    start_time = time.time()
  
    main = ["107年嘉義站_20190315.xls", "107年麥寮站_20190315.xls", "107年臺東站_20190315.xls"]

    df1 = pd.read_excel(main[0])
    df2 = pd.read_excel(main[1])
    df3 = pd.read_excel(main[2])

    heatmap_data(df1, df2, df3)   
                
    print("--- %s seconds ---" % (time.time() - start_time))