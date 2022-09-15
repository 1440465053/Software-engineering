import xlwt
from Pxx.match_data import confirm_add, asymptomatically_add


def saveFile(path):
    table = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet_confirm = table.add_sheet('每日新增确诊', cell_overwrite_ok=True)
    sheet_asymptomatically = table.add_sheet('每日新增无症状', cell_overwrite_ok=True)
    col = ('日期', '中国大陆', '河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东',
           '海南', '四川', '贵州', '云南', '陕西', '甘肃', '青海', '内蒙古', '广西', '西藏', '宁夏', '新疆', '北京', '天津', '上海', '重庆')
    for i in range(len(col)):
        sheet_confirm.write(0, i, col[i])
        sheet_asymptomatically.write(0, i, col[i])
    m = 0
    for j in confirm_add.keys():
        list_1 = list(confirm_add[j])
        for k in range(len(list_1)):
            sheet_confirm.write(k + 1, m, list_1[k])
        m += 1
    m = 0
    for n in asymptomatically_add.keys():
        list_2 = list(asymptomatically_add[n])
        for a in range(len(list_2)):
            sheet_asymptomatically.write(a + 1, m, list_2[a])
        m += 1

    savepath = path
    table.save(savepath)