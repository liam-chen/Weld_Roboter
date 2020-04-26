
import math


class MainCalculate(object):

    def __init__(self,Ah,Vf,d,Vw,angle,t):
        """Ah:熔敷系数
            Vf:送丝速度
            d:焊丝的直径
            Vw:焊接速度
            angle:V型坡口夹角
            t:板厚
        """
        self.Ah=Ah
        self.Vf=Vf
        self.d=d
        self.Vw=Vw
        self.angle=angle
        self.t=t

    def getEachArea(self):
        """获取单道焊缝截面积"""
        result=(self.Ah*self.Vf*math.pi*self.d**2)/(4*self.Vw)
        return result

    def getTotalArea(self):
        """计算整个V型剖口总面积"""
        return self.t**2*math.tan(self.angle/2)

    def getTotalFloor(self):
        """计算总共的焊接层数,取偏大整数"""
        A=self.getTotalArea()
        As=self.getEachArea()
        r=(math.sqrt(1+8*A/As)-1)/2
        return  math.ceil(r)

    def getEachHeightsAndWeights(self):
        """计算各个焊层初始高度,返回两个list"""
        heights=[]
        weights=[]
        n=self.getTotalFloor()
        i=1
        while i<=n:
            As = self.getEachArea()
            hi=math.sqrt(i*(i+1)*As/2/math.tan(self.angle/2))
            heights.append(hi)
            wi=2*hi*math.tan(self.angle/2)
            weights.append(wi)
            i=i+1
        return heights,weights

    def getCoordinate(self):
        """获取每层每道焊缝坐标"""
        X=[[0]]
        Y=[[0]]
        Z=[[0]]
        n=self.getTotalFloor()
        hs,ws=self.getEachHeightsAndWeights()
        i = 2
        j=1
        while i <= n:
            xi=[]
            yi=[]
            zi=[]
            while j <= i:
                xij=j*ws[i-2]/(i+1)-ws[i-2]/2
                xi.append(xij)
                yi.append(0)
                zi.append(hs[i-2])
                j=j+1
            X.append(xi)
            Y.append(yi)
            Z.append(zi)
            i=i+1
            j=1
        return X,Y,Z
