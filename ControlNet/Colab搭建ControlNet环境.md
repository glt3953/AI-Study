# Colab搭建ControlNet环境
## Git地址
https://github.com/lllyasviel/ControlNet
https://github.com/camenduru/controlnet-colab
https://github.com/camenduru/stable-diffusion-webui-colab
## 扩展阅读
https://www.uisdc.com/stable-diffusion-2
## 相关网站
https://promptomania.com/
https://www.urania.ai/top-sd-artists
https://stableres.info/
https://civitai.com/
## Colab示例
https://colab.research.google.com/drive/12Uuq5Mz0vW68FHDKAmHmn2cs3vxQ0R4K#scrollTo=muwu2bF7q5eP
## 搭建流程
1. 安装Git环境
```
%pip install gitpython
```
2. 拉取代码并进入目录
```
import git

git.Repo.clone_from('https://github.com/lllyasviel/ControlNet.git', '/content/repo/ControlNet')

%cd /content/repo/ControlNet
```
3. 下载模型到models目录
```
!wget https://huggingface.co/lllyasviel/ControlNet/resolve/38a62cbf79862c1bac73405ec8dc46133aee3e36/models/control_sd15_mlsd.pth -P models/
#!mv control_sd15_mlsd.pth models/
#!pwd
!ls models
```
4. 安装依赖库
```
!pip install einops
!pip install transformers
!pip install open_clip_torch
!pip install gradio
!pip install pytorch-lightning==1.7.7
!pip install omegaconf
!pip install basicsr
```
5. 使用 ngrok 映射到Colab端口（此设置大多数情况下报错，直接跳过）
```
!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
!unzip ngrok-stable-linux-amd64.zip
#获取token https://dashboard.ngrok.com/get-started/your-authtoken
#验证token
!./ngrok authtoken 2PuPonHwFQpdeht3WZFgMlQDRuw_2YkcaMrbuG5pjg9jTzkT5
#开启ngrok service，绑定port(这里指定7860)
!get_ipython().system_raw('./ngrok http 7860 &')
! curl -s http://localhost:4040/api/tunnels | python3 -c "import sys, json; print(json.load(sys.stdin)['tunnels'][0]['public_url'])"
```
6. 使用 ngrok 映射到Colab端口运行代码
```
!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
!unzip ngrok-stable-linux-amd64.zip
#获取token https://dashboard.ngrok.com/get-started/your-authtoken
#验证token
!./ngrok authtoken 2PuPonHwFQpdeht3WZFgMlQDRuw_2YkcaMrbuG5pjg9jTzkT5
import subprocess
ngrok_process = subprocess.Popen('./ngrok http 7860', shell=True)  

!python gradio_hough2image.py
```
映射的地址在https://dashboard.ngrok.com/tunnels/agents 中查询