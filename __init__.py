# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "Slack" + os.sep + "libs" + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from slack import RTMClient
from slack import WebClient
from slack_service import SlackService

"""
    Obtengo el modulo que fue invocado
"""
global slack_service_
module = GetParams("module")

if module == "connect":
    slack_token = GetParams("slack_token")
    res = GetParams("res")
    try:
        slack_service_ = None
        if slack_token:
            slack_service_ = SlackService(slack_token)
            SetVar(res, True)
        else:
            SetVar(res, False)
        if slack_token == None:
            SetVar(res, False)
    except Exception as e:
        SetVar(res, False)
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "send_message":
    channel = GetParams("channel_id")
    text = GetParams("message")
    res = GetParams("res")
    try:
        res_status_code = slack_service_.post_message(channel, text)
        if res_status_code == 200:   
            SetVar(res, True)
        if res_status_code != 200:   
            SetVar(res, False)    
    except Exception as e:
        SetVar(res, False)
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "upload_file":
    channel = GetParams("channel_id")
    text = GetParams("message")
    image = GetParams("image")
    res = GetParams("res")
    try:
        res_status_code = slack_service_.post_message_with_image(channel, text, image)
        print('Status code: ' + str(res_status_code))
        if res_status_code == 200:   
            SetVar(res, True)
        if res_status_code != 200:   
            SetVar(res, False)    
    except Exception as e:
        SetVar(res, False)
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "list_channels":
    res = GetParams("res")
    try:
        list_channels = slack_service_.list_channels('public_channel')
        #list_channels = slack_service_.list_channels('private_channel')
        SetVar(res, list_channels)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

@RTMClient.run_on(event="message")
def listen_events_slack(**payload):
    """
        This function triggers when someone sends
        a message on the slack
        """
    global message
    global rtm_client
    message = payload
    rtm_client._event_loop.stop()
    rtm_client._event_loop.close()

if module == "listen_channel":
    res = GetParams("res")
    try:
        rtm_client = None
        rtm_client = RTMClient(token=slack_service_.slack_token)
        print("Listening workspace")
        try:
            message = None
            rtm_client.start()
        except RuntimeError:
            pass
        rtm_client = None
        if message is not None:
            del message['rtm_client']
            del message['web_client']
            SetVar(res, message)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e
    
if module == "inviteUsers":
    channel = GetParams("channel_id1")
    users = GetParams("users")
    res = GetParams("res1")
    try:
        client = WebClient(token=slack_service_.slack_token)
        res_status_code = client.conversations_invite(channel=channel, users=users)
        print(res_status_code)
        if res_status_code['ok']:   
            SetVar(res, True)
        else:   
            SetVar(res, False)    
    except Exception as e:
        SetVar(res, False)
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e
    
