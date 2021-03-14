import wx
from tugas1Firra import MyFrame1

class PageFirra(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)

app = wx.App() 
page = PageFirra(parent=None)
page.Show()
app.MainLoop()