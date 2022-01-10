import csv, os, re, sqlite3, subprocess, time, webbrowser
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets
from selenium import webdriver
from ui import Ui_error, Ui_successfully

os.system("TASKKILL /F /IM chromedriver.exe")
os.system("TASKKILL /F /IM chrome.exe")
url_authorization = "http://router.asus.com/Main_Login.asp"
head = "user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) TuneIn/1.20.0 Chrome/69.0.3497.128 Electron/4.2.8 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
prefs = {f"profile.default_content_settings.popups": 0, f"download.default_directory": f"{os.getcwd()}",
         "directory_upgrade": True}
options.add_argument(head)
options.add_experimental_option("prefs", prefs)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.headless = True
driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)


def adding_or_removing_or_rename_users(window_adding_and_removing_and_rename_users_2, ui_window_open_adding_and_removing_and_rename_users_2, table,
                             action):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    output = 1
    entered_users = ui_window_open_adding_and_removing_and_rename_users_2.input_group.toPlainText().split("\n")
    if action == "add":
        main_mac = getting_main_mac()
        cur.execute(f"SELECT COUNT (*) FROM \"{table}\"")
        number_users = cur.fetchone()[0]
        for i in entered_users:
         if "|" in i:
            clients_mac = i.split("|")[1].replace(" ", "")
            if len(clients_mac) == 17 and clients_mac[2] == ":" and clients_mac[5] == ":" and clients_mac[8] == ":" and clients_mac[11] == ":" and clients_mac[14] == ":":
             pass
            else:
                output = 0
                withdraw_error(text_1="Был введён недопустимый MAC", text_2="Пример: 76:GL:D9:37:97:B5")
                break
         else:
             output = 0
             withdraw_error(text_1="Неправильный ввод", text_2="Пример: PO | 76:GL:D9:37:97:B5")
             break

        if output == 1:
          for i in entered_users:
             clients_name = i.split("|")[0].replace(" ", "")
             clients_mac = i.split("|")[1].replace(" ", "")
             if number_users != 63:
                try:
                    cur.execute(f"SELECT COUNT (*) FROM \"{table}\" WHERE clients_mac = \"{clients_mac}\"")
                    if cur.fetchone()[0] == 0:
                        cur.execute(f"INSERT INTO \"{table}\" (clients_name, clients_mac) VALUES (\"{clients_name}\", \"{clients_mac}\")")
                        number_users += 1
                except:
                    pass
             else:
                output = 0
                withdraw_error(text_1="Максимальное колличество пользователей - 63", text_2="")
                break
        cur.execute(f"DELETE FROM \"{table}\" WHERE clients_mac = \"{main_mac}\"")
    elif action == "remove":
        for i in entered_users:
            if "|" in i:
             clients_mac = i.split("|")[1].replace(" ", "")
             if len(clients_mac) == 17 and clients_mac[2] == ":" and clients_mac[5] == ":" and clients_mac[8] == ":" and clients_mac[11] == ":" and clients_mac[14] == ":":
              pass
             else:
                output = 0
                withdraw_error(text_1="Был введён недопустимый MAC", text_2="Пример: 76:GL:D9:37:97:B5")
                break
            else:
             output = 0
             withdraw_error(text_1="Неправильный ввод", text_2="Пример: PO | 76:GL:D9:37:97:B5")
             break

        if output == 1:
          for i in entered_users:
            try:
             clients_mac = i.split("|")[1].replace(" ", "")
             cur.execute(f"DELETE FROM \"{table}\" WHERE clients_mac = \"{clients_mac}\"")
            except:
                pass
    else:
        for i in entered_users:
         if "|" in i:
            clients_mac = i.split("|")[1].replace(" ", "")
            if len(clients_mac) == 17 and clients_mac[2] == ":" and clients_mac[5] == ":" and clients_mac[8] == ":" and clients_mac[11] == ":" and clients_mac[14] == ":":
             pass
            else:
                output = 0
                withdraw_error(text_1="Был введён недопустимый MAC", text_2="Пример: 76:GL:D9:37:97:B5")
                break
         else:
             output = 0
             withdraw_error(text_1="Неправильный ввод", text_2="Пример: PO | 76:GL:D9:37:97:B5")
             break
         if output == 1:
             for i in entered_users:
                 try:
                     clients_name = i.split("|")[0].replace(" ", "")
                     clients_mac = i.split("|")[1].replace(" ", "")
                     cur.execute(f"UPDATE \"{table}\" SET clients_name = \"{clients_name}\" WHERE clients_mac = \"{clients_mac}\"")
                 except:
                     pass

    if output == 1:
        window_adding_and_removing_and_rename_users_2.close()
        withdraw_successfully(value="default")
    con.commit()
    con.close()


