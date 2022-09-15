import re

# 23个省分别为：河北省、山西省、辽宁省、吉林省、黑龙江省、江苏省、浙江省、安徽省、福建省、江西省、山东省、河南省、湖北省、湖南省、广东省、海南省、四川省、
# 贵州省、云南省、陕西省、甘肃省、青海省、台湾省。
# 5个自治区分别为：内蒙古自治区、广西壮族自治区、西藏自治区、宁夏回族自治区、新疆维吾尔自治区。
# 4个直辖市分别为：北京市、天津市、上海市、重庆市。
# 2个特别行政区分别为：香港特别行政区、澳门特别行政区。
confirm_add = {'date': [], 'mainland_confirm_add': [], 'hebei': [], 'shanxi_dong': [], 'liaoning': [], 'jilin': [],
               'heilongjiang': [],
               'jiangsu': [], 'zhejiang': [], 'anhui': [], 'fujian': [], 'jiangxi': [], 'shandong': [], 'henan': [],
               'hubei': [], 'hunan': [], 'guangdong': [],
               'hainan': [], 'sichuan': [], 'guizhou': [], 'yunnan': [], 'shanxi': [], 'gansu': [], 'qinghai': [],
               'neimenggu': [], 'guangxi': [],
               'xizang': [], 'ningxia': [], 'xinjiang': [], 'beijing': [], 'tianjin': [], 'shanghai': [],
               'chongqing': []}
asymptomatically_add = {'date': [], 'mainland_asymptomatically_add': [], 'hebei': [], 'shanxi_dong': [], 'liaoning': [],
                        'jilin': [], 'heilongjiang': [],
                        'jiangsu': [], 'zhejiang': [], 'anhui': [], 'fujian': [], 'jiangxi': [], 'shandong': [],
                        'henan': [], 'hubei': [], 'hunan': [], 'guangdong': [],
                        'hainan': [], 'sichuan': [], 'guizhou': [], 'yunnan': [], 'shanxi': [], 'gansu': [],
                        'qinghai': [], 'neimenggu': [], 'guangxi': [],
                        'xizang': [], 'ningxia': [], 'xinjiang': [], 'beijing': [], 'tianjin': [], 'shanghai': [],
                        'chongqing': []}

# 港澳台没有完成相应匹配代码，所以没有统计
confirm_add_gat = {'xianggang': [], 'aomen': [], 'taiwan': []}

province_all = {'河北': 'hebei', '山西': 'shanxi_dong', '辽宁': 'liaoning', '吉林': 'jilin', '黑龙江': 'heilongjiang',
                '江苏': 'jiangsu', '浙江': 'zhejiang',
                '安徽': 'anhui', '福建': 'fujian', '江西': 'jiangxi', '山东': 'shandong', '河南': 'henan', '湖北': 'hubei',
                '湖南': 'hunan', '广东': 'guangdong',
                '海南': 'hainan', '四川': 'sichuan', '贵州': 'guizhou', '云南': 'yunnan', '陕西': 'shanxi', '甘肃': 'gansu',
                '青海': 'qinghai', '内蒙古': 'neimenggu',
                '广西': 'guangxi', '西藏': 'xizang', '宁夏': 'ningxia', '新疆': 'xinjiang', '北京': 'beijing',
                '天津': 'tianjin', '上海': 'shanghai',
                '重庆': 'chongqing'}


def match(content):
    # 匹配各省新增确诊函数
    def match_confirm_add_province(province, province_pinyin):
        if re.search('{}(.*?)例'.format(province), confirm_text.group(0), re.DOTALL):
            confirm_add_num = (re.search('{}(.*?)例'.format(province), confirm_text.group(0), re.DOTALL)).group(1)
            confirm_add[province_pinyin].append(confirm_add_num)
        else:
            confirm_add[province_pinyin].append('0')

    # 匹配各省新增无症状函数
    def match_asymptomatically_add_province(province, province_pinyin):
        if re.search('{}(.*?)例'.format(province), asymptomatically_text.group(0), re.DOTALL):
            asymptomatically_add_num = re.search('{}(.*?)例'.format(province), asymptomatically_text.group(0),
                                                 re.DOTALL).group(1)
            asymptomatically_add[province_pinyin].append(asymptomatically_add_num)
        else:
            asymptomatically_add[province_pinyin].append('0')

    # 匹配各省新增确诊属于一个省，本土13例（均在广东）
    def match_only_confirm_province(province, province_pinyin):
        if re.search('（.*{}'.format(province), confirm_text.group(0), re.DOTALL):
            confirm_add[province_pinyin].append(confirm_text.group(1))

    # 匹配各省新增无症状属于一个省
    def match_only_asymptomatically_province(province, province_pinyin):
        if re.search('（.*{}'.format(province), asymptomatically_text.group(0), re.DOTALL):
            asymptomatically_add[province_pinyin].append(asymptomatically_text.group(1))

    # 从卫健委爬取的文章做一次裁剪，保留本土病例新增确诊那句就好了
    confirm_text = re.search('本土病例(\d*)例（.*?）', content, re.DOTALL)

    #从卫健委爬取的文章做一次裁剪，保留本土病例新增无症状那句就好了
    asymptomatically_text = re.search('新增无症状感染者\d*例.*?本土(\d*)例（.*?）', content, re.DOTALL)
    # print(confirm_text.group(0))
    # print(asymptomatically_text.group(0))

    # 大陆每日新增确诊
    if confirm_text is None:
        confirm_add['mainland_confirm_add'].append('0')
    elif re.search('（.*\d', confirm_text.group(0), re.DOTALL) is None:
        for i in province_all:
            match_only_confirm_province(i, province_all[i])
    else:
        mainland_confirm_add_num = confirm_text.group(1)
        confirm_add['mainland_confirm_add'].append(mainland_confirm_add_num)
        # 各省每日新增
        for i in province_all:
            match_confirm_add_province(i, province_all[i])
    # 本土病例196例（四川127例，北京18例，山东10例，西藏8例，内蒙古7例，广西7例，广东6例，湖南4例，贵州3例，江西2例，黑龙江1例，上海1例，重庆1例，新疆1例）
    # 大陆每日新增无症状
    if asymptomatically_text is None:
        asymptomatically_add['mainland_asymptomatically_add'].append('0')
    elif re.search('（.*\d', asymptomatically_text.group(0), re.DOTALL) is None:
        for i in province_all:
            match_only_asymptomatically_province(i, province_all[i])
    else:
        mainland_asymptomatically_add_num = asymptomatically_text.group(1)
        asymptomatically_add['mainland_asymptomatically_add'].append(mainland_asymptomatically_add_num)
        # 各省每日新增无症状
        for i in province_all:
            match_asymptomatically_add_province(i, province_all[i])
