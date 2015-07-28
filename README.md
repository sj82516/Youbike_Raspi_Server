# Youbike_Raspi_Server

##api.py
功用：網站檔，讓使用者可以讀取資料，ip/date取得當天資料，ip/date1/date2取得期間資料
參考資料：http://blog.kenyang.net/2013/05/nginx-flask-uwsgi-deployment.html

##getData.py
功用：自動到Data.Taipei抓資料，按照不同天數劃分Table

##進階
設定crontab讓getData.py自動每隔十分鐘執行一次


