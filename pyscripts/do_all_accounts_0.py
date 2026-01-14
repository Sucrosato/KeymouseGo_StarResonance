from auto_daily_work import login, logout, subrun
import time

def get_accounts():
    '''[[account ids for fast run], [account ids for slow run]]'''
    return [
        ['3151557406',
        '3610876935',
        '1597036577',
        '3220825744',],
        [
        '1220468193',
        '1144236972',
        '3446345810',
        '2832907574',
        '3620953166',]
    ]

if __name__ == '__main__':
    time.sleep(7)
    ids = get_accounts()
    for id in ids[0][:]: 
        login(id)
        subrun()
        logout()
    for id in ids[1][:]: 
        login(id)
        subrun(slow=True)
        logout()
