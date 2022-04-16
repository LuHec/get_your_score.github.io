# -*- coding = utf-8 -*-
# @Time : 2022/4/16 18:29
# @Author : Luhe
# @File : main.py
# @SofWare: PyCharm

import requests
from bs4 import BeautifulSoup
import csv


def get_lesson(response_lesson):
    lesson_list = []
    for value in response_lesson['kbList']:
        every_list = [value['kcmc'], value['xm'], value['xqjmc'], value['cdmc'], value['zcd'], value['kcxz'], value['xf']]
        lesson_list.append(every_list)
    return lesson_list


def get_exam(response_exam):
    exam_list = []
    for value in response_exam['items']:
        every_list = [value['kcmc'], value['dateDigit'], value['cj'], value['jd'], value['xm'], value['jgmc']]
        exam_list.append(every_list)

    return exam_list


if __name__ == '__main__':
    lesson_url = 'http://10.2.1.94/jwglxt/kbcx/xskbcx_cxXsgrkb.html?gnmkdm=N253508&su=210501050120'
    score_url = 'http://10.2.1.94/jwglxt/cjcx/cjcx_cxXsgrcj.html?doType=query&gnmkdm=N305005&su=210501050120'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39 ',
        'Cookie': 'JSESSIONID=F1A1DE52BA451CE167A20BB8FBA6DCB1; route=ec9f1523782f6fc8f64960f81492aa8e'
    }

    lesson_data = {
        'xnm': '2021',
        'xqm': '12',
        'xqh_id': '1',
    }
    score_data = {
        'xnm': '2021',
        'xqm': '3',
        '_search': 'false',
        'nd': '1650118441144',
        'queryModel.showCount': '15',
        'queryModel.currentPage': '1',
        'queryModel.sortName': '',
        'queryModel.sortOrder': 'asc',
        'time': '3',
    }
    response_exam = requests.post(url=score_url, headers=headers, data=score_data).json()
    response_lesson = requests.post(url=lesson_url, headers=headers, data=lesson_data).json()

    lesson_list = get_lesson(response_lesson)
    exam_list = get_exam(response_exam);

    with open('exam.csv', 'w', newline='', encoding='utf-8') as f:
        for exam in exam_list:
            writer = csv.writer(f)
            writer.writerow(exam)

    with open('lesson.csv', 'w', newline='', encoding='utf-8') as f:
        for lesson in lesson_list:
            writer = csv.writer(f)
            writer.writerow(lesson)