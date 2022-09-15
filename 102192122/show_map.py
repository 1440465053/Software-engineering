import xlrd
from pyecharts.charts import Bar


def show_map():
    # 读取表格
    confirm_data = xlrd.open_workbook("./新冠疫情.xls")
    # 获取表格的sheets
    confirm_table = confirm_data.sheets()[0]
    asymptomatically_table = confirm_data.sheets()[1]

    # X轴对应日期，y轴对应每天新增确诊和无症状
    xdata = []
    ydata_confirm = []
    ydata_asymptomatically = []

    # 获取表格对应数据
    for i in range(1, confirm_table.nrows):
        xdata.append(confirm_table.col_values(0)[i])
        ydata_confirm.append(confirm_table.col_values(1)[i])
        ydata_asymptomatically.append(asymptomatically_table.col_values(1)[i])

    # 数据可视化，柱状图
    bar = Bar()
    bar.add_xaxis(xdata)
    bar.add_yaxis("新增确诊", ydata_confirm,is_large =True)
    bar.add_yaxis("新增无症状", ydata_asymptomatically,is_large =True)
    bar.render("show_map.html")
