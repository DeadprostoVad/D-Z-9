import datetime, time
import random

class Phone:
    brand: str
    model: str
    issue_year: int
    is_busy: bool
    call_history: list
    miss_call: list
    receive_sms: list
    random_tel: str
    start_call: time

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.call_history = []
        self.miss_call = []
        self.receive_sms = []
        self.start_call = 0
        self.is_busy = False

    def __str__(self):
        self.get_info()
        return ""

    def get_info(self):
        s = self.brand, self.model, self.issue_year, self.call_history
        print(s)
        return ''

    def receive_call(self, name, tell):
        if self.is_busy is False:
            self.start_call = datetime.datetime.today()
            self.is_busy = True
            print(f'\nЗвонит {name}\n')
            self.call_history.append([self.start_call.strftime("%Y-%m-%d %H.%M.%S"), name, tell])
        else:
            print('Занято')
            self.miss_call.append([self.start_call.strftime("%Y-%m-%d %H.%M.%S"), name, tell])
            self.call_history.append([self.start_call.strftime("%Y-%m-%d %H.%M.%S"), name, tell])

    def end_call(self):
        t2 = datetime.datetime.now()
        t = t2 - self.start_call
        self.is_busy = False
        print(f'\nЗвонок завершен.Время разговора: {t} \n')
        self.start_call = 0


    def recieve_sms(self, name, txt):
        t = datetime.datetime.today().strftime("%Y-%m-%d %H.%M.%S")
        self.receive_sms.append([name, t, txt, ])
        print(f'new sms: from {name} : {txt}')


    def history(self):
        print('\nИстория звонков:')
        for i in self.call_history:
            print(i)


    def sms_history(self):
        print(f'\nsms history:')
        for i in self.receive_sms:
            print(i)


def random_tel():
    str1 = '1234567890'
    l = list(str1)
    new_tel = '+375'
    for x in range(9):
        new_tel = new_tel + random.choice(l)
    return new_tel


a =  Phone("Poco", "M3_Pro_5G", 2021) #, Phone('Honor', '8X', 2018), Phone('Xiaomi', 'Redmi_Note_8_Pro', 2020), Phone('Huawei', 'Y5', 2015))

#print(l)
name1 = 'Vadim'
name2 = 'Tatyana'
name3 = 'Vlad'
tell1 = random_tel()
tell2 = random_tel()
tell3 = random_tel()
txt1 = 'Как дела?'
txt2 = 'Ты где?'
txt3 = 'Ты скоро'
a.recieve_sms(name1,txt1)
a.recieve_sms(name3,txt3)
a.recieve_sms(name2,txt2)
a.sms_history()

a.receive_call(name1,tell1)
time.sleep(10)
a.receive_call(name2,tell2)
a.end_call()
a.receive_call(name3,tell3)
a.end_call()
a.receive_call(name1,tell2)
time.sleep(1)
a.end_call()
a.history()




