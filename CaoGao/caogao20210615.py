#!/usr/bin/python3
# -*- coding:utf-8 -*-

remark = '''获取当前价格'''


response={'words_result': [{'words': '概念:一个力作用在物体上', 'location': {'top': 11, 'left': 181, 'width': 258, 'height': 24}}, {'words': '物体在这个力的方向移动了一段距离', 'location': {'top': 37, 'left': 240, 'width': 346, 'height': 24}}, {'words': '1功', 'location': {'top': 67, 'left': 118, 'width': 33, 'height': 21}}, {'words': '公式: W = f S ', 'location': {'top': 65, 'left': 180, 'width': 122, 'height': 22}}, {'words': '单位:焦耳(j) 1 J = 1 N . m ', 'location': {'top': 91, 'left': 176, 'width': 276, 'height': 22}}, {'words': '功的原理:使用任何机械都不省功', 'location': {'top': 113, 'left': 178, 'width': 310, 'height': 24}}, {'words': '概念:做功的快慢', 'location': {'top': 141, 'left': 193, 'width': 162, 'height': 24}}, {'words': '定义:单位时间内做的功', 'location': {'top': 170, 'left': 193, 'width': 225, 'height': 25}}, {'words': '功和功率2功', 'location': {'top': 190, 'left': 4, 'width': 149, 'height': 26}}, {'words': '公式: P = W J  tP=FV(匀速)', 'location': {'top': 197, 'left': 200, 'width': 249, 'height': 28}}, {'words': '单位:瓦特(W) 1 M = 1 J / s ', 'location': {'top': 225, 'left': 200, 'width': 257, 'height': 25}}, {'words': '定义:有用功跟总功的比值', 'location': {'top': 256, 'left': 240, 'width': 250, 'height': 24}}, {'words': '公式 \\eta = W \\Leftrightarrow R , w , w \\notin R + W \\phi \\ne W _ { + } ', 'location': {'top': 285, 'left': 233, 'width': 355, 'height': 24}}, {'words': '3机械效率', 'location': {'top': 322, 'left': 109, 'width': 98, 'height': 23}}, {'words': '提高方法:减轻机械的自重,减小摩擦', 'location': {'top': 310, 'left': 232, 'width': 359, 'height': 23}}, {'words': '斜面', 'location': {'top': 346, 'left': 300, 'width': 42, 'height': 28}}, {'words': 'S _ { n } = \\frac { s i n ^ { 2 } } { s i n 3 0 ^ { \\circ } } ', 'location': {'top': 330, 'left': 354, 'width': 151, 'height': 67}}, {'words': '应用', 'location': {'top': 385, 'left': 236, 'width': 37, 'height': 22}}, {'words': '倾斜程度有关', 'location': {'top': 375, 'left': 500, 'width': 126, 'height': 24}}, {'words': 'ghg', 'location': {'top': 401, 'left': 422, 'width': 71, 'height': 19}}, {'words': '滑轮组:n=fs=nf', 'location': {'top': 415, 'left': 300, 'width': 208, 'height': 24}}, {'words': 'n与物重和动滑轮重有关', 'location': {'top': 439, 'left': 383, 'width': 231, 'height': 24}}, {'words': '(不计摩擦', 'location': {'top': 466, 'left': 383, 'width': 93, 'height': 24}}], 'log_id': 1404834023942914048, 'words_result_num': 23}

print(type(response))


# [print(one["words"]) for one in response['words_result']]




for one in response.json()["words_result"]:
    if one["words"].startswith('公式'):
        print(one["words"])
