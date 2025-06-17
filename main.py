json_filter = {"size":99,
 "page":0,
 "filter":
 {
  "status":[],
  "idCertType":[],
  "idCertObjectType":[],
  "idProductType":[],
  "idGroupEEU":[],
  "idGroupRU":[],
  "idTechReg":[],
  "idApplicantType":[],
  "regDate":{"minDate":"","maxDate":""},
  "endDate":{"minDate":"","maxDate":""},
  "columnsSearch":[],
  "idProductSingleListRU":[],
  "idProductSingleListEEU":[]
 },
 "columnsSort":[{"column":"date","sort":"DESC"}]
}

import tkinter as tk, json

window = tk.Tk()
window.title('Парсер Сертификатов')
window.resizable(width=False, height=False)

date_label = tk.Label(window, text='Пожалуйста, вводите дату в формате год-месяц-число')
date_label.pack()

start_date_frame = tk.LabelFrame(window, text='Дата регистрации сертификата')
start_date_frame.pack()
start_date_label_left = tk.Label(start_date_frame, text='Минимальная дата')
start_date_label_left.pack(side='left')
start_date_label_right = tk.Label(start_date_frame, text='Максимальная дата')
start_date_label_right.pack(side='right')
start_date_entry_left = tk.Entry(start_date_frame, width=10)
start_date_entry_left.pack(side='left')
start_date_entry_right = tk.Entry(start_date_frame, width=10)
start_date_entry_right.pack(side='right')

end_date_frame = tk.LabelFrame(window, text='Дата окончания действия сертификата')
end_date_frame.pack()
end_date_label_left = tk.Label(end_date_frame, text='Минимальная дата')
end_date_label_left.pack(side='left')
end_date_label_right = tk.Label(end_date_frame, text='Максимальная дата')
end_date_label_right.pack(side='right')
end_date_entry_left = tk.Entry(end_date_frame, width=10)
end_date_entry_left.pack(side='left')
end_date_entry_right = tk.Entry(end_date_frame, width=10)
end_date_entry_right.pack(side='right')

def mode_filter(type_filter, id_):
    if json_filter['filter'][type_filter].count(id_) > 0:
        json_filter['filter'][type_filter].remove(id_)
    else:
        json_filter['filter'][type_filter].append(id_)

status_json = json.load(open('status.json', 'r', encoding='utf-8'))
status_menu = tk.Menu(tearoff=0)
for i in status_json:
    status_menu.add_checkbutton(label=i, command=lambda id_=status_json[i]['id']: mode_filter('status', id_))
status_button = tk.Button(window, text='Статус', command=lambda: status_menu.post(0,0))
status_button.pack()

cert_type_json = json.load(open('idCertType.json', 'r', encoding='utf-8'))
cert_type_menu = tk.Menu(tearoff=0)
for i in cert_type_json:
    cert_type_menu.add_checkbutton(label=i, command=lambda id_=cert_type_json[i]['id']: mode_filter('idCertType', id_))
cert_type_button = tk.Button(window, text='Тип сертификата', command=lambda: cert_type_menu.post(0,0))
cert_type_button.pack()

obj_type_json = json.load(open('idCertObjectType.json', 'r', encoding='utf-8'))
obj_type_menu = tk.Menu(tearoff=0)
for i in obj_type_json:
    obj_type_menu.add_checkbutton(label=i, command=lambda id_=obj_type_json[i]['id']: mode_filter('idCertObjectType', id_))
obj_type_button = tk.Button(window, text='Тип объекта сертификации', command=lambda: obj_type_menu.post(0,0))
obj_type_button.pack()

country_json = json.load(open('idProductType.json', 'r', encoding='utf-8'))
country_menu = tk.Menu(tearoff=0)
for i in country_json:
    country_menu.add_checkbutton(label=i, command=lambda id_=country_json[i]['id']: mode_filter('idProductType', id_))
country_button = tk.Button(window, text='Происхождение продукции', command=lambda: country_menu.post(0,0))
country_button.pack()

