# -*- coding:utf-8 -*-

from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
from simulation import Simulation
from weld_calculate import MainCalculate
from generate_code import Code
import math


class WeldGui:

    def __init__(self, master=None):
        '''初始化程序界面'''
        self.varcurrent = StringVar()
        self.varvoltage = StringVar()
        self.vspeed1 = StringVar()
        self.vspeed2 = StringVar()
        self.vdiameter = StringVar()
        self.vangle = StringVar()
        self.vjianxi = StringVar()
        self.vrongfulv = StringVar()
        self.vethicknessofslab = StringVar()
        self.vlengthofweld = StringVar()
        self.setToolBar(master)
        frame1 = Frame(master)
        self.setPanelSpecification(frame1)
        frame1.pack(fill=X)
        frame2 = Frame(master)
        self.setWeldParameter(frame2)
        frame2.pack(fill=X)


    def getParameter(self):
        '''获取参数,返回字典
            Ah:熔敷系数
            Vf:送丝速度
            d:焊丝的直径
            Vw:焊接速度
            angle:V型坡口夹角
            t:板厚
            l:焊缝长度
        '''
        return {
            'Ah':self.vrongfulv.get(),
            'Vf':self.vspeed2.get(),
            'd':self.vdiameter.get(),
            'Vw':self.vspeed1.get(),
            'angle':self.vangle.get(),
            't':self.vethicknessofslab.get(),
            'l':self.vlengthofweld.get()
        }

    def about(self):
        '''显示版权信息'''
        showinfo('关于软件','      本NB软件由可爱的陈一元、谭浩、王冲、王利'
                        '（排名按拼音：））组成的课设小组倾情制作。'
                        '严禁抄袭，一经发现,直接打死。')

    def printp(self):
        '''测试用例 打印获取的参数'''
        print(self.getParameter())

    def simulateSection(self):
        '''仿真模拟焊接截面效果'''
        try:
            map = self.getParameter()
            calculate = MainCalculate(
                float(map['Ah']),
                float(map['Vf']),
                float(map['d']),
                float(map['Vw']),
                float(map['angle'])*math.pi/180,
                float(map['t']))
            n = calculate.getTotalFloor()
            X, Y, Z = calculate.getCoordinate()
            simulation = Simulation(X,Y,Z,n,float(self.vlengthofweld.get()))
            simulation.simulateSection(
                math.pi*(float(self.vethicknessofslab.get())/n)**2,
                float(self.vangle.get())*math.pi/180,
                float(self.vethicknessofslab.get()))
        except BaseException:
            showerror("超级错误出现",'参数输入木有？？知道要输入什么参数吗？？？'
                               '那些框框是给你输入数字的？'
                               '懂？别**随便乱输！')


    def initSimulation(self):
        try:
            map = self.getParameter()
            calculate = MainCalculate(
                float(map['Ah']),
                float(map['Vf']),
                float(map['d']),
                float(map['Vw']),
                float(map['angle'])*math.pi/180,
                float(map['t']))
            n = calculate.getTotalFloor()
            X, Y, Z = calculate.getCoordinate()
            simulation = Simulation(X,Y,Z,n,float(self.vlengthofweld.get()))
            return simulation
        except BaseException:
            showerror("超级错误出现",'参数输入木有？？知道要输入什么参数吗？？？'
                               '那些框框是给你输入数字的？'
                               '懂？别**随便乱输！')


    def initCode(self):
        try:
            map = self.getParameter()
            calculate = MainCalculate(
                float(map['Ah']),
                float(map['Vf']),
                float(map['d']),
                float(map['Vw']),
                float(map['angle'])*math.pi/180,
                float(map['t']))
            n = calculate.getTotalFloor()
            X, Y, Z = calculate.getCoordinate()
            code = Code(X,Z,float(self.vlengthofweld.get()),n,float(self.vethicknessofslab.get()),float(self.vspeed1.get()))
            return code
        except BaseException:
            showerror("超级错误出现",'参数输入木有？？知道要输入什么参数吗？？？'
                               '那些框框是给你输入数字的？'
                               '懂？别**随便乱输！')

    def simulate(self):
        '''模拟仿真'''
        self.initSimulation().simulate()


    def code(self):
        '''生成ｒｏｂｏｔｓｔｕｄｉｏ可运行代码'''
        self.initCode().generatecode()

    def setToolBar(self,master=None):
        '''设置菜单按钮'''
        toolBar = Frame(master,height=25,bg='#8EA5EB')
        # button1 = Button(toolBar,text='工艺参数')
        button4 = Button(toolBar,text='截面仿真', command=self.simulateSection)
        button5 = Button(toolBar,text='生成代码', command=self.code)
        button2 = Button(toolBar,text='焊道仿真', command=self.simulate)
        button3 = Button(toolBar,text='关于',command=self.about)
        # button1.pack(padx=5,pady=6,side=LEFT)
        button4.pack(padx=5,pady=6,side=LEFT)
        button5.pack(padx=5,pady=6,side=LEFT)
        button2.pack(padx=5,pady=6,side=LEFT)
        button3.pack(padx=5,pady=6,side=LEFT)
        toolBar.pack(fill=X,expand=NO)

    def setPanelSpecification(self,master=None):
        '''设置板件规格参数界面'''
        panelSpecification = LabelFrame(master, text='板件规格', padx=5,pady=5)
        thicknessofslab = Label(panelSpecification, text='板厚（mm）')
        lengthofweld = Label(panelSpecification, text='焊缝长度(mm)')
        thicknessofslab.grid(row=0, column=0,sticky=W)
        lengthofweld.grid(row=0,column=2, sticky=W)

        ethicknessofslab = Entry(panelSpecification,width=15,textvariable=self.vethicknessofslab)
        elengthofweld = Entry(panelSpecification, width=15, textvariable=self.vlengthofweld)
        ethicknessofslab.grid(row=0,column=1)
        elengthofweld.grid(row=0,column=3)
        panelSpecification.pack(padx=10,pady=10,fill=X)

    def setWeldParameter(self, master=None):
        '''设置焊接工艺参数界面'''
        weldParameter = LabelFrame(master, text='焊接工艺', padx=5,pady=5)
        current = Label(weldParameter, text='焊接电流（A）')
        voltage = Label(weldParameter, text='焊接电压(V)')
        current.grid(row=0, column=0, sticky=W)
        voltage.grid(row=0, column=2, sticky=W)
        ecurrent = Entry(weldParameter, width=15, textvariable=self.varcurrent)
        evoltage = Entry(weldParameter, width=15, textvariable=self.varvoltage)
        ecurrent.grid(row=0, column=1)
        evoltage.grid(row=0, column=3)

        speed1 = Label(weldParameter, text='焊接速度(mm/s)')
        speed2 = Label(weldParameter, text='送丝速度(mm/s)')
        speed1.grid(row=1, column=0, sticky=W)
        speed2.grid(row=1, column=2, sticky=W)

        espeed1 = Entry(weldParameter, width=15, textvariable=self.vspeed1)
        espeed2 = Entry(weldParameter, width=15, textvariable=self.vspeed2)
        espeed1.grid(row=1, column=1)
        espeed2.grid(row=1, column=3)

        diameter = Label(weldParameter, text='焊丝直径(mm)')
        angle = Label(weldParameter, text='截面坡口角度(度)')
        diameter.grid(row=2, column=0, sticky=W)
        angle.grid(row=2, column=2, sticky=W)
        ediameter = Entry(weldParameter, width=15, textvariable=self.vdiameter)
        eangle = Entry(weldParameter, width=15, textvariable=self.vangle)
        ediameter.grid(row=2, column=1)
        eangle.grid(row=2, column=3)
        weldParameter.pack(padx=10, pady=10, fill=X)

        jianxi = Label(weldParameter, text='间隙(mm)')
        rongfulv = Label(weldParameter, text='熔敷系数')
        jianxi.grid(row=3, column=0, sticky=W)
        rongfulv.grid(row=3, column=2, sticky=W)

        ejianxi = Entry(weldParameter, width=15, textvariable=self.vjianxi)
        erongfulv = Entry(weldParameter, width=15, textvariable=self.vrongfulv)
        ejianxi.grid(row=3, column=1)
        erongfulv.grid(row=3, column=3)




if __name__ == '__main__':
    root = Tk()
    root.title('多层多道焊路径规划')
    root.resizable(0, 0)
    root.geometry('500x300+100+100')
    weldGui = WeldGui(root)
    root.mainloop()
