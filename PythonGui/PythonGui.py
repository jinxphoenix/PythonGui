
import wx

class MyFrame(wx.Frame):
    """ We derive a new class from frame"""
    def __init__(self, parent, title):
        wx.Frame.__init__(self,parent,title=title,size=(200,100))
        self.control = wx.TextCtrl(self,style=wx.TE_MULTiLINE)
        self.Show(True)

app = wx.App(False)