def tree_parsing(my_json, menu, filter_name):
    for i in my_json:
        if len(my_json[i]['items']) == 0:
            menu.add_checkbutton(label=i, command=lambda id_=my_json[i]['id']: mode_filter(filter_name, id_))
        else:
            menu1 = tk.Menu(tearoff=0)
            menu.add_cascade(label=i, menu=menu1)
            tree_parsing(my_json[i]['items'], menu1, filter_name)

EEU_groups_json = json.load(open('idGroupEEU.json', 'r', encoding='utf-8'))
EEU_groups_menu = tk.Menu(tearoff=0)
tree_parsing(EEU_groups_json, EEU_groups_menu, 'idGroupEEU')
EEU_groups_button = tk.Button(window, text='Группа продукции ЕАЭС', command=lambda: EEU_groups_menu.post(0,0))
EEU_groups_button.pack()

RU_groups_json = json.load(open('idGroupRU.json', 'r', encoding='utf-8'))
RU_groups_menu = tk.Menu(tearoff=0)
tree_parsing(RU_groups_json, RU_groups_menu, 'idGroupRU')
RU_groups_button = tk.Button(window, text='Группа продукции РФ', command=lambda: RU_groups_menu.post(0,0))
RU_groups_button.pack()

EEU_list_json = json.load(open('idProductSingleListEEU.json', 'r', encoding='utf-8'))
EEU_list_menu = tk.Menu(tearoff=0)
tree_parsing(EEU_list_json, EEU_list_menu, 'idProductSingleListEEU')
EEU_list_button = tk.Button(window, text='Единый перечень продукции ЕАЭС', command=lambda: EEU_list_menu.post(0,0))
EEU_list_button.pack()

RU_list_json = json.load(open('idProductSingleListRU.json', 'r', encoding='utf-8'))
RU_list_menu = tk.Menu(tearoff=0)
tree_parsing(RU_list_json, RU_list_menu, 'idProductSingleListRU')
RU_list_button = tk.Button(window, text='Единый перечень продукции РФ', command=lambda: RU_list_menu.post(0,0))
RU_list_button.pack()

tech_json = json.load(open('idTechReg.json', 'r', encoding='utf-8'))
tech_menu = tk.Menu(tearoff=0)
for i in tech_json:
    tech_menu.add_checkbutton(label=i, command=lambda id_=tech_json[i]['id']: mode_filter('idTechReg', id_))
tech_button = tk.Button(window, text='Технический регламент', command=lambda: tech_menu.post(0,0))
tech_button.pack()

applicant_json = json.load(open('idApplicantType.json', 'r', encoding='utf-8'))
applicant_menu = tk.Menu(tearoff=0)
for i in applicant_json:
    applicant_menu.add_checkbutton(label=i, command=lambda id_=applicant_json[i]['id']: mode_filter('idApplicantType', id_))
applicant_button = tk.Button(window, text='Вид заявителя', command=lambda: applicant_menu.post(0,0))
applicant_button.pack()

