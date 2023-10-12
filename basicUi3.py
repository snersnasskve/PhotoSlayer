import wx

app = wx.App()
frame = wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0,0,640,480)
frame.Show()
app.MainLoop()