import win32con
import win32gui
frgrnd_wndw = win32gui.GetForegroundWindow()
win32gui.ShowWindow(frgrnd_wndw, win32con.SW_HIDE)


import functions_app
import sys
from ui import *


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setFixedSize(900, 540)
ui_MainWindow = Ui_MainWindow()
ui_MainWindow.setupUi(MainWindow)
MainWindow.show()


def open_all_connections(decision):
    global window_all_connections
    window_all_connections = QtWidgets.QMainWindow()
    window_all_connections.setFixedSize(530, 530)
    ui_window_all_connections = Ui_all_connections()
    ui_window_all_connections.setupUi(window_all_connections)
    if decision == "connections":
     functions_app.output_all_connections(ui_window_all_connections)
    else:
        functions_app.show_use_tables(ui_window_all_connections, decision)
    window_all_connections.show()


def open_changing_router_data():
    global window_changing_router_data
    window_changing_router_data = QtWidgets.QMainWindow()
    window_changing_router_data.setFixedSize(650, 350)
    ui_window_open_changing_router_data = Ui_changing_router_data()
    ui_window_open_changing_router_data.setupUi(window_changing_router_data)
    window_general_network_settings.close()
    window_changing_router_data.show()
    ui_window_open_changing_router_data.accept_button.clicked.connect(
        lambda: functions_app.getting_new_password_login_router(window_changing_router_data,
                                                                ui_window_open_changing_router_data))


def open_data_change_wifi():
    global window_data_change_wifi
    window_data_change_wifi = QtWidgets.QMainWindow()
    window_data_change_wifi.setFixedSize(650, 350)
    ui_window_open_data_change_wifi = Ui_data_change_wifi()
    ui_window_open_data_change_wifi.setupUi(window_data_change_wifi)
    window_data_change_wifi.show()
    ui_window_open_data_change_wifi.accept_button.clicked.connect(
        lambda: functions_app.data_change_wifi(window_data_change_wifi, ui_window_open_data_change_wifi))


def open_delete_group():
    global window_delete_group
    window_delete_group = QtWidgets.QMainWindow()
    window_delete_group.setFixedSize(900, 530)
    ui_window_open_delete_group = Ui_deleting_and_adding_groups()
    ui_window_open_delete_group.setupUi(window_delete_group)
    ui_window_open_delete_group.text_1.setText("Введите группы для удаления")
    functions_app.showing_groups(required_table=ui_window_open_delete_group)
    window_group_action.close()
    window_delete_group.show()
    ui_window_open_delete_group.accept_button.clicked.connect(
        lambda: functions_app.delete_group(window_delete_group, ui_window_open_delete_group))


def open_general_network_settings():
    global window_general_network_settings
    window_general_network_settings = QtWidgets.QMainWindow()
    window_general_network_settings.setFixedSize(700, 540)
    ui_window_open_general_network_settings = Ui_general_network_settings()
    ui_window_open_general_network_settings.setupUi(window_general_network_settings)
    window_general_network_settings.show()
    ui_window_open_general_network_settings.data_change_wifi_button.clicked.connect(lambda: open_data_change_wifi())
    ui_window_open_general_network_settings.initial_settings_button.clicked.connect(
        lambda: functions_app.reset_program_settings(window_general_network_settings))
    ui_window_open_general_network_settings.all_connections_button.clicked.connect(lambda: open_all_connections(decision="connections"))
    ui_window_open_general_network_settings.data_change_router_button.clicked.connect(
        lambda: open_changing_router_data())


def open_group_access(window_internet_access):
    global window_group_access
    window_group_access = QtWidgets.QMainWindow()
    window_group_access.setFixedSize(900, 530)
    ui_window_open_group_access = Ui_deleting_and_adding_groups()
    ui_window_open_group_access.setupUi(window_group_access)
    ui_window_open_group_access.text_1.setText("Введите группы для добавления")
    functions_app.showing_groups(required_table=ui_window_open_group_access)
    window_internet_access.close()
    window_group_access.show()
    ui_window_open_group_access.accept_button.clicked.connect(
        lambda: functions_app.group_access(window_group_access, ui_window_open_group_access))


def open_group_action():
    global window_group_action
    window_group_action = QtWidgets.QMainWindow()
    window_group_action.setFixedSize(700, 680)
    ui_window_open_group_action = Ui_group_action()
    ui_window_open_group_action.setupUi(window_group_action)
    window_group_setting.close()
    window_group_action.show()
    ui_window_open_group_action.delete_group_button.clicked.connect(lambda: open_delete_group())
    ui_window_open_group_action.rename_group_button.clicked.connect(lambda: open_rename_group())
    ui_window_open_group_action.add_to_group_button.clicked.connect(
        lambda: open_adding_and_removing_and_rename_users_1(window_group_action, action="add"))
    ui_window_open_group_action.remove_from_group_button.clicked.connect(
        lambda: open_adding_and_removing_and_rename_users_1(window_group_action, action="remove"))
    ui_window_open_group_action.rename_users_button.clicked.connect(
        lambda: open_adding_and_removing_and_rename_users_1(window_group_action, action="rename"))


