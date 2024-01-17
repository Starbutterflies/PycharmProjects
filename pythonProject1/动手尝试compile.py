import execjs
jstext = """
function hello(str){return str;}
"""
ctx = execjs.compile(jstext)
a = ctx.call("hello","helloworld")
print(a)