#coding=utf-8
#�����ǽ��ļ�������������Ϊutf-8��
#����ʽ������ӣ�

def testit(fun, *Tuple, **Dict):
    try:
            resualt = fun(*Tuple, **Dict)       #��fun��intʱ���ȼ���int(*Tuple, **Dict)���Դ�����
            return (True, resualt)
    except Exception, diag:
            return (False, diag)

def test():
    funcs = (int, long, float)               #funcs Ԫ���ֵ�Ƕ�int��long��float�������������á�
    vals = (1234, 12.34, '1234', '12.34')

    for eachfun in funcs:
            print '__' * 20
            for eachval in vals:
                retval = testit(eachfun, eachval)

                if retval[0]:
                    print '%s(%s)= ' % (eachfun, eachval), retval[1]           #���쳣�����ת�����ֵ
                else:   
                    print '%s(%s)= False:' %  (eachfun, eachval), retval[1]    #����쳣��Ϣ
                
if __name__ == "__main__":
    test()

