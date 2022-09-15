import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup


async def pyppteer_fetchUrl(url):
    browser = await launch({'headless': False, 'dumpio': True, 'autoClose': True})
    page = await browser.newPage()

    await page.goto(url)  # 加不加timeout都报超时错误
    await asyncio.wait([asyncio.create_task(page.waitForNavigation())])
    # await asyncio.wait([page.waitForNavigation()])，过时报错，虽然不影响
    # asyncio.create_task([page.waitForNavigation()])
    str = await page.content()
    await browser.close()
    return str


def fetchUrl(url):
    return asyncio.get_event_loop().run_until_complete(pyppteer_fetchUrl(url))


def getPageUrl(page__star=1, page__end=5):
    if page__end == 1:
        yield 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml'
    for page in range(page__star, page__end):
        if page == 1:
            yield 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml'
        else:
            url = 'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd_' + str(page) + '.shtml'
            yield url


def getTitleUrl(html):
    bsobj = BeautifulSoup(html, 'html.parser')
    titleList = bsobj.find('div', attrs={"class": "list"}).ul.find_all("li")
    for item in titleList:
        link = "http://www.nhc.gov.cn" + item.a["href"];
        title = item.a["title"]
        date = item.span.text
        yield title, link, date


def getContent(html):
    bsobj = BeautifulSoup(html, 'html.parser')
    cnt = bsobj.find('div', attrs={"id": "xw_box"}).find_all("p")
    s = ""
    if cnt:
        for item in cnt:
            s += item.text
        return s

    return "爬取失败！"
