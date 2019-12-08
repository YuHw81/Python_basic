for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)


for n in ['body', 'foo', 'bar']:
    print(n)


a = ['body', 'foo', 'bar']
for i in range(0, len(a)):
    print(i, a[i])


print(eval('1 + 2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))


exec("name = '홍길동'")
print(name)


def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))


def callbackTest(x):
    print(x)

def callback(fn, l):
    for i in l:
        fn(i)

callback(callbackTest, [1, 2, 3])        
