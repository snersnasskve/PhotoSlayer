import wx

class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.FULL_REPAINT_ON_RESIZE)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.img = wx.Image('background.jpg', wx.BITMAP_TYPE_JPEG)
        self.bckImageWidth, self.bckImageHeight = self.img.GetSize()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.Clear()
        width,height = self.GetSize()
        posx,posy = 0, 0

        # Use this code to maintain aspect ratio
        # newheight = int(float(width)/self.bckImageWidth*self.bckImageHeight)
        # if newheight < height:
        #     posy = int((height - newheight) / 2) 
        #     height = newheight
        # else:
        #     newwidth = int(float(height)/self.bckImageHeight*self.bckImageWidth)
        #     posx = int((width - newwidth) / 2)
        #     width = newwidth        

        img = self.img.Scale(width,height, wx.IMAGE_QUALITY_HIGH)
        self.bmp = wx.Bitmap(img)
        dc.DrawBitmap(self.bmp,posx,posy)

class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, title='Scaling Image', size=(600,400))
        self.panel = MainPanel(self)
        self.Show()

app = wx.App(0)
frame = MainFrame(None)
app.MainLoop()    