#pip install translate
from translate import Translator

# 初始化Translator对象,指定源语言和目标语言
translator = Translator(from_lang="zh", to_lang="en")

# 进行翻译,返回翻译结果
text = "虎虎生威!"
translation = translator.translate(text)
print(translation)
# 你好,世界!
# Hello, world!

# 也可以翻译整段文本
text = "苹果是一家美国跨国科技公司,专门从事消费电子产品、软件和在线服务。"
translation = translator.translate(text)
print(translation)
# 苹果是一家美国跨国科技公司,专门从事消费电子产品、软件和在线服务。
# Apple is an American multinational technology company that specializes in consumer electronics, software and online services.

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