def launch():
    if len(end_date_entry_left.get()) > 0:
        end_date1 = end_date_entry_left.get()+"T00:00:00.000Z"
        json_filter['filter']['endDate']['minDate'] = end_date1
    if len(end_date_entry_right.get()) > 0:
        end_date2 = end_date_entry_right.get()+"T00:00:00.000Z"
        json_filter['filter']['endDate']['maxDate'] = end_date2
    if len(start_date_entry_left.get()) > 0:
        start_date1 = start_date_entry_left.get()+"T00:00:00.000Z"
        json_filter['filter']['regDate']['minDate'] = start_date1
    if len(start_date_entry_right.get()) > 0:
        start_date2 = start_date_entry_right.get()+"T00:00:00.000Z"
        json_filter['filter']['regDate']['maxDate'] = start_date2
    #print(json.dumps(json_filter, indent=4))
    window.destroy()

    import requests, random, time
    import pandas as pd
    from datetime import date
    from dateutil.relativedelta import relativedelta

    today = date.today()
    last_today = today +  relativedelta(months=1)
    last_today1 = today +  relativedelta(months=2)

    data = pd.DataFrame({
    "Ссылка на сертификат в реестре": [],
    "Дата окончания сертификата": [],
    "Заявитель": [],
    "Изготовитель": [],
    "Общее наименование": [],
    "Телефон": [],
    "Почта": [],
    "Номер сертификата": [],
    "Имя": []
    })

    headers1 = {
    "Host": "pub.fsa.gov.ru",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Authorization": "Bearer null",
    "lkId": "",
    "orgId": "",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",
    "Content-Length": "2000",
    "Origin": "https://pub.fsa.gov.ru",
    "Connection": "keep-alive",
    "Referer": "https://pub.fsa.gov.ru/rss/certificate",
    "Cookie": "JSESSIONID=node015z2sdlw6pjyehncmf9fivyh1815751.node0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
    }
    while True:
        try:
            r_log = requests.post('https://pub.fsa.gov.ru/login', json={"username":"anonymous","password":"hrgesf7HDR67Bd"}, headers=headers1, verify=False)
            if not(r_log):
                print(r_log)
                raise BaseException
            break
        except BaseException:
            pass
    auth_token = r_log.headers['Authorization']
    headers1['Authorization'] = auth_token
    headers2 = {
    "Host": "pub.fsa.gov.ru",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Authorization": auth_token,
    "lkId": "",
    "orgId": "",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Origin": "https://pub.fsa.gov.ru",
    "Connection": "keep-alive",
    "Referer":"JSESSIONID=node015z2sdlw6pjyehncmf9fivyh1815751.node0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
    }

    n = -1
    json_filter['page'] = -1
    while True:
        json_filter['page'] += 1
        time.sleep(random.uniform(0.5, 1.5))
        try:
            r = requests.post('https://pub.fsa.gov.ru/api/v1/rss/common/certificates/get', json = json_filter, headers=headers1, verify=False)
            if not(r):
                raise BaseException
        except BaseException:
            try:
                r = requests.post('https://pub.fsa.gov.ru/api/v1/rss/common/certificates/get', json = json_filter, headers=headers1, verify=False)
                if not(r):
                    raise BaseException
            except BaseException:
                print(r)
                continue
        if len(r.json()['items']) > 0:
            for cert in r.json()['items']:
                new_series = ['', '' , '', '', '', '', '', '', '']
                n += 1
                time.sleep(random.uniform(0.5, 1.5))
                certificate_id = cert['id']
                new_series[0] = f'https://pub.fsa.gov.ru/rss/certificate/view/{certificate_id}/baseInfo'
                new_series[1] = cert['endDate']
                new_series[3] = cert['manufacterName']
                new_series[2] = cert['applicantName']
                new_series[4] = cert['productFullName']
                new_series[7] = certificate_id
                try:
                    r_cert = requests.get(f'https://pub.fsa.gov.ru/api/v1/rss/common/certificates/{certificate_id}', headers=headers2, verify=False)
                    if not(r_cert):
                        raise BaseException
                except BaseException:
                    try:
                        r_cert = requests.get(f'https://pub.fsa.gov.ru/api/v1/rss/common/certificates/{certificate_id}', headers=headers2, verify=False)
                        if not(r_cert):
                            raise BaseException
                    except BaseException:
                        print(r_cert)
                        data.loc[n] = new_series
                        continue
                try:
                    applicant_data = r_cert.json()['applicant']
                    if list(applicant_data.keys()).count('surname') > 0 and type(applicant_data['surname']) == str:
                        new_series[8] += applicant_data['surname']+' '
                    if list(applicant_data.keys()).count('firstName') > 0 and type(applicant_data['firstName']) == str:
                        new_series[8] += applicant_data['firstName']+' '
                    if list(applicant_data.keys()).count('patronymic') > 0 and type(applicant_data['patronymic']) == str:
                        new_series[8] += applicant_data['patronymic']
                    for i in applicant_data['contacts']:
                        if i['idContactType'] == 4 and new_series[6] == '':
                            new_series[6] = i['value']
                        elif i['idContactType'] != 4 and new_series[5] == '':
                            new_series[5] = i['value']
                except BaseException:
                    pass
                data.loc[n] = new_series
        else:
            break
    with pd.ExcelWriter("result.xlsx", engine='xlsxwriter') as writer:
        data.to_excel(writer)

launch_button = tk.Button(window, bg='red', text='Запустить', command=launch)
launch_button.pack()
window.mainloop()
