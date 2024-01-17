import os
import execjs
import json

os.environ["NODE_PATH"] = r"C:\Users\61912\AppData\Roaming\npm\node_modules"
print(execjs.get().name)
from execjs import get
import os

runtime = get('Node')
# print(os.getcwd()+"\\node_modules")
# print(execjs.get().name)
#
# parser = execjs.compile("""
#     var wtf_wikipedia = require("wtf_wikipedia");
#     function parse(text) {
#         return wtf_wikipedia.parse(text);
#     }
# """)
# #
# if __name__ == "__main__":
#     obj = parser.call("parse", '<doc id=\'1\'></doc>')
#     print(obj)
e = execjs.eval("a = new Array(1,2,3)")
print(e)