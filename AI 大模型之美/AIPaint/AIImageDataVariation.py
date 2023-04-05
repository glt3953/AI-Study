import os
import openai
import requests
import shutil
from io import BytesIO
from PIL import Image

openai.api_key = os.getenv("OPENAI_API_KEY")
      
def paint():
    try:
        # Read the image file from disk and resize it
        image = Image.open("messi 3d character cartoon disney pixar render.jpg")
        width, height = 1024, 1024
        image = image.resize((width, height))

        # Convert the image to a BytesIO object
        byte_stream = BytesIO()
        image.save(byte_stream, format='PNG')
        byte_array = byte_stream.getvalue()
        
        response = openai.Image.create_variation(
            image=byte_array,
            n=1,
            size="1024x1024"
        )
    except Exception as e:
        print(e)
        return e

    return response

print("AI会自动变换当前图片并提供下载地址")

response = paint()
    
print("生成的图片地址如下: \n%s" % response["data"][0]["url"])

image = requests.get(response["data"][0]["url"], stream=True)  # 获取URL的响应，并启用流模式
with open('image.png', 'wb') as out_file:  # 以二进制模式打开文件
    shutil.copyfileobj(image.raw, out_file)  # 将响应内容写入文件中
del image  # 删除响应对象
