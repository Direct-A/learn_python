#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: syc
# Date: 2021-03-24 08:52:52
# Version: 0.1
# Description: learn urllib


import json
import colorama
import requests
from bs4 import BeautifulSoup

# req_bili = request.Request("https://www.bilibili.com")
# print(req_bili.read().decode("utf-8"))

# url = "https://www.medsci.cn/sci/nsfc.do?page=1&project_classname_list=%E9%9D%A2%E4%B8%8A%E9%A1%B9%E7%9B%AE%2C%E9%9D%92%E5%B9%B4%E7%A7%91%E5%AD%A6%E5%9F%BA%E9%87%91%E9%A1%B9%E7%9B%AE%2C%E7%94%9F%E5%91%BD%E7%A7%91%E5%AD%A6%2C%E5%8C%BB%E5%AD%A6%E7%A7%91%E5%AD%A6%2C%E9%87%8D%E7%82%B9%E9%A1%B9%E7%9B%AE%2C%E9%9D%92%E5%B9%B4%E9%A1%B9%E7%9B%AE%2C%E9%87%8D%E5%A4%A7%E9%A1%B9%E7%9B%AE%2C%E9%9D%92%E5%B9%B4%E5%9F%BA%E9%87%91%2C%E5%9B%BD%E5%AE%B6%E6%9D%B0%E5%87%BA%E9%9D%92%E5%B9%B4%E7%A7%91%E5%AD%A6%E5%9F%BA%E9%87%91&sort_type=3"


def request_dd(url):
    """request_dd send get request to server use url

    Args:
        url (str): dangdang top book link

    Returns:
        obj: html responce from server
    """
    try:
        rsp = requests.get(url)
        if rsp.status_code == 200:
            return rsp
    except requests.RequestException:
        return None


def cutter(soup: object, selector: str, strings: list) -> list:
    """cutter tidy web data

    Args:
        soup (object): BeautifulSoup(html, "html.parser)
        sp (str): seletor behind

    Returns:
        list: tiddied data
    """

    items = soup.select(selector)
    all_items = []

    for item in items:
        item = item.get_text()
        for garb in strings:
            item = item.replace(str(garb), "")
        all_items.append(item)

    return all_items


def main(page):
    url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-{}".format(page)

    html = request_dd(url)
    soup = BeautifulSoup(html.text, "html.parser")
    selector = "body > div.bang_wrapper > div.bang_content > div.bang_list_box > ul > li > "

    b_ranks = cutter(soup, selector + "div.list_num", ["\n", ".", " "])
    b_names = cutter(soup, selector + "div.name > a", ["\n", " "])
    b_authors = cutter(soup, selector + "div:nth-child(5)", ["\n", " "])
    b_stars = cutter(soup, selector +
                     "div.star > span.tuijian", ["\n", "推荐", " "])
    b_counts = cutter(
        soup, selector + "div.biaosheng > span", ["\n", "次", " "])
    b_prices = cutter(
        soup, selector + "div.price > p:nth-child(1) > span.price_n", ["\n", "¥", " "])

    b_pic = soup.select(selector + "div.pic > a > img")
    b_pics = []
    for i in b_pic:
        b_pics.append(i.get("src"))

    with open("data_dd_booktop500", "a") as file:
        for i in range(len(b_ranks)):
            data = {
                "rank": b_ranks[i],
                "name": b_names[i],
                "author": b_authors[i],
                "pic": b_pics[i],
                "star": b_stars[i],
                "comment": b_counts[i],
                "price": b_prices[i]
            }
            print(colorama.Fore.GREEN +
                  colorama.Style.BRIGHT +
                  "==> Writing" +
                  colorama.Style.RESET_ALL +
                  str(data)
                  )
            file.write(json.dumps(data, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    for page in range(26):
        main(page)
