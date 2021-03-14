# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Selamat Datang!!!", pos = wx.DefaultPosition, size = wx.Size( 898,760 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		self.m_menubar4 = wx.MenuBar( 0 )
		self.m_menubar4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_menubar4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_menubar4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		self.m_menu14 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu14, wx.ID_ANY, u"Biodata", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuItem3.SetBitmap( wx.NullBitmap )
		self.m_menu14.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.m_menu14, wx.ID_ANY, u"Kartu Tanda Mahasiswa", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu14.Append( self.m_menuItem4 )

		self.m_menuItem5 = wx.MenuItem( self.m_menu14, wx.ID_ANY, u"Telegram", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu14.Append( self.m_menuItem5 )

		self.m_menuItem6 = wx.MenuItem( self.m_menu14, wx.ID_ANY, u"Student Plan", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu14.Append( self.m_menuItem6 )

		self.m_menuItem7 = wx.MenuItem( self.m_menu14, wx.ID_ANY, u"Login SFS", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu14.Append( self.m_menuItem7 )

		self.m_menuItem8 = wx.MenuItem( self.m_menu14, wx.ID_ANY, u"Ormawa", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu14.Append( self.m_menuItem8 )

		self.m_menubar4.Append( self.m_menu14, u"Profil" )

		self.m_menu16 = wx.Menu()
		self.m_menuItem14 = wx.MenuItem( self.m_menu16, wx.ID_ANY, u"Jadwal Hari Ini", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu16.Append( self.m_menuItem14 )

		self.m_menuItem15 = wx.MenuItem( self.m_menu16, wx.ID_ANY, u"Kuesioner", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu16.Append( self.m_menuItem15 )

		self.m_menuItem16 = wx.MenuItem( self.m_menu16, wx.ID_ANY, u"Grafik IP", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu16.Append( self.m_menuItem16 )

		self.m_menuItem17 = wx.MenuItem( self.m_menu16, wx.ID_ANY, u"Cetak Tagihan", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu16.Append( self.m_menuItem17 )

		self.m_menuItem18 = wx.MenuItem( self.m_menu16, wx.ID_ANY, u"Status Kuliah", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu16.Append( self.m_menuItem18 )

		self.m_menuItem19 = wx.MenuItem( self.m_menu16, wx.ID_ANY, u"KRS", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu16.Append( self.m_menuItem19 )

		self.m_menuItem20 = wx.MenuItem( self.m_menu16, wx.ID_ANY, u"Hasil Studi", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu16.Append( self.m_menuItem20 )

		self.m_menubar4.Append( self.m_menu16, u"Akademik" )

		self.m_menu17 = wx.Menu()
		self.m_menuItem21 = wx.MenuItem( self.m_menu17, wx.ID_ANY, u"Event Universitas", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu17.Append( self.m_menuItem21 )

		self.m_menuItem22 = wx.MenuItem( self.m_menu17, wx.ID_ANY, u"Event Ormawa", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu17.Append( self.m_menuItem22 )

		self.m_menuItem23 = wx.MenuItem( self.m_menu17, wx.ID_ANY, u"Event E-Voting", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu17.Append( self.m_menuItem23 )

		self.m_menubar4.Append( self.m_menu17, u"Even" )

		self.m_menu18 = wx.Menu()
		self.m_menuItem24 = wx.MenuItem( self.m_menu18, wx.ID_ANY, u"E-learning", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu18.Append( self.m_menuItem24 )

		self.m_menuItem26 = wx.MenuItem( self.m_menu18, wx.ID_ANY, u"Kawanda", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu18.Append( self.m_menuItem26 )

		self.m_menuItem27 = wx.MenuItem( self.m_menu18, wx.ID_ANY, u"Blog", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu18.Append( self.m_menuItem27 )

		self.m_menuItem28 = wx.MenuItem( self.m_menu18, wx.ID_ANY, u"UC3", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu18.Append( self.m_menuItem28 )

		self.m_menuItem25 = wx.MenuItem( self.m_menu18, wx.ID_ANY, u"ShortURL", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu18.Append( self.m_menuItem25 )

		self.m_menubar4.Append( self.m_menu18, u"Web dan Personal" )

		self.m_menu19 = wx.Menu()
		self.m_menubar4.Append( self.m_menu19, u"Logout" )

		self.SetMenuBar( self.m_menubar4 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,650 ), wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		tempatJudul = wx.BoxSizer( wx.VERTICAL )

		self.judul = wx.StaticText( self.m_panel1, wx.ID_ANY, u"\"HELLO WX\"", wx.DefaultPosition, wx.Size( 600,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.judul.Wrap( -1 )

		self.judul.SetFont( wx.Font( 40, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Georgia" ) )
		self.judul.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		tempatJudul.Add( self.judul, 0, wx.ALL, 5 )

		tempatIdentitas = wx.FlexGridSizer( 0, 2, 0, 0 )
		tempatIdentitas.SetFlexibleDirection( wx.BOTH )
		tempatIdentitas.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.nama = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Nama", wx.Point( -1,-1 ), wx.Size( 200,-1 ), 0 )
		self.nama.Wrap( -1 )

		self.nama.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Georgia" ) )
		self.nama.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		tempatIdentitas.Add( self.nama, 0, wx.ALL, 5 )

		self.firra = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Firra Andriani", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.firra.Wrap( -1 )

		self.firra.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Georgia" ) )
		self.firra.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		tempatIdentitas.Add( self.firra, 0, wx.ALL, 5 )

		self.nim = wx.StaticText( self.m_panel1, wx.ID_ANY, u"NIM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nim.Wrap( -1 )

		self.nim.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Georgia" ) )
		self.nim.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		tempatIdentitas.Add( self.nim, 0, wx.ALL, 5 )

		self.nimFirra = wx.StaticText( self.m_panel1, wx.ID_ANY, u"192410101028", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nimFirra.Wrap( -1 )

		self.nimFirra.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Georgia" ) )
		self.nimFirra.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		tempatIdentitas.Add( self.nimFirra, 0, wx.ALL, 5 )

		self.nama1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Kelas", wx.Point( -1,-1 ), wx.Size( 200,-1 ), 0 )
		self.nama1.Wrap( -1 )

		self.nama1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Georgia" ) )
		self.nama1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		tempatIdentitas.Add( self.nama1, 0, wx.ALL, 5 )

		self.nama2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"PBO 2 C", wx.Point( -1,-1 ), wx.Size( 200,-1 ), 0 )
		self.nama2.Wrap( -1 )

		self.nama2.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Georgia" ) )
		self.nama2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		tempatIdentitas.Add( self.nama2, 0, wx.ALL, 5 )

		self.nama3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Prodi", wx.Point( -1,-1 ), wx.Size( 200,-1 ), 0 )
		self.nama3.Wrap( -1 )

		self.nama3.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Georgia" ) )
		self.nama3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		tempatIdentitas.Add( self.nama3, 0, wx.ALL, 5 )

		self.nama4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Sistem Informasi", wx.Point( -1,-1 ), wx.Size( 320,-1 ), 0 )
		self.nama4.Wrap( -1 )

		self.nama4.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Georgia" ) )
		self.nama4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		tempatIdentitas.Add( self.nama4, 0, wx.ALL, 5 )

		self.nama31 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Fakultas", wx.Point( -1,-1 ), wx.Size( 200,-1 ), 0 )
		self.nama31.Wrap( -1 )

		self.nama31.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Georgia" ) )
		self.nama31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		tempatIdentitas.Add( self.nama31, 0, wx.ALL, 5 )

		self.nama21 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Fasilkom", wx.Point( -1,-1 ), wx.Size( 200,-1 ), 0 )
		self.nama21.Wrap( -1 )

		self.nama21.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Georgia" ) )
		self.nama21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		tempatIdentitas.Add( self.nama21, 0, wx.ALL, 5 )


		tempatJudul.Add( tempatIdentitas, 1, wx.EXPAND, 5 )

		self.m_animCtrl2 = wx.adv.AnimationCtrl( self.m_panel1, wx.ID_ANY, wx.adv.NullAnimation, wx.DefaultPosition, wx.Size( 500,370 ), wx.adv.AC_DEFAULT_STYLE )
		self.m_animCtrl2.LoadFile( u"D:\\Kuliah\\Semester 4\\Pemrograman Berorientasi Obyek 2\\Tugas\\396d8cf19235b7b437d1067045a63b5a (1).gif" )
		tempatJudul.Add( self.m_animCtrl2, 0, wx.ALL, 5 )


		bSizer16.Add( tempatJudul, 1, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer16 )
		self.m_panel1.Layout()
		bSizer15.Add( self.m_panel1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


