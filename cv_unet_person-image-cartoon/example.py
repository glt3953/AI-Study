import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

#原始图片
source_image_path = './drive/MyDrive/colab_data/examples/input3.png'

#img_cartoon = pipeline(Tasks.image_portrait_stylization, model='cvaisz/cartoon_njqx1')
#result = img_cartoon(img_path)

img_matting = pipeline(Tasks.portrait_matting, model='damo/cv_unet_image-matting')
result = img_matting(source_image_path)

cv2.imwrite('result.png', result[OutputKeys.OUTPUT_IMG])
print('finished!')
