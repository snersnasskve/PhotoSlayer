import wx

class PSPanel(wx.Panel):
    
    def __init__(self, parent):
        super().__init__(parent)
        #   The purpose of a frame is to house UI elements
        file_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file_sizer.AddSpacer(15)

        file_sizer.Add(wx.StaticText(self, label='Root Folder:'), proportion=1, flag=wx.ALL, border=5)
        file_path = wx.TextCtrl(self)
        file_sizer.Add(file_path, proportion=3, flag=wx.ALL, border=5)
        browse_button = wx.Button(self, label='Browse')
        browse_button.Bind(wx.EVT_BUTTON, self.onBrowseClicked)
        file_sizer.Add(browse_button, proportion=1,
                       flag=wx.ALL, border=5)
        file_sizer.AddSpacer(15)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.AddSpacer(15)
        collect_button = wx.Button(self, label='Collect images')
        collect_button.Bind(wx.EVT_BUTTON, self.onCollectClicked)
        main_sizer.Add(file_sizer)
        main_sizer.Add(collect_button, 0, wx.ALL, 15)
        self.SetSizer(main_sizer)
        
    def onBrowseClicked(self, event):
        #
        print('You clicked Browse')

    def onCollectClicked(self, event):
        #
        print('You clicked Collect')

    def OnClose(self, e):
        super().Close(True)

class PSFrame(wx.Frame):
    # Init the class
    #   The purpose of a Frame is to house a Panel
    def __init__(self):
        super().__init__(None, title='Photo Slayer')
        panel = PSPanel(self)
        self.Show()
   
def main():
    # Create the main application window
    app = wx.App()
    # Instantiate the User Interface
    psFrame = PSFrame()

    # Start the processing behind the user interface
    app.MainLoop()

if __name__ == "__main__":
    main()