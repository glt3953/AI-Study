import os
import openai
import requests
import shutil
from io import BytesIO
from PIL import Image

openai.api_key = os.getenv("OPENAI_API_KEY")
      
def paint(prompt):
    try:
        # Read the image file from disk and resize it
        source_image = Image.open("source.png")
        width, height = 1024, 1024
        source_image = source_image.resize((width, height))

        # Convert the image to a BytesIO object
        byte_stream = BytesIO()
        source_image.save(byte_stream, format='PNG')
        source_byte_array = byte_stream.getvalue()
        
        # Read the image file from disk and resize it
        mask_image = Image.open("mask.png")
        width, height = 1024, 1024
        mask_image = mask_image.resize((width, height))

        # Convert the image to a BytesIO object
        byte_stream = BytesIO()
        mask_image.save(byte_stream, format='PNG')
        mask_byte_array = byte_stream.getvalue()
        
        response = openai.Image.create_edit(
            image=source_byte_array,
            mask=mask_byte_array,
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
    except Exception as e:
        print(e)
        return e

    return response

print("请说出你想添加的事物，AI会自动生成图片并提供下载地址")

while True:
    user_input = input("> ")
    if user_input.lower() in ["bye", "goodbye", "exit"]:
        print("Goodbye!")
        break
    
    response = paint(user_input)
    
    print("生成的图片地址如下: \n%s" % response["data"][0]["url"])
    
    image = requests.get(response["data"][0]["url"], stream=True)  # 获取URL的响应，并启用流模式
    with open('image.png', 'wb') as out_file:  # 以二进制模式打开文件
        shutil.copyfileobj(image.raw, out_file)  # 将响应内容写入文件中
    del image  # 删除响应对象
