from Pxx.get_data import getPageUrl, fetchUrl, getTitleUrl, getContent
from Pxx.match_data import match, confirm_add, asymptomatically_add
from Pxx.saveFile import saveFile
from Pxx.show_map import show_map
from Pxx.show_table import show_table


def main(page_star, page_end):
    for url in getPageUrl(page_star, page_end):
        s = fetchUrl(url)
        for title, link, date in getTitleUrl(s):
            # print(title, link)
            # 如果日期在2020年1月21日之前，则直接退出
            year = int(date.split("-")[0])
            mon = int(date.split("-")[1])
            day = int(date.split("-")[2])
            if year < 2021 and mon <= 9 and day - 1 < 12:  # 最后一页
                break;
            html = fetchUrl(link)
            content = getContent(html)
            match(content)
            confirm_add["date"].append(date)
            asymptomatically_add["date"].append(date)
            # print(content)
            # saveFile("/text/", date, content)
            # print("-----"*20)
            # print(confirm_add)
            # print(asymptomatically_add)


if "__main__" == __name__:
    # main(1, 10)
    # saveFile('./新冠疫情.xls')
    # show_table("2022-09-13")
    show_map()