def authorization_site():
    wifi = return_SSID()
    con = sqlite3.connect("router.db")
    cur = con.cursor()
    cur.execute(f"SELECT COUNT(*) FROM pers_inf WHERE wifi = \"{wifi}\"")
    if cur.fetchone()[0] != 0:
        con.close()
        driver.get(f"{url_authorization}")
        try:
         email_input = driver.find_element_by_id("login_username")
         email_input.send_keys(f"{getting_login_password_router(wifi)[0]}")
         password_input = ((driver.find_elements_by_name("login_passwd"))[0])
         password_input.send_keys(f"{getting_login_password_router(wifi)[1]}")
         driver.find_element_by_class_name("button").click()
         time.sleep(1)
         name_wifi = driver.find_element_by_id("elliptic_ssid_2g").text
         return True
        except:
         return False
    else:
        con.close()
        return False


def changing_router_login_password(wifi, new_login, new_password, window_changing_router_data):
    driver.get("http://router.asus.com/Advanced_System_Content.asp")
    login_old = driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[1]/td/div/input")[
        0]
    login_old.clear()
    login_old.send_keys(new_login)
    password_old = driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[2]/td/input")[0]
    password_old.send_keys(new_password)
    password_old_repeat = driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[3]/td/input")[0]
    password_old_repeat.send_keys(new_password)
    driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/div[6]/input")[0].click()
    time.sleep(1)
    con = sqlite3.connect("router.db")
    cur = con.cursor()
    cur.execute(f"UPDATE pers_inf SET login = \"{new_login}\" WHERE wifi = \"{wifi}\"")
    con.commit()
    cur.execute(f"UPDATE pers_inf SET password = \"{new_password}\" WHERE wifi = \"{wifi}\"")
    con.commit()
    con.close()
    window_changing_router_data.close()
    try:
     driver.switch_to.alert.accept()
    except:
        pass
    withdraw_successfully(value="otherwise")

def check_for_file_existence():
  if os.path.isfile("router.db"):
      pass
  else:
      file = open("temporary_files.txt", "w+", encoding="utf-8")
      creation_db()


def checking_tables(tables):
    all_tables = return_all_tables()
    issued_tables = []
    unique_tables = []
    non_unique_tables = []
    all_tables_treatment = []
    for i in all_tables:
        all_tables_treatment.append(i[0])
    if type(tables) == tuple:
        for i in tables:
            issued_tables.append(f"{i[0]}")
    elif type(tables) == list:
        for i in tables:
            issued_tables.append(f"{i}")
    else:
        issued_tables.append(f"{tables}")
    for i in issued_tables:
        if i not in all_tables_treatment:
            unique_tables.append(i)
        else:
            non_unique_tables.append(i)
    return (unique_tables, non_unique_tables)


def clearing_list_macs():
    driver.get("http://router.asus.com/Advanced_ACL_Content.asp")
    driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[3]/td/input[1]")[
        0].click()
    driver.find_elements_by_xpath(
        '/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[4]/td/select')[
        0].click()
    time.sleep(0.5)
    driver.find_elements_by_xpath(
        '/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[4]/td/select/option[1]')[
        0].click()

    for i in range(1, 65):
        try:
            driver.find_elements_by_xpath(
                "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/div[5]/table/tbody/tr[1]/td[2]/input")[
                0].click()
        except:
            break


def connection_check(decision):
    if authorization_site() == True:
        decision()
    else:
        withdraw_error(text_1="Не удалось подключиться к роутеру", text_2="Проверьте данные в настройках программы")


def creation_db():
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE devices (clients_name text, clients_mac text)")
    con.commit()
    con.close()
    con = sqlite3.connect("router.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE pers_inf (wifi text, login text, password text)")
    con.commit()
    con.close()


