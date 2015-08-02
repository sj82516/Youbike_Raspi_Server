# Youbike_Raspi_Server

##api.py
功用：網站檔，讓使用者可以讀取資料，ip/date取得當天資料，ip/date1/date2取得期間資料  
參考資料：http://blog.kenyang.net/2013/05/nginx-flask-uwsgi-deployment.html
![alt tag](https://github.com/sj82516/Youbike_Raspi_Server/blob/master/img/web_request_result.jpg)

##getData.py
功用：自動到Data.Taipei抓資料，按照不同天數劃分Table
![alt tag](https://github.com/sj82516/Youbike_Raspi_Server/blob/master/img/check_DB.jpg)

##進階
設定crontab，讓getData.py自動每隔十分鐘執行一次
一天下來約60筆，遺失率約50%.... 可以調高抓取頻率
![alt tag](https://github.com/sj82516/Youbike_Raspi_Server/blob/master/img/table_result.jpg)

