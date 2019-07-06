import os
import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu.
        filemenu = wx.Menu()
        
        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        menuOpen = filemenu.Append(wx.FD_OPEN,"&Open","Open a file")
        menuSave = filemenu.Append(wx.FD_SAVE,"&Save","Save a file")
        menuAbout = filemenu.Append(wx.ID_ABOUT,"&About","Information about this program")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit","Terminate the program")     

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        self.Show(True)

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)

        self.Show(True)

    def OnAbout(self,e):
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor",wx.OK)

        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self,e):
        self.Close(True)
        
    def OnOpen(self,e):
        """Open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*",wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def OnSave(self,e):
        """Save a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self, "Save file as", self.dirname, "", "*.*",wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'w')
            f.write(self.control.GetValue())
            f.close()
        dlg.Destroy()

app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()

