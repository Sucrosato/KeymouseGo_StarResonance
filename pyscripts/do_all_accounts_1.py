from auto_daily_work import login, logout, subrun
import time

def get_accounts():
    '''[[account ids for fast run], [account ids for slow run]]'''
    return [
        [],
        [
        '2021543280',
        '2023799194',
        '3842978571',]
    ]

if __name__ == '__main__':
    time.sleep(5)
    ids = get_accounts()
    for id in ids[0][:]: 
        login(id)
        subrun()
        logout()
    for id in ids[1][:]: 
        login(id)
        subrun(slow=True)
        logout()