def data_change_wifi(window_data_change_wifi, ui_window_open_data_change_wifi):
    status = ""
    login_1 = ui_window_open_data_change_wifi.login_1.text()
    login_2 = ui_window_open_data_change_wifi.login_2.text()
    password_1 = ui_window_open_data_change_wifi.password_1.text()
    password_2 = ui_window_open_data_change_wifi.password_2.text()
    if login_1 == login_2:
        if password_1 == password_2:
            if len(password_1) >= 8:
                driver.get("http://router.asus.com./Advanced_Wireless_Content.asp")
                login = driver.find_elements_by_xpath(
                    "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/input")[
                    0]
                login.clear()
                login.send_keys(login_1)
                password = driver.find_elements_by_xpath(
                    "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input")[
                    0]
                password.clear()
                password.send_keys(password_1)
                driver.find_elements_by_xpath(
                    "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/div[5]/input")[
                    0].click()
                window_data_change_wifi.close()
                withdraw_successfully(value="default")
            else:
                status = "error"
        else:
            status = "error"
    else:
        status = "error"

    if status == "error":
        withdraw_error(text_1="Логины/пароли должны быть одинаковыми",
                       text_2="Пароль должен содержать не менее 8 символов")


def delete_group(window_delete_group, ui_window_open_delete_group):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    tables = ui_window_open_delete_group.input_group.toPlainText().split("\n")
    repeat_table = checking_tables(tables)[1]
    for i in repeat_table:
        cur.execute(f"DROP TABLE \"{i}\"")
    con.commit()
    con.close()
    window_delete_group.close()
    withdraw_successfully(value="default")


def denied_access():
    clearing_list_macs()
    driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr[2]/td[1]/input")[
        0].clear()
    driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr[2]/td[1]/input")[
        0].send_keys(getting_main_mac())
    driver.find_elements_by_xpath('//*[@id="MainTable2"]/tbody/tr[2]/td[2]/input')[0].click()
    driver.find_elements_by_xpath('//*[@id="submitBtn"]/input')[0].click()
    time.sleep(1)
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    withdraw_successfully(value="otherwise")


def download_csv_list():
    if os.path.exists("ClientList.csv"):
        os.remove("ClientList.csv")
    driver.get("http://router.asus.com/index.asp")
    driver.find_element_by_css_selector("#clients_td > input").click()
    driver.find_element_by_css_selector(
        "#clientlist_viewlist_block > table > tbody > tr > td > div:nth-child(3) > input").click()
    time.sleep(1)


def export_db():
    Desktop = f"{os.path.expanduser('~')}\Desktop"
    os.popen(f"copy data.db {Desktop}\data.db")
    withdraw_successfully(value="default")


def getting_connection_information(ui_window_open_info_connection):
    driver.get("http://router.asus.com/Advanced_Wireless_Content.asp")
    login = driver.find_element_by_id("elliptic_ssid_2g").text
    password = driver.find_element_by_name("wl_wpa_psk").get_attribute("value")
    driver.get("http://router.asus.com/index.asp")
    security = driver.find_elements_by_xpath(
        "/html/body/table/tbody/tr/td[3]/div/div[3]/div/table/tbody/tr[3]/td[2]/div[3]/strong")[0].text
    driver.get("http://router.asus.com/Advanced_ACL_Content.asp")
    radio_yes = driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[3]/td/input[1]")[
        0]
    radio_yes_value = str(radio_yes.get_attribute('value'))
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    use_tables = []
    if radio_yes_value == "0":
        radio_yes_value = "Отсутствуют"
    else:
        radio_yes_value = "Присутствуют"
        if os.path.isfile("mac_page.html"):
            os.remove("mac_page.html")
        html = driver.page_source
        page = open('mac_page.html', 'a+', encoding="utf-8")
        page.write(html)
        page.close()
        with open("mac_page.html", "r", encoding="utf-8") as f:
            contents = f.read()
            soup = BeautifulSoup(contents, 'lxml')
            strings = soup.find_all(string=re.compile('var wl_maclist_x_array'))
            list_mac = str(strings[0].split(";")).split("'")[1].replace("&#60", " ")[1:].split(" ")
            list_mac.remove(getting_main_mac())
        all_table = return_all_tables()
        for j in all_table:
            if j[0] != "devices":
                cur.execute(f"SELECT clients_mac FROM \"{j[0]}\"")
                clients_macs = cur.fetchall()
                len_clients_macs = len(clients_macs)
                for i in clients_macs:
                    if i[0] in list_mac:
                        len_clients_macs -= 1
                    else:
                        break
                if len_clients_macs == 0:
                    use_tables.append(f"{j[0]}")
    con.close()
    ui_window_open_info_connection.table_2_1.setText(f"{login}")
    ui_window_open_info_connection.table_2_2.setText(f"{password}")
    ui_window_open_info_connection.table_2_3.setText(f"{security}")
    ui_window_open_info_connection.table_2_4.setText(f"{radio_yes_value}")
    return use_tables


