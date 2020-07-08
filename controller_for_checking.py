import os
import pywinauto as pw
import time

def controller(file_path, file_name, app_path, saving_path, window_size, step_size):
	"""file_path - path to file in sse extension with file included+watch for path=r""!
	app_path - path to sse executable
	saving_path - path to folder for output, / is subsituted for //
	window and step should contain int in str format"""
	os.startfile(file_path+file_name)
	time.sleep(5)
	app = pw.Application(backend = 'win32').connect(path = app_path)
	time.sleep(5)
	while True:
		try:
			dlg = app.window(title_re = 'Recover')
			dlg.type_keys('{TAB}{ENTER}')
		except pw.findwindows.ElementNotFoundError:
			break
	dlg = app.window(title_re="Loading File")
	app.dlg.type_keys('{ENTER}')
	time.sleep(5)
	dlg = app.window(title_re="SSE")
	dlg.type_keys('{F10}{r}{g}{ENTER}')
	time.sleep(5)
	dlg = app.window(title_re="Grouping Scan Parameters")
	dlg.ComboBox0.select("File")
	dlg.Edit0.set_text(saving_path)
	dlg.Edit2.set_text(str(window_size) + "_" + str(step_size) + "_" + str(round(time.time(), 0))[:-2])
	dlg.Edit3.set_text("1")
	dlg.Edit4.set_text("10245")
	dlg.ComboBox4.select("K2P")
	dlg.Edit5.set_text("default")
	dlg.Button16.click()
	time.sleep(5)
	dlg = app.window(title_re = "Scan Variables")
	dlg.Edit1.set_text(window_size)
	dlg.Edit2.set_text(step_size)
	dlg.Button3.click()

def closing_app(app_path):
	while True:
		try:
			app = pw.Application(backend = 'win32').connect(path = app_path)
			app.kill()
		except pw.application.ProcessNotFoundError:
			break