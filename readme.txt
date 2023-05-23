çalıştırmak için python gereklidir cmd ye python yazarak kontrol edebilirsiniz

bat files:
install.bat batch dosyası rest api nin çalışacağı virtual enviroment ı kurup çalıştırıp(call edip) gerekli dependencyleri yükler
initiliaze_database.bat OrgResProject altındaki text filedan veritabanını yükler, sqllite db ilgili dizine oluşturulur
run_server.bat virtual env call edilerek sunucu çalıştırılır manage.py ile
multi_thread_api_test.bat ile de OrgResProject altındaki testapi.py ile sunucuyu multithread request gönderilir(id [1..10])

install.bat -> initiliaze_database.bat -> run_server.bat

api test:
sunucu çalışır haldeyken http://127.0.0.1:8000/adults/100 ile sunucuya get request i yollayabilirsiniz record_id:100 olan objeyi dönecektir
http://127.0.0.1:8000/adults/ db deki tüm objeleri döner
POSTMAN gibi bir uygulamayla birlikte 127.0.0.1:8000/queryAdultTrain POST isteği atarsanız(*body ile) size veritabanını ilgili filtrelerle sorgulayıp bulduklarını dönecektir

*body
[
    {
        "columnName": "AGE",
        "columnValueInt": "37"
    },
    {
        "columnName": "EDUCATION",
        "columnValueStr": "Masters"
    },
    {
        "columnName": "WORKCLASS",
        "columnValueStr": "Private"
    }
]

python files:
databaseinit.py veritabanı create ve insert işlemleri
models.py django models
mylooger.py loglamak için kullanılan methodlar tutuluyor
serializers.py django serializers
settings.py django project settings , database ve dependency
testapi.py multithread request
urls.py sunucu request mapping
views.py request mappingden çağrılan methodlar (get post implementationları) 
