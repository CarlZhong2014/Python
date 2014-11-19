#coding=utf-8
#上述是将文件编码事先申明为utf-8。
#函数式编程例子：

def testit(fun, *Tuple, **Dict):
    try:
            resualt = fun(*Tuple, **Dict)       #当fun是int时，等价于int(*Tuple, **Dict)，以此类推
            return (True, resualt)
    except Exception, diag:
            return (False, diag)

def test():
    funcs = (int, long, float)               #funcs 元组的值是对int，long，float三个函数的引用。
    vals = (1234, 12.34, '1234', '12.34')

    for eachfun in funcs:
            print '__' * 20
            for eachval in vals:
                retval = testit(eachfun, eachval)

                if retval[0]:
                    print '%s(%s)= ' % (eachfun, eachval), retval[1]           #无异常就输出转换后的值
                else:   
                    print '%s(%s)= False:' %  (eachfun, eachval), retval[1]    #输出异常信息
                
if __name__ == "__main__":
    test()

