# -*- coding: utf-8 -*- 

def test(num_1,num_2,operation):

    if operation == 1:
        print "�����Z�J�n"
        print num_1 + num_2

    elif operation == 2:
        print "�����Z�J�n"
        print num_1 - num_2

    elif operation == 3:
        print "�|���Z�J�n"
        print num_1 * num_2

    elif operation == 4:
        print "����Z�J�n"
        print num_1 / num_2

    else:
        print "�s���ȃI�y���[�V�����w��ł���"
        

if __name__ == "__main__":
    test(100,10,4)
