import wx
from tugas1Firra import MyFrame1

class PageFirra(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self.SetIcon(wx.Icon("DSCF1642.ico"))

app = wx.App() 
page = PageFirra(parent=None)
page.Show()
app.MainLoop()