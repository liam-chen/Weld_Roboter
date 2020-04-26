# coding:utf-8
import datetime
from tkinter import *
from tkinter.messagebox import *

class Code:
    def __init__(self, Y, Z, l, n, t, v):
        '''Y:Y坐标数组，Ｚ坐标数组，ｌ焊缝长度，ｎ焊道层数, t板厚, v焊接速度'''
        self.Y = Y
        self.Z = Z
        self.l = l
        self.n = n
        self.t = t
        self.v = int(v)

    def generatecode(self):
        filename = datetime.datetime.now().strftime('%Hh%Mm%Ss')  + 'path.txt'
        f = open(filename, 'a')
        f.write('MODULE Module1\n')

        i = 0
        j = 1
        while i < self.n:
            for y, z in zip(self.Y[i], self.Z[i]):
                code = '\tCONST robtarget Target_' + \
                       str(j) + ':=[[' + str(-20) + ',' + str(y) + ',' \
                       + str(self.t*2) + '],[0,1,0,0],[0,0,2,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];\n'
                f.write(code)
                j += 1
                code = '\tCONST robtarget Target_' + \
                       str(j) + ':=[[' + str(-20) + ',' + str(y) + ',' \
                       + str(z) + '],[0,1,0,0],[0,0,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];\n'
                f.write(code)
                j += 1
                code = '\tCONST robtarget Target_' + \
                       str(j) + ':=[[' + str(self.l) + ',' + str(y) + ',' \
                       + str(z) + '],[0,1,0,0],[0,0,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];\n'
                f.write(code)
                j += 1
                code = '\tCONST robtarget Target_' + \
                       str(j) + ':=[[' + str(self.l) + ',' + str(y) + ',' \
                       + str(2*self.t) + '],[0,1,0,0],[0,0,1,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];\n'
                f.write(code)
                j += 1
            i += 1
        f.write('\tPROC Path_20()\n')
        i = 1
        while i < j:
            if i%4 == 0 or i%4 == 1:
                code = '\t\tMoveJ Target_'+str(i)+',v100,z100,MyTool\WObj:=Workobject_1;\n'
            else:
                code = '\t\tMoveL Target_'+str(i)+',v'+str(self.v)+',z0,MyTool\WObj:=Workobject_1;\n'
            f.write(code)
            i += 1
        f.write('\tENDPROC\n')
        f.write('ENDMODULE')
        f.close()
        showinfo('代码生成','代码生成完毕，请检查目录下相关文件')


if __name__ == '__main__':
    code = Code([[0],[0]],[[0],[10]],100,2,50)
    code.generatecode()
