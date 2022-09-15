import xlwt
import match_data


def saveFile(path):
    table = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet_confirm = table.add_sheet('每日新增确诊', cell_overwrite_ok=True)
    sheet_asymptomatically = table.add_sheet('每日新增无症状', cell_overwrite_ok=True)
    col = ('日期', '中国大陆', '河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东',
           '海南', '四川', '贵州', '云南', '陕西', '甘肃', '青海', '内蒙古', '广西', '西藏', '宁夏', '新疆', '北京', '天津', '上海', '重庆')
    # 设置第一行为日期、各个省份
    for i in range(len(col)):
        sheet_confirm.write(0, i, col[i])
        sheet_asymptomatically.write(0, i, col[i])
    m = 0
    # 将每日新增确诊数据写入sheet_confirm表
    for j in match_data.confirm_add.keys():
        list_1 = list(match_data.confirm_add[j])
        for k in range(len(list_1)):
            sheet_confirm.write(k + 1, m, list_1[k])
        m += 1
    # 将每日新增无症状输入写入sheet_asymptomatically
    m = 0
    for n in match_data.asymptomatically_add.keys():
        list_2 = list(match_data.asymptomatically_add[n])
        for a in range(len(list_2)):
            sheet_asymptomatically.write(a + 1, m, list_2[a])
        m += 1

    # 保存相应路径
    savepath = path
    table.save(savepath)