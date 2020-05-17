from iqoptionapi.stable_api import IQ_Option

def sign(email, password):
    error_password="""{"code":"invalid_credentials","message":"You entered the wrong credentials. Please check that the login/password is correct."}"""
    iqoption = IQ_Option(email, password)
    check,reason=iqoption.connect()
    MODE = 'PRACTICE'
    if check:
        print('\n')
        print("user " +email+ " connected ")
        iqoption.change_balance(MODE)
        return iqoption
    
        #if see this you can close network for test
    elif iqoption.check_connect()==False:#detect the websocket is close
            print("try reconnect")
            check,reason=iqoption.connect()         
            if check:
                print("Reconnect successfully")
            else:
                if reason==error_password:
                    print("Error Password")
                else:
                    print("No Network")
    else:
        
        if reason=="[Errno -2] Name or service not known":
            print("No Network")
        elif reason==error_password:
            print("Error Password")