import wx
from traverseFiles import FileWalker

class MainPanel(wx.Panel):
    def __init__(self, parent):
        self.phBackgroundColour = (255, 243, 226)
        wx.Panel.__init__(self, parent, -1, style=wx.FULL_REPAINT_ON_RESIZE)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.img = wx.Image('background.jpg', wx.BITMAP_TYPE_JPEG)
        self.bckImageWidth, self.bckImageHeight = self.img.GetSize()
        self.SetBackgroundColour(self.phBackgroundColour)

               #   The purpose of a frame is to house UI elements
        file_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file_sizer.AddSpacer(15)

        #   Get a font to use
        #https://www.blog.pythonlibrary.org/2011/04/28/wxpython-learning-to-use-fonts/
        self.photoFont = wx.Font(13, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, 
                                   wx.FONTWEIGHT_MEDIUM)

        #Label text
        labelText = wx.StaticText(self, label='Root Folder:')
        labelText.SetFont(self.photoFont)
        file_sizer.Add(labelText, proportion=1, flag=wx.ALL, border=5)

        # File path editable text frame
        self.photoFolder = wx.TextCtrl(self)
        self.photoFolder.SetBackgroundColour(self.phBackgroundColour)
        self.photoFolder.SetFont(self.photoFont)
        file_sizer.Add(self.photoFolder, proportion=3, flag=wx.ALL, border=5)

        # Browse button
        browse_button = self.GetPhotoButton('Browse')
        browse_button.Bind(wx.EVT_BUTTON, self.onBrowseClicked)
        file_sizer.Add(browse_button, proportion=1,
                       flag=wx.ALL, border=5)
        file_sizer.AddSpacer(15)

        # All together
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.AddSpacer(15)

        # Collect button below
        collect_button = self.GetPhotoButton('Collect images')
        collect_button.Bind(wx.EVT_BUTTON, self.onCollectClicked)

        # All together
        main_sizer.Add(file_sizer)
        main_sizer.Add(collect_button, 0, wx.ALL, 15)
        self.SetSizer(main_sizer)
        self.call_me()      # NB: Dont put self in brackets

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

        
    def call_me(self) :
        self.photoFolder.SetValue('')
        
    def onBrowseClicked(self, event):
        #
        print('You clicked Browse')
        self.dir = event.GetString()
        dlg = wx.DirDialog (None, "Choose input directory", "",
                    wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            print('Selected files are: ', dlg.GetPath())
            self.photoFolder.SetValue(dlg.GetPath())
        dlg.Destroy()

    def onCollectClicked(self, event):
        #
        print('You clicked Collect')
        # # https://www.makeuseof.com/create-import-reuse-module-python/
        fileWalker = FileWalker()
   
        for fname in fileWalker.walkThroughFiles(self.photoFolder.GetValue()):
            print(fname)

    def OnClose(self, e):
        super().Close(True)

    def GetPhotoButton(self, buttonLabel):
        browse_button = wx.Button(self, label=buttonLabel)
        browse_button.SetBackgroundColour(self.phBackgroundColour)
        browse_button.SetFont(self.photoFont)
        return browse_button

class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, title='Scaling Image', size=(600,400))
        self.panel = MainPanel(self)
        self.panel.SetAutoLayout(1)
        self.Show()

if __name__ == "__main__":
    app = wx.App(0)
    frame = MainFrame(None)
    app.MainLoop()    