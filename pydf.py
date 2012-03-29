import wx
import diskFree

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(600,400))
		self.CreateStatusBar()
		# Setting up the menu
		filemenu = wx.Menu()
		
		# Filemenu:
		menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", " Termenita the program")

		# Creating the menubar.
		menuBar = wx.MenuBar()
		# Add the items to the menu:
		menuBar.Append(filemenu, "&File")
		self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
		self.Show(True)

	def OnExit (self, e):
		""" Exits the program """
		dlg = wx.MessageDialog(self, "Do you realy want to quit?", "Confirm Exit", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
		result = dlg.ShowModal()
		dlg.Destroy()
		if result == wx.ID_OK:
			self.Close(True)  # Close the frame

app= wx.App(False)
frame = MainWindow(None, "PyDF")
app.MainLoop()