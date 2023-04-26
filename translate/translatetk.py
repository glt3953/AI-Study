#from translatetk import Translator
#
## 初始化Translator对象,指定源语言和目标语言
#translator = Translator("en", "zh")
#
## 进行翻译,返回翻译结果
#translation = translator.translate("Hello, world!")
#print(translation)
## 你好,世界!
#
## 也可以翻译整段文本
#text = "Apple is an American multinational technology company that specializes in consumer electronics, software and online services."
#translation = translator.translate(text)
#print(translation)
## 苹果是一家美国跨国科技公司,专门从事消费电子产品、软件和在线服务。

from translate import Translator

translator= Translator(to_lang="zh")
translation = translator.translate("Hello, world!")
print(translation)
# 你好,世界!

text = "Apple is an American multinational technology company."
translation = translator.translate(text)
print(translation)
# 苹果是一家美国跨国科技公司。
