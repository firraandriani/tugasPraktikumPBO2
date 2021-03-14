# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 975,592 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 800,650 ), wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		tempatJudul = wx.BoxSizer( wx.VERTICAL )

		self.judul = wx.StaticText( self.m_panel1, wx.ID_ANY, u"\"HELLO WX\"", wx.DefaultPosition, wx.Size( 600,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.judul.Wrap( -1 )

		self.judul.SetFont( wx.Font( 40, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Georgia" ) )
		self.judul.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		tempatJudul.Add( self.judul, 0, wx.ALL, 5 )

		tempatIdentitas = wx.FlexGridSizer( 0, 2, 0, 0 )
		tempatIdentitas.SetFlexibleDirection( wx.BOTH )
		tempatIdentitas.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.nama = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Nama", wx.Point( -1,-1 ), wx.Size( 200,-1 ), 0 )
		self.nama.Wrap( -1 )

		self.nama.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Georgia" ) )

		tempatIdentitas.Add( self.nama, 0, wx.ALL, 5 )

		self.firra = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Firra Andriani", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.firra.Wrap( -1 )

		self.firra.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Georgia" ) )

		tempatIdentitas.Add( self.firra, 0, wx.ALL, 5 )

		self.nim = wx.StaticText( self.m_panel1, wx.ID_ANY, u"NIM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nim.Wrap( -1 )

		self.nim.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Georgia" ) )

		tempatIdentitas.Add( self.nim, 0, wx.ALL, 5 )

		self.nimFirra = wx.StaticText( self.m_panel1, wx.ID_ANY, u"192410101028", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nimFirra.Wrap( -1 )

		self.nimFirra.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Georgia" ) )

		tempatIdentitas.Add( self.nimFirra, 0, wx.ALL, 5 )


		tempatJudul.Add( tempatIdentitas, 1, wx.EXPAND, 5 )


		fgSizer2.Add( tempatJudul, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( fgSizer2 )
		self.m_panel1.Layout()
		bSizer1.Add( self.m_panel1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


