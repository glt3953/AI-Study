import torch

# 载入模型
model = torch.load("xn--fiq599j.pt")

# 翻译一句话
input = "我的名字是小明。"
output = model.translate(input)
print(output)
# My name is Xiaoming.

# 翻译文件
with open('./data/test.txt') as f:
    inputs = f.readlines()
outputs = model.translate(inputs)

with open('./data/OpenNMT.txt', 'w') as f:
    f.write(outputs)
