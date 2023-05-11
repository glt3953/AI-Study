## 项目
https://github.com/microsoft/TaskMatrix
## 本地搭建
### clone the repo
git clone https://github.com/microsoft/TaskMatrix.git
### Go to directory
cd visual-chatgpt
### create a new environment
conda create -n visgpt python=3.8
### activate the new environment
conda activate visgpt
###  prepare the basic environments
pip install -r requirements.txt
pip install  git+https://github.com/IDEA-Research/GroundingDINO.git
pip install  git+https://github.com/facebookresearch/segment-anything.git
### prepare your private OpenAI key (for Linux)
export OPENAI_API_KEY={Your_Private_Openai_Key}
### prepare your private OpenAI key (for Windows)
set OPENAI_API_KEY={Your_Private_Openai_Key}
### Start TaskMatrix !
You can specify the GPU/CPU assignment by "--load", the parameter indicates which 
Visual Foundation Model to use and where it will be loaded to
The model and device are separated by underline '_', the different models are separated by comma ','
The available Visual Foundation Models can be found in the following table
For example, if you want to load ImageCaptioning to cpu and Text2Image to cuda:0
You can use: "ImageCaptioning_cpu,Text2Image_cuda:0"
### Advice for CPU Users
python visual_chatgpt.py --load ImageCaptioning_cpu,Text2Image_cpu
### Advice for 1 Tesla T4 15GB  (Google Colab)                       
python visual_chatgpt.py --load "ImageCaptioning_cuda:0,Text2Image_cuda:0"                    
### Advice for 4 Tesla V100 32GB                            
python visual_chatgpt.py --load "Text2Box_cuda:0,Segmenting_cuda:0,Inpainting_cuda:0,ImageCaptioning_cuda:0,Text2Image_cuda:1,Image2Canny_cpu,CannyText2Image_cuda:1,Image2Depth_cpu,DepthText2Image_cuda:1,VisualQuestionAnswering_cuda:2,InstructPix2Pix_cuda:2,Image2Scribble_cpu,ScribbleText2Image_cuda:2,SegText2Image_cuda:2,Image2Pose_cpu,PoseText2Image_cuda:2,Image2Hed_cpu,HedText2Image_cuda:3,Image2Normal_cpu,NormalText2Image_cuda:3,Image2Line_cpu,LineText2Image_cuda:3"
## 通过 Huggingface
https://huggingface.co/spaces/glt3953/visual_chatgpt
1. 只提供免费的CPU使用，需要将app.py中模型全部改为CPU模式
```
bot = ConversationBot({'Text2Box': 'cpu',
       'Segmenting': 'cpu',
       'Inpainting': 'cpu',
       'Text2Image': 'cpu',
       'ImageCaptioning': 'cpu',
       'VisualQuestionAnswering': 'cpu',
       'Image2Canny': 'cpu',
       'CannyText2Image': 'cpu',
       'InstructPix2Pix': 'cpu',
       'Image2Depth': 'cpu',
       'DepthText2Image': 'cpu',
       })
```
2.正常编译运行即可
## 通过 Colab
https://colab.research.google.com/drive/1fTO0Onix7TTk7C7KzjsxtzDX8nztMv2_#scrollTo=XBWXWPLZsHG2
1. 代码块
```
%pip install gitpython

import git
git.Repo.clone_from('https://github.com/glt3953/TaskMatrix.git', '/content/repo/gltTaskMatrix')

%cd /content/repo/gltTaskMatrix

%pip install -r requirements.txt
%pip install  git+https://github.com/IDEA-Research/GroundingDINO.git
%pip install  git+https://github.com/facebookresearch/segment-anything.git

%env OPENAI_API_KEY=""
!set OPENAI_API_KEY=""

!python visual_chatgpt.py --load "ImageCaptioning_cuda:0,Text2Image_cuda:0"
# !python visual_chatgpt.py --load ImageCaptioning_cpu,Text2Image_cpu
```
2. 访问colab的http://0.0.0.0:7860
```
ssh -L 7860:172.28.0.12:7860 -N -f -l glt3953@gmail.com colab.research.google.com

ssh -L 7860:内网IP:7860 -N -f -l 你的Colab用户名 colab.research.google.com
```