def open_group_creation():
    file = open('temporary_files.txt', 'w')
    file.close()
    global window_group_creation
    window_group_creation = QtWidgets.QMainWindow()
    window_group_creation.setFixedSize(530, 330)
    ui_window_open_group_creation = Ui_group_creation()
    ui_window_open_group_creation.setupUi(window_group_creation)
    ui_window_open_group_creation.info.setPlainText(
        f'{ui_window_open_group_creation.info.toPlainText()}Введите ниже имя нового списка через латиницу, первый сивол не может быть числом, а так же имя списка не может содержать никаких знаков, кроме "_"')
    window_group_creation.show()
    ui_window_open_group_creation.accept_button.clicked.connect(
        lambda: functions_app.group_creation(window_group_creation, ui_window_open_group_creation))


def open_group_setting():
    global window_group_setting
    window_group_setting = QtWidgets.QMainWindow()
    window_group_setting.setFixedSize(700, 540)
    ui_window_open_group_setting = Ui_group_setting()
    ui_window_open_group_setting.setupUi(window_group_setting)
    window_group_setting.show()
    ui_window_open_group_setting.automatic_group_creation_button.clicked.connect(lambda: open_group_creation())
    ui_window_open_group_setting.group_import_button.clicked.connect(
        lambda: functions_app.import_db(window_group_setting, QtWidgets))
    ui_window_open_group_setting.group_export_button.clicked.connect(
        lambda: functions_app.export_db())
    ui_window_open_group_setting.group_action_button.clicked.connect(lambda: open_group_action())


def open_info_1():
    global window_info_1
    window_info_1 = QtWidgets.QMainWindow()
    window_info_1.setFixedSize(650, 265)
    ui_window_open_info_1 = Ui_info_1()
    ui_window_open_info_1.setupUi(window_info_1)
    window_info_1.show()


def open_info_2():
    global window_info_2
    window_info_2 = QtWidgets.QMainWindow()
    window_info_2.setFixedSize(650, 200)
    ui_window_open_info_2 = Ui_info_2()
    ui_window_open_info_2.setupUi(window_info_2)
    window_info_2.show()


def open_info_3():
    global window_info_3
    window_info_3 = QtWidgets.QMainWindow()
    window_info_3.setFixedSize(650, 200)
    ui_window_open_info_3 = Ui_info_3()
    ui_window_open_info_3.setupUi(window_info_3)
    window_info_3.show()


def open_info_connection():
    global window_info_connection
    window_info_connection = QtWidgets.QMainWindow()
    window_info_connection.setFixedSize(330, 140)
    ui_window_open_info_connection = Ui_info_connection()
    ui_window_open_info_connection.setupUi(window_info_connection)
    use_tables = functions_app.getting_connection_information(ui_window_open_info_connection)
    window_info_connection.show()
    ui_window_open_info_connection.all_group.clicked.connect(lambda: open_all_connections(decision=use_tables))


def open_internet_access():
    global window_internet_access
    window_internet_access = QtWidgets.QMainWindow()
    window_internet_access.setFixedSize(700, 680)
    ui_window_open_internet_access = Ui_internet_access()
    ui_window_open_internet_access.setupUi(window_internet_access)
    window_internet_access.show()
    ui_window_open_internet_access.passwordless_access_button.clicked.connect(
        lambda: functions_app.opening_access_wifi())
    ui_window_open_internet_access.password_access_button.clicked.connect(lambda: open_password_access())
    ui_window_open_internet_access.denied_access_button.clicked.connect(
        lambda: functions_app.denied_access())
    ui_window_open_internet_access.group_access_button.clicked.connect(
        lambda: open_group_access(window_internet_access))
    ui_window_open_internet_access.group_off_access_button.clicked.connect(
        lambda: functions_app.off_group_access(window_internet_access))


def open_password_access():
    global window_password_access
    window_password_access = QtWidgets.QMainWindow()
    window_password_access.setFixedSize(605, 190)
    ui_window_open_password_access = Ui_password_access()
    ui_window_open_password_access.setupUi(window_password_access)
    window_password_access.show()
    ui_window_open_password_access.accept_button.clicked.connect(
        lambda: functions_app.getting_new_password(ui_window_open_password_access, window_password_access))


