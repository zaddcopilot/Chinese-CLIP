# -*- coding: utf-8 -*-
from PIL import Image
from io import BytesIO
import base64
import os
import sys

path = '/Users/zhangdong/work/ai_comp/data/'
img_type = 'jpg'

tsv_file = 'test.tsv'

num = 1


def img_2_base64(file_name):
    full_path = path + file_name
    img = Image.open(full_path) # 访问图片路径
    img_buffer = BytesIO()
    img.save(img_buffer, format=img.format)
    byte_data = img_buffer.getvalue()
    base64_str = base64.b64encode(byte_data) # bytes
    base64_str = base64_str.decode("utf-8") # str
    return base64_str


def base64_2_img(base64_str, id):
    img_data = base64.b64decode(base64_str)
    img = Image.open(BytesIO(img_data))
    img_name = str(id) + '.' + img_type
    img.save(img_name, 'JPEG')


# 将tsv文件中base64字符串转换为图片
def get_base64_img(tsv):
    count = 0
    with open(tsv, 'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            img_id, base64_str = line.split('\t')
            base64_2_img(base64_str, img_id)
            count += 1
            if count == num:
                break


# 生成tsv文件
def get_tsv(path):
    with open(tsv_file, 'w') as f:
        for file in os.listdir(path):
            f_type = file.split(".")[1]
            if f_type != img_type:
                continue
            img_2_base64(file)
            img_id = file.split(".")[0]
            f.write(img_id + '\t' + img_2_base64(file) + '\n')


if __name__ == '__main__':
    # img_2_base64('1.jpg')
    get_tsv(path)
