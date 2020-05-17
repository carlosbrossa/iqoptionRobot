from iqoptionapi.stable_api import IQ_Option
import time, json

MODE="PRACTICE"

API = IQ_Option('user', 'pass')
API.connect()
print('conecting ...')
print(API.check_connect)
API.change_balance(MODE)

def getProfile(API):
    perfil = json.loads(json.dumps(API.get_profile_ansyc()))
    return perfil
 

profile = getProfile(API)
print(profile['name'])
print(profile['last_name'])
print(profile['email'])
print(profile['currency'])
print(API.get_balance())

par = 'EURUSD-OTC'
entrada = 12
direcao = 'call'
timeframe = 1

status, id = API.buy(entrada, par, direcao, timeframe)

print(status)
print(id)

if status:
    lucro = API.check_win_v3(id)
    print(' LUCRO: ' + str(lucro))