def open_adding_and_removing_and_rename_users_1(window_group_action, action):
    global window_adding_and_removing_and_rename_users_1
    window_adding_and_removing_and_rename_users_1 = QtWidgets.QMainWindow()
    window_adding_and_removing_and_rename_users_1.setFixedSize(900, 530)
    ui_window_open_adding_and_removing_and_rename_users_1 = Ui_adding_and_removing_and_rename_users_1()
    ui_window_open_adding_and_removing_and_rename_users_1.setupUi(window_adding_and_removing_and_rename_users_1)
    functions_app.showing_groups(required_table=ui_window_open_adding_and_removing_and_rename_users_1)
    window_group_action.close()
    window_adding_and_removing_and_rename_users_1.show()
    ui_window_open_adding_and_removing_and_rename_users_1.accept_button.clicked.connect(
        lambda: open_adding_and_removing_and_rename_users_2(window_adding_and_removing_and_rename_users_1,
                                                 ui_window_open_adding_and_removing_and_rename_users_1, action))


def open_adding_and_removing_and_rename_users_2(window_adding_and_removing_and_rename_users_1, ui_window_open_adding_and_removing_and_rename_users_1,
                                     action):
    table_availability = functions_app.checking_tables(tables = ui_window_open_adding_and_removing_and_rename_users_1.input_group.toPlainText())
    if table_availability[0] == []:
        global window_adding_and_removing_and_rename_users_2
        window_adding_and_removing_and_rename_users_2 = QtWidgets.QMainWindow()
        window_adding_and_removing_and_rename_users_2.setFixedSize(900, 530)
        ui_window_open_adding_and_removing_and_rename_users_2 = Ui_adding_and_removing_and_rename_users_2()
        ui_window_open_adding_and_removing_and_rename_users_2.setupUi(window_adding_and_removing_and_rename_users_2)
        window_adding_and_removing_and_rename_users_1.close()
        table = functions_app.show_group_users(ui_window_open_adding_and_removing_and_rename_users_1,
                                               ui_window_open_adding_and_removing_and_rename_users_2)
        if action == "rename":
            ui_window_open_adding_and_removing_and_rename_users_2.text_1.setText("Введите нов. имя устр. и mac")
        else:
            ui_window_open_adding_and_removing_and_rename_users_2.text_1.setText("Введите имя и mac устройств")
        window_adding_and_removing_and_rename_users_2.show()
        ui_window_open_adding_and_removing_and_rename_users_2.accept_button.clicked.connect(
            lambda: functions_app.adding_or_removing_or_rename_users(window_adding_and_removing_and_rename_users_2, ui_window_open_adding_and_removing_and_rename_users_2, table, action))
    else:
      functions_app.withdraw_error(text_1="Недопустимое имя таблицы", text_2="")

def open_rename_group():
    global window_rename_group
    window_rename_group = QtWidgets.QMainWindow()
    window_rename_group.setFixedSize(900, 530)
    ui_window_open_rename_group = Ui_rename_group()
    ui_window_open_rename_group.setupUi(window_rename_group)
    functions_app.showing_groups(required_table=ui_window_open_rename_group)
    window_rename_group.close()
    window_rename_group.show()
    ui_window_open_rename_group.accept_button.clicked.connect(
        lambda: functions_app.rename_group(window_rename_group, ui_window_open_rename_group))


def open_settings():
    global window_settings
    window_settings = QtWidgets.QMainWindow()
    window_settings.setFixedSize(460, 410)
    ui_window_open_settings = Ui_settings()
    ui_window_open_settings.setupUi(window_settings)
    window_settings.show()
    ui_window_open_settings.accept_button.clicked.connect(
        lambda: functions_app.settings(window_settings, ui_window_open_settings))


ui_MainWindow.connect_info_button.clicked.connect(lambda:  functions_app.connection_check(decision=open_info_connection))
ui_MainWindow.internet_access_button.clicked.connect(
    lambda: functions_app.connection_check(decision=open_internet_access))
ui_MainWindow.group_setting_button.clicked.connect(lambda: functions_app.connection_check(decision=open_group_setting))
ui_MainWindow.general_network_settings_button.clicked.connect(
    lambda: functions_app.connection_check(decision=open_general_network_settings))
ui_MainWindow.info_button_1.clicked.connect(lambda: open_info_1())
ui_MainWindow.info_button_2.clicked.connect(lambda: open_info_2())
ui_MainWindow.info_button_3.clicked.connect(lambda: open_info_3())
ui_MainWindow.transition_tg_button.clicked.connect(lambda: functions_app.go_to_telegram())
ui_MainWindow.top_setting_button.clicked.connect(lambda: open_settings())
sys.exit(app.exec_())
