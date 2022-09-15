import xlrd
# 读取表格
from pyecharts.charts import Bar


def show_table(year_mon_day):
    confirm_data = xlrd.open_workbook("./新冠疫情.xls")
    # 获取表格的sheets
    confirm_table = confirm_data.sheets()[0]
    asymptomatically_table = confirm_data.sheets()[1]

    xdata = []
    ydata_confirm = []
    ydata_asymptomatically = []

    row = 0
    for i in range(1, confirm_table.nrows):
        if confirm_table.row_values(i)[0] == year_mon_day:
            row = i
            break
    for i in range(2, confirm_table.ncols):
        xdata.append(confirm_table.row_values(0)[i])
        ydata_confirm.append(confirm_table.row_values(row)[i])
        ydata_asymptomatically.append(asymptomatically_table.row_values(row)[i])

    # 数据可视化，柱状图
    bar = Bar()
    bar.add_xaxis(xdata)
    bar.add_yaxis("新增确诊", ydata_confirm)
    bar.add_yaxis("新增无症状", ydata_asymptomatically)
    bar.render("show_table.html")
