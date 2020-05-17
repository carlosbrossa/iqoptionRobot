from login import sign
from iqoptionapi.stable_api import IQ_Option
import time, json

user = raw_input('Please enter your email: ')
print("You entered: " + user)

password = raw_input("Please enter your password: ")

API = sign(user, password)

def getProfile(API):
    perfil = json.loads(json.dumps(API.get_profile_ansyc()))
    return perfil
 
profile = getProfile(API)
print('user: ' + profile['email'])
print('currency: ' + profile['currency'])
print('your balance: ' + str(API.get_balance()))

par = 'EURUSD-OTC'
amount = 12
direction = 'call'
timeframe = 1

print('\n')
print('Init pay for par=' + par + ' amount=' + str(amount) + ' direction=' + direction +  ' timeframe=' + str(timeframe))

status, id = API.buy(amount, par, direction, timeframe)

print('\n')
print('status=' + str(status))
print(id)
print('id=' + str(id))
print('\n')

if status:
    lucro = API.check_win_v3(id)
    print(' LUCRO: ' + str(lucro))

