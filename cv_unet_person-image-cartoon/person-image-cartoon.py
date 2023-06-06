#pip install "modelscope[cv]" -f https://modelscope.oss-cn-beijing.aliyuncs.com/releases/repo.html
#pip install gradio

import os
import datetime
import imageio
import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from tqdm import tqdm
import numpy as np

#获取当前北京时间
utc_dt = datetime.datetime.utcnow()
beijing_dt = utc_dt.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
formatted = beijing_dt.strftime("%Y-%m-%d_%H")
print(f"北京时间: {beijing_dt.year}年{beijing_dt.month}月{beijing_dt.day}日 "
      f"{beijing_dt.hour}时{beijing_dt.minute}分{beijing_dt.second}秒")
#创建作品存放目录
works_path = './drive/MyDrive/colab_data/works_cv_unet_person-image-cartoon/' + formatted
if not os.path.exists(works_path):
  os.makedirs(works_path)
print('作品目录：' + works_path)
#原始图片
source_image_path = './drive/MyDrive/colab_data/examples/input3.png'

models = ['damo/cv_unet_person-image-cartoon-sd-illustration_compound-models', 'damo/cv_unet_person-image-cartoon-3d_compound-models', 'damo/cv_unet_person-image-cartoon-handdrawn_compound-models', 'damo/cv_unet_person-image-cartoon-artstyle_compound-models', 'damo/cv_unet_person-image-cartoon-sd-design_compound-models', 'damo/cv_unet_person-image-cartoon_compound-models', 'damo/cv_unet_person-image-cartoon-sketch_compound-models', 'lskhh/moran-cv_unet_person-image-cartoon-genshin_compound-models', 'lskhh/ty_cv_unet_person-image-cartoon-wz_compound-models']
image_names = ['sd-illustration', '3d', 'handdrawn', 'artstyle', 'sd-design', 'anime', 'sketch', 'genshin', 'wz'];

# 图像处理等操作
i = 0
works_num = 0
while i < len(models):
    pipe = pipeline(Tasks.image_portrait_stylization, model=models[i])

    result = pipe(source_image_path)

    utc_dt = datetime.datetime.utcnow()
    beijing_dt = utc_dt.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
    formatted = beijing_dt.strftime("%Y-%m-%d_%H-%M-%S.%f")
    result_path = works_path + '/' + image_names[i] + '_' + formatted + '.png'
    cv2.imwrite(result_path, result[OutputKeys.OUTPUT_IMG])
    works_num += 1
    i += 1

print(f'生成了{works_num}张作品')
