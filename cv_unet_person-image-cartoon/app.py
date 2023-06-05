#pip install "modelscope[cv]" -f https://modelscope.oss-cn-beijing.aliyuncs.com/releases/repo.html
#pip install gradio

import gradio as gr
from PIL import Image
import base64
import os
import datetime
import imageio
import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from tqdm import tqdm
import numpy as np
from skimage import io

@staticmethod
def encode_image(image):
    _bytes = io.BytesIO()
    image.save(_bytes, format="PNG")
    b64 = base64.b64encode(_bytes.getvalue())
    return b64.decode("utf-8")

@staticmethod
def decode_image(raw_image):
    if not is_vision_available():
        raise ImportError(
            "This tool returned an image but Pillow is not installed. Please install it (`pip install Pillow`)."
        )

    from PIL import Image

    b64 = base64.b64decode(raw_image)
    _bytes = io.BytesIO(b64)
    return Image.open(_bytes)

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
#创建用户上传图片存放目录
user_upload_path = './drive/MyDrive/colab_data/user_upload/' + formatted
if not os.path.exists(user_upload_path):
  os.makedirs(user_upload_path)
print('用户图片目录：' + user_upload_path)

name_dict = {"日漫风":"anime", "3D风":"3d", "手绘风":"handdrawn", "国漫风":"sd-illustration", "插画风":"sd-design", "原神风":"genshin", "王者荣耀风":"wz"}
style_dict = {"日漫风":"damo/cv_unet_person-image-cartoon_compound-models", "3D风":"damo/cv_unet_person-image-cartoon-3d_compound-models", "手绘风":"damo/cv_unet_person-image-cartoon-handdrawn_compound-models", "国漫风":"damo/cv_unet_person-image-cartoon-sd-illustration_compound-models", "插画风":"damo/cv_unet_person-image-cartoon-sd-design_compound-models", "原神风":"lskhh/moran-cv_unet_person-image-cartoon-genshin_compound-models", "王者荣耀风":"lskhh/ty_cv_unet_person-image-cartoon-wz_compound-models"}

# def get_size(h, w, max = 720):
#     if min(h, w) > max:
#         if h > w:
#             h, w = int(max * h / w), max
#         else:
#             h, w = max, int(max * w / h)
#     return h, w

def inference(image: Image, style: str) -> Image:
  utc_dt = datetime.datetime.utcnow()
  beijing_dt = utc_dt.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
  formatted = beijing_dt.strftime("%Y-%m-%d_%H:%M:%S.%f")
  image_path = user_upload_path + '/' + formatted + '.png'
  print('用户图片：' + image_path)
  image.save(image_path)

  pipe = pipeline(Tasks.image_portrait_stylization, model=style_dict[style])
  result = pipe(image_path)

  utc_dt = datetime.datetime.utcnow()
  beijing_dt = utc_dt.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
  formatted = beijing_dt.strftime("%Y-%m-%d_%H:%M:%S.%f")
  result_path = works_path + '/' + name_dict[style] + '_' + formatted + '.png'
  cv2.imwrite(result_path, result[OutputKeys.OUTPUT_IMG])

  res_img = Image.open(result_path)
  print('作品：' + result_path)

  return res_img


css_style = "#fixed_size_img {height: 240px;} "


title = "AI人像漫画 by宁侠"
# description = "输入一张人像照片,并指定希望的风格（如：日漫风、3D风、手绘风、素描风、艺术效果），内置多种风格模型用于生成对应的转换结果。本页面提供了在线体验的服务，欢迎使用！"
description = '''
街拍，人像，团建照片...随意上传您心仪的照片（尽量是正面近景人像照片），选择对应风格(日漫风，3D风，手绘风等等)，一键即可转换为不同风格的卡通化图片！多风格的人像模型已经内置好，点点鼠标就可以抢占朋友圈的C位，立刻玩起来吧
'''
examples_path = './drive/MyDrive/colab_data/examples/'
examples = [[examples_path + 'input1.png'], [examples_path + 'input2.png'], [examples_path + 'input3.png'], [examples_path + 'input4.png']]
# examples = [[os.path.dirname(__file__) + './images/input1.png'], [os.path.dirname(__file__) + './images/input2.png'], [os.path.dirname(__file__) + './images/input3.png'], [os.path.dirname(__file__) + './images/input4.png']]
# examples = [[os.path.dirname(__file__) + '/images/input1.png'], [os.path.dirname(__file__) + '/images/input2.png'], [os.path.dirname(__file__) + '/images/input3.png']]

with gr.Blocks(title=title, css=css_style) as demo:
    
    gr.HTML('''
      <div style="text-align: center; max-width: 720px; margin: 0 auto;">
                  <div
                    style="
                      display: inline-flex;
                      align-items: center;
                      gap: 0.8rem;
                      font-size: 1.75rem;
                    "
                  >
                    <h1 style="font-family: PingFangSC; font-weight: 500; line-height: 1.5em; font-size: 32px; margin-bottom: 7px;">
                      AI人像漫画 by宁侠
                    </h1>
                  </div>
                  <img id="overview" alt="overview" src="https://modelscope.oss-cn-beijing.aliyuncs.com/demo/image-cartoon/demo_sin1.gif" />
                  
                </div>
      ''')


    gr.Markdown(description)
    with gr.Row():
        radio_style = gr.Radio(label="风格选择", choices=["日漫风", "3D风", "手绘风", "国漫风", "插画风", "原神风", "王者荣耀风"], value="日漫风")
    with gr.Row():
        img_input = gr.Image(type="pil", elem_id="fixed_size_img")
        img_output = gr.Image(type="pil", elem_id="fixed_size_img")
    with gr.Row():
        btn_submit = gr.Button(value="一键生成", elem_id="blue_btn")
        # btn_clear = gr.Button(value="清除")

    examples = gr.Examples(examples=examples, inputs=[img_input], outputs=img_output)
    btn_submit.click(inference, inputs=[img_input, radio_style], outputs=img_output)
    # btn_clear清除画布

demo.launch(debug=True)
