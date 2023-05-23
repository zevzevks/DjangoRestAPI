import logging

class mylogger():

    #rest api logger method
    def restlogger(request_timestamp,request_url,request_data,response_timestamp,response_status,response_data = None):
        logging.basicConfig(filename='rest_api.log', encoding='utf-8', level=logging.INFO)
        logging.info('RequestTimestamp:%s -- RequestURL:%s -- RequestBody:%s -- ResponseTimestamp:%s -- ResponseCode:%s -- ResponseBody:%s',request_timestamp,request_url,request_data,response_timestamp,response_status,response_data)
        print('')
        print('LOGGER METHOD REQUEST OUTPUT:')
        print(request_timestamp,'// URL :',request_url,'// REQUEST :',request_data)
        print('LOGGER METHOD RESPONSE OUTPUT:')
        print(response_timestamp,'// STATUS: ',response_status,'// RESPONSE: ',response_data)
        print('')
        
    def exceptionlogger(e,response_timestamp):
        logging.basicConfig(filename='rest_api.log', encoding='utf-8', level=logging.INFO)
        logging.exception("EXCEPTION TIME: ",response_timestamp,"EXCEPTION MSG: ",e)
        print('')
        print('LOGGER METHOD OUTPUT:')
        print("Exception :",e)
        print('')