import get_data
import match_data
import saveFile
import show_map
import show_table


def main(page_star, page_end):

    # 获取卫健委从第几页到第几页的数据
    for url in get_data.getPageUrl(page_star, page_end):
        s = get_data.fetchUrl(url)

        # 获取标题，链接，和日期
        for title, link, date in get_data.getTitleUrl(s):
            # 如果日期在2020年1月21日之前，则直接退出
            year = int(date.split("-")[0])
            mon = int(date.split("-")[1])
            day = int(date.split("-")[2])
            if year < 2020 and mon <= 1 and day - 1 < 21:  # 最后一页
                break;
            # 获取每日文章链接
            html = get_data.fetchUrl(link)
            # 获取链接内容
            content = get_data.getContent(html)
            # 进行关键子抓取
            match_data.match(content)
            # 将日期加入到字典
            match_data.confirm_add["date"].append(date)
            match_data.asymptomatically_add["date"].append(date)

            # print(content)
            # saveFile("/text/", date, content)
            # print(confirm_add)
            # print(asymptomatically_add)


if "__main__" == __name__:
    # 抓取第一页到第10页的数据
    main(1, 10)
    # 保存数据到EXCEL
    saveFile('./新冠疫情.xls')
    # 绘制 某天的每日新增确诊和无症状数据柱状图
    show_table("2022-09-13")
    # 绘制 每日大陆新增数据柱状图
    show_map()