#pip install translate
from translate import Translator

# 初始化Translator对象,指定源语言和目标语言
translator = Translator(from_lang="zh", to_lang="en")

# 进行翻译,返回翻译结果
text = "心有猛虎，细嗅蔷薇!"
translation = translator.translate(text)
print(translation)
# 你好,世界!
# Hello, world!

# 也可以翻译整段文本
text = "那是一九七五年二三月间，一个平平常常的日子，细蒙蒙的雨丝夹着一星半点的雪花，正纷纷淋淋地向大地飘洒着。时令已经快到惊蛰，雪当然再也不会存留，往往还没等落地，就已经消失得无踪无影了。黄土高原严寒而漫长的冬天看来就要过去，但那真正温暖的春天还远远没有到来。"
translation = translator.translate(text)
print(translation)
# 苹果是一家美国跨国科技公司,专门从事消费电子产品、软件和在线服务。
# Apple is an American multinational technology company that specializes in consumer electronics, software and online services.
# It was in February and March 1975, on an ordinary day, the thin raindrops of rain sandwiched between a star and a half of snow, and they were watered to the earth. The time is fast approaching, of course, the snow will never remain, often before the landing, it has disappeared without a trace. The cold and long winter of the Loess Plateau seemed to be passing, but the truly warm spring was far from over.

#from translate import Translator
#
##translator = Translator(to_lang="en")
#translator = Translator("zh", "en")
#translation = translator.translate("你好,世界!")
#print(translation)
# 你好,世界!
# Hello, world!

#text = "苹果是一家美国跨国科技公司。"
#translation = translator.translate(text)
#print(translation)
# 苹果是一家美国跨国科技公司。
# Apple is an American multinational technology company.
