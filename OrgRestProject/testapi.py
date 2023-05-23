import json
from urllib import response
import requests
import multiprocessing

url = 'http://127.0.0.1:8000/queryAdultTrain'
req_data = [[{"columnName": "RECORD_ID", "columnValueInt": "1"}], [{"columnName": "RECORD_ID","columnValueInt": "2"}],
            [{"columnName": "RECORD_ID", "columnValueInt": "3"}], [{"columnName": "RECORD_ID","columnValueInt": "4"}],
            [{"columnName": "RECORD_ID", "columnValueInt": "5"}], [{"columnName": "RECORD_ID","columnValueInt": "6"}],
            [{"columnName": "RECORD_ID", "columnValueInt": "7"}], [{"columnName": "RECORD_ID","columnValueInt": "8"}],
            [{"columnName": "RECORD_ID", "columnValueInt": "9"}], [{"columnName": "RECORD_ID","columnValueInt": "10"}]]


def query_test(post_data):
    json_array = []
    response = requests.post(url,json=post_data)
    json_array.append(response.json())
    return json_array

print("multiprocessing starts")
if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool = multiprocessing.Pool(processes=10)
    outputs = pool.map(query_test, req_data)
    print("you can also check rest_api.log file to see server output which adds process number lines")
    print("Output: {}".format(outputs))