from exchangelib import DELEGATE, Account, Configuration, Credentials
from exchangelib.autodiscover import AutodiscoverProtocol
import sys
sys.path.append('../exchange_oth/')
import loginData as crd


config = Configuration(server='exchange.othr.de', credentials=crd.credentials)
account = Account(primary_smtp_address='simon1.hofmeister@st.othr.de', config=config,
                  autodiscover=False, access_type=DELEGATE)


i = 0
for calendar_item in account.calendar.all(): #all().order_by('datetime_received')
    if i == 0:
        print(calendar_item)
    i=i+1


for calendar_item in account.calendar.all(): #all().order_by('datetime_received')
    print('Kalender: ', 'Kalender', ', Termin: ', calendar_item.subject)
for cal in account.calendar.tree().split('\n'):
    while cal[0] < '0' or cal[0] > 'z':
        cal = cal[1:]
    if cal != 'Kalender' and cal != 'Calendar':
        for calendar_item in (account.calendar / cal).all():
            print('Kalender: ', cal, ', Termin: ', calendar_item.subject)

