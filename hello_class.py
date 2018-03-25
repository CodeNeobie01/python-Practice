# _*_ codeing : utf-8 _*_
# 面向对象的练习
class SayHello:
    def __init__(self, name):
        self._name = name
    def sayOut(self):
        print ("Hello python {0}".format(self._name))

W = SayHello("World")
W.sayOut