def getting_login_password_router(wifi):
    pers_inf = []
    con = sqlite3.connect("router.db")
    cur = con.cursor()
    cur.execute(f"SELECT login, password FROM pers_inf WHERE wifi = \"{wifi}\"")
    data = cur.fetchone()
    pers_inf.append(data[0])
    pers_inf.append(data[1])
    con.close()
    return pers_inf


def getting_main_mac():
    main_mac = str(subprocess.check_output('netsh wlan show interfaces', universal_newlines=True)).split(
        "Physical address")[1].split("\n")[0][-17:].upper()
    return main_mac


def getting_new_password(ui_closed_system, window_password_access):
    new_password = ui_closed_system.password_1.text()
    new_password_repeat = ui_closed_system.password_2.text()
    if new_password == new_password_repeat and len(new_password) >= 8:
        install_wpa2_wifi(new_password)
        window_password_access.close()
        withdraw_successfully(value="otherwise")
    else:
        withdraw_error(text_1="Пароли должны быть одинаковыми", text_2="Пароль должен содержать не менее 8 символов")


def getting_new_password_login_router(window_changing_router_data, ui_window_open_changing_router_data):
    wifi = return_SSID()
    new_password = ui_window_open_changing_router_data.password_1.text()
    new_password_repeat = ui_window_open_changing_router_data.password_2.text()
    new_login = ui_window_open_changing_router_data.login_1.text()
    new_login_repeat = ui_window_open_changing_router_data.login_2.text()
    if new_password == new_password_repeat and len(
            new_password) >= 8 and new_login == new_login_repeat and new_password != "admin":
        changing_router_login_password(wifi, new_login, new_password, window_changing_router_data)
    else:
        withdraw_error(text_1="Логины/пароли должны быть одинаковыми",
                       text_2="Пароль должен содержать не менее 8 символов")


def go_to_telegram():
    webbrowser.open("https://t.me/deprius_official_news", new=0, autoraise=True)


def group_access(window_group_access, ui_window_open_group_access):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    list_mac_0 = []
    tables = ui_window_open_group_access.input_group.toPlainText().split("\n")
    repeat_table = checking_tables(tables)[1]
    number_users_all = 0
    for i in repeat_table:
        cur.execute(f"SELECT COUNT (*) FROM \"{i}\"")
        number_users = cur.fetchone()[0]
        number_users_all += number_users
        cur.execute(f"SELECT clients_mac FROM \"{i}\"")
        clients_mac = cur.fetchall()
        for i in clients_mac:
            list_mac_0.append(i[0])
    list_mac_0.append(getting_main_mac())
    list_mac = list(set(list_mac_0))
    window_group_access.close()
    if number_users_all <= 64:
        clearing_list_macs()
        for row in list_mac:
            try:
                driver.find_elements_by_xpath(
                    "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr[2]/td[1]/input")[
                    0].clear()
                driver.find_elements_by_xpath(
                    "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr["
                    "2]/td[1]/input")[
                    0].send_keys(row)
                driver.find_elements_by_xpath('//*[@id="MainTable2"]/tbody/tr[2]/td[2]/input')[0].click()
                driver.switch_to.alert.accept()
            except:
                pass
        driver.find_elements_by_xpath('//*[@id="submitBtn"]/input')[0].click()
        withdraw_successfully(value="otherwise")
    else:
        withdraw_error(text_1="Лимит колличества пользователей", text_2="")
    con.close()


def group_creation(window_group_creation, ui_window_open_group_creation):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    plain_text = f"{ui_window_open_group_creation.input.toPlainText()}".lower()
    repeat_table = checking_tables(tables=plain_text)
    file = open("temporary_files.txt", "r+", encoding="utf-8")
    table = file.read()
    if table == "":
        if plain_text[0].isdigit() or any(
                x for x in '!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~ ' if x in plain_text) or re.search('[а-я]',
                                                                                                 plain_text) or len(
            repeat_table[0]) == 0 or plain_text == "all":
            withdraw_error(text_1="Недопустимое имя группы", text_2="")
        else:
            ui_window_open_group_creation.info.clear()
            ui_window_open_group_creation.info.setPlainText('Группа подготовлена и готова к использованию. Нажмите на кнопку "Принять" тогда, когда будете готовы поместить пользователей в группу')
            ui_window_open_group_creation.input.setPlainText('Для отмены действия закройте окно')
            file.write(f"{plain_text}")
    else:
            cur.execute(f"CREATE TABLE \"{table}\" (clients_name text, clients_mac "f"text)")
            main_mac = getting_main_mac()
            state_one = 0
            download_csv_list()
            time.sleep(2)
            with open('ClientList.csv', newline='', encoding="utf-8") as File:
                reader = csv.reader(File)
                for row in reader:
                    if state_one == 0:
                        state_one = 1
                    else:
                        cur.execute(f"SELECT COUNT(*) FROM devices WHERE clients_mac = \"{row[5]}\"")
                        if cur.fetchone()[0] == 0:
                            cur.execute(
                                f"INSERT INTO devices (clients_name, clients_mac) VALUES (\"{row[2]}\", \"{row[5]}\")")
                        cur.execute(
                            f"INSERT INTO \"{table}\" (clients_name, clients_mac) VALUES (\"{row[2]}\", \"{row[5]}\")")
            cur.execute(f"DELETE FROM \"{table}\" WHERE clients_mac = \"{main_mac}\"")
            window_group_creation.close()
            withdraw_successfully(value="default")
    file.close()
    con.commit()
    con.close()


def import_db(window_group_setting, QtWidgets):
    filename, filetype = QtWidgets.QFileDialog.getOpenFileName()
    if filename != "":
        os.replace(f"{filename}", f"{os.getcwd()}\\data.db")
        window_group_setting.close()
        withdraw_successfully(value="default")


def install_wpa2_wifi(new_password):
    driver.get("http://router.asus.com/Advanced_Wireless_Content.asp")
    driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[8]/td/select")[
        0].click()
    time.sleep(0.5)
    driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[8]/td/select/option[2]")[
        0].click()
    password_wifi = driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input")[0]
    password_wifi.clear()
    password_wifi.send_keys(f"{new_password}")
    driver.find_elements_by_id("applyButton")[0].click()
    time.sleep(1)


def off_group_access(window_internet_access):
    driver.get("http://router.asus.com/Advanced_ACL_Content.asp")
    driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[3]/td/input[2]")[
        0].click()
    driver.find_elements_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/div[6]/input")[0].click()
    window_internet_access.close()
    withdraw_successfully(value="otherwise")


def opening_access_wifi():
    driver.get("http://router.asus.com/Advanced_Wireless_Content.asp")
    driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[8]/td/select")[
        0].click()
    driver.find_elements_by_xpath(
        "/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[8]/td/select/option[1]")[
        0].click()
    driver.find_elements_by_id("applyButton")[0].click()
    time.sleep(1)
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    withdraw_successfully(value="otherwise")


def output_all_connections(ui_window_all_connections):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT clients_name, clients_mac FROM devices")
    devices = cur.fetchall()
    for i in devices:
        try:
            ui_window_all_connections.all_connections.setPlainText(
                f"{ui_window_all_connections.all_connections.toPlainText()}{i[0]} | {i[1]}\n")
        except:
            pass
    con.close()


def rename_group(window_rename_group, ui_window_open_rename_group):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    all_table = return_all_tables()
    old_name = ui_window_open_rename_group.input_group.toPlainText()
    new_name = ui_window_open_rename_group.input_group_2.toPlainText().lower()
    repeat_table = checking_tables(tables=[old_name, new_name])
    result = 0
    if new_name[0].isdigit() or any(
            x for x in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ' if x in new_name) or re.search('[а-я]',
                                                                                            new_name) or new_name not in \
            repeat_table[0] or old_name not in repeat_table[1] or new_name == "all":
        withdraw_error(text_1="Недопустимое имя группы", text_2="")
    else:
        for i in all_table:
            if i[0] == old_name:
                cur.execute(f"ALTER TABLE \"{old_name}\" RENAME TO \"{new_name}\"")
                result = 1
                break
        if result != 0:
            window_rename_group.close()
            withdraw_successfully(value="default")
        else:
            withdraw_error(text_1="Произошла непредвиденная ошибка", text_2="")
    con.commit()
    con.close()


def reset_program_settings(window_general_network_settings):
    os.remove("data.db")
    os.remove("router.db")
    creation_db()
    window_general_network_settings.close()
    withdraw_successfully(value="default")


def return_SSID():
    wifi = (str(subprocess.check_output("netsh wlan show interfaces"))).split("SSID")[1].split(":")[1].split("\\")[
        0].replace(" ", "")
    return wifi


def return_all_tables():
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute('SELECT name from sqlite_master where type = "table"')
    all_table = cur.fetchall()
    con.close()
    return all_table


def settings(window_settings, ui_window_open_settings):
    con = sqlite3.connect("router.db")
    cur = con.cursor()
    wifi = ui_window_open_settings.wifi.text()
    login = ui_window_open_settings.login.text()
    password = ui_window_open_settings.password.text()
    cur.execute(f"DELETE FROM pers_inf WHERE wifi = \"{wifi}\"")
    cur.execute(f"INSERT INTO pers_inf (wifi, login, password) VALUES (\"{wifi}\", \"{login}\", \"{password}\")")
    con.commit()
    con.close()
    window_settings.close()
    withdraw_successfully(value="default")


def show_group_users(ui_window_open_adding_and_removing_and_rename_users_1, ui_window_open_adding_and_removing_and_rename_users_2):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    table = ui_window_open_adding_and_removing_and_rename_users_1.input_group.toPlainText()
    cur.execute(f"SELECT clients_name, clients_mac FROM \"{table}\"")
    all_users = cur.fetchall()
    j = 1
    for i in all_users:
        ui_window_open_adding_and_removing_and_rename_users_2.info_group.setPlainText(
            f"{ui_window_open_adding_and_removing_and_rename_users_2.info_group.toPlainText()}{j}){i[0]} | {i[1]}\n\n")
        j += 1
    con.close()
    return table


def show_use_tables(ui_window_all_connections, decision):
    for i in decision:
        ui_window_all_connections.all_connections.setPlainText(
            f"{ui_window_all_connections.all_connections.toPlainText()}{i}\n")


def showing_groups(required_table):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    all_table = return_all_tables()
    for i in all_table:
        if i[0] != "devices":
            cur.execute(f"SELECT COUNT (*) FROM \"{i[0]}\"")
            number_users = cur.fetchone()[0]
            required_table.info_group.setPlainText(
                f"{required_table.info_group.toPlainText()}{i[0]} | {number_users}\n")


def withdraw_error(text_1, text_2):
    global window_error
    window_error = QtWidgets.QMainWindow()
    window_error.setFixedSize(440, 145)
    ui_error = Ui_error()
    ui_error.setupUi(window_error)
    ui_error.text_1.setText(f"{text_1}")
    ui_error.text_2.setText(f"{text_2}")
    window_error.show()


def withdraw_successfully(value):
    global window_successfully
    window_successfully = QtWidgets.QMainWindow()
    window_successfully.setFixedSize(440, 145)
    ui_successfully = Ui_successfully()
    ui_successfully.setupUi(window_successfully)
    if value == "default":
        ui_successfully.text_1.setText(f"Операция выполнена успешно")
    else:
        ui_successfully.text_1.setText(f"Изменения вступят в силу через 20 секунд")
        ui_successfully.text_2.setText(f"При необходимости заново подключитесь к сети")
    window_successfully.show()


check_for_file_existence()