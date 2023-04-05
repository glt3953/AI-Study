import os
import openai
import requests
import shutil

openai.api_key = os.getenv("OPENAI_API_KEY")
      
def paint():
    try:
        #惊蛰万物苏醒，清明踏青，秋分桂花飘香，大寒赏雪。
        #晴方好，雨亦奇，来几日，见彩霏。花遮著，人掩扉，但自知，春色在。
        #三月春归，草长莺飞。伴着疫情的寒冬远去，一个崭新的春天正在走近。和春天一起回归的，还有林野间的绚烂山桃花海。
        #落花人独立，微雨燕双飞。
        response = openai.Image.create_variation(
            image=open("motorbike.png", "rb"),
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
