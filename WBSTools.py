#!/usr/bin/env python
# -*- coding: utf-8 -*-

# If this is a web application, set the remote host here
remotehost = ""

import sys
import traceback
import time
import tempfile
import os
import wx
import dabo.ui
from dabo.dLocalize import _
# The loading of the UI needs to happen before the importing of the
# db, biz, and ui packages:
dabo.ui.loadUI("wx")
print sys.platform
if sys.platform[:3] == "win":
	dabo.MDI = True

if sys.platform == "darwin":
	print "running on OSX"
	dabo.MDI = True
	# hack for locale error on OSX
	import locale
	print "imported locale"
	print locale.getdefaultlocale()
	locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
	print "locale.setlocale successful"
	print locale.getdefaultlocale()
import db
import biz
import ui
import reports
import sys
import time

# included for PyInstaller
import wx.gizmos, wx.lib.calendar 

from App import App
app = App(SourceURL=remotehost)
app.db = db
app.biz = biz
app.ui = ui
app.reports = reports

# Make it easy to find any images or other files you put in the resources
# directory.
sys.path.append(os.path.join(app.HomeDirectory, "resources"))

app.setup()

app.getTempDir()
print "TempDir = " + str(app.TempDir) + " " + str(type(app.TempDir))
if not app.testTempDir:
	app.getTempDir()
app.MainFormClass = app.ui.FrmMain
app.PreferenceManager.setValue("fontsize", 11)
app.NoneDisplay = ""
# Set up a global connection to the database that all bizobjs will share:
try:
	app.dbConnectionName = "wbs_monro_user"
	app.dbConnection = app.getConnectionByName(app.dbConnectionName)
except:
	dabo.ui.exclaim("Error connecting to database, please check the network before trying again!" + str(traceback.format_exc()))
	time.sleep(5)
	
	sys.exit(1)
#app.dbConnection.LogEvents = ['All']


# Open one or more of the defined forms. A default one was picked by the app
# generator, but you can change that here. Additionally, if form names were
# passed on the command line, they will be opened instead of the default one
# as long as they exist.
if sys.platform == "darwin":
	print "running on OSX"
	dabo.MDI = True
	# hack for locale error on OSX
	import locale
	print "imported locale"
	print locale.getdefaultlocale()
	locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
	print "locale.setlocale successful"
	print locale.getdefaultlocale()

app.ui.AnswersForm = dabo.ui.createClass("ui" + os.sep + "AnswersForm.cdxml")
app.ui.AttachmentsForm = dabo.ui.createClass("ui" + os.sep + "AttachmentsForm.cdxml")
app.ui.CommentsForm = dabo.ui.createClass("ui" + os.sep + "CommentsForm.cdxml")
app.ui.ContactsForm = dabo.ui.createClass("ui" + os.sep + "ContactsForm.cdxml")
app.ui.FileTypeSelector = dabo.ui.createClass("ui" + os.sep + "FileTypeSelector.cdxml")
app.ui.GetFilesForContactForm = dabo.ui.createClass("ui" + os.sep + "GetFilesForContactForm.cdxml")
app.ui.GradesForm = dabo.ui.createClass("ui" + os.sep + "GradesForm.cdxml")
app.ui.LessonsForm = dabo.ui.createClass("ui" + os.sep + "LessonsForm.cdxml")
app.ui.StudentsForm = dabo.ui.createClass("ui" + os.sep + "StudentsForm.cdxml")
app.ui.TeachersForm = dabo.ui.createClass("ui" + os.sep + "TeachersForm.cdxml")
app.ui.PrintOrPreviewForm = dabo.ui.createClass("ui" + os.sep + "PrintOrPreviewForm.cdxml")
app.ui.LessonSelector = dabo.ui.createClass("ui" + os.sep + "LessonSelector.cdxml")
app.ui.CommentSelectorForm = dabo.ui.createClass("ui" + os.sep + "CommentSelectorForm.cdxml")
app.DefaultForm = app.ui.StudentsForm
app.FormsToOpen = [app.DefaultForm]
app.startupForms()
if app.MainForm != None:
	userName = str(app.dbConnectionName).upper()
	app.MainForm.Caption = 'WBSTools version ' + str(app.getAppInfo('appVersion') + ' user = ' + userName)
	app.MainForm.Icon = "icons/wbs.ico"
# Start the application event loop:
app.start()
