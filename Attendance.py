import paramiko
import requests,json, datetime,io
from datetime import  date, timedelta 
import csv
import time
import pandas as pd
import pysftp


def attadance():

    fromdate = datetime.date.today()-timedelta(1)
    # if fromdate.day > 31:
    #     fromdate += datetime.timedelta(7)
    # fromdate = fromdate.replace(day=1)
    fromdate = fromdate
    print (fromdate)

    # fromDate = date.today() - timedelta(1)
    # print("FFFFFFRRRRRRR",fromDate)
    toDate = date.today()-timedelta(1)
    # toDate = 
    # print("TTTTTTTTTTTTTTTTTTTTTTTTOOOOOOOOOOOOOOOOOOOOOOOOOOOOO",toDate)
    # # print("time>>>>>>>>>>>>>>>>>>>>>>>>",timestr)\
    date_str = str(fromdate.strftime("%Y%m%d")) + "-" + str(toDate.strftime("%Y%m%d"))

    url = "http://localhost:82/api/v2/WebAPI/GetDeviceLogs?APIKey=482012072208&FromDate="+str(fromdate)+"&ToDate="+str(toDate)+""

    headers = {}
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response_dict = json.loads(response.text)
    # print(response.text)
    
    
    file_name = str(date_str)+".json"
    # print("file_name>>>>>>>>>>>>>>>>>>>>>>>>",file_name)
    
    attendance_file = json.dumps(response_dict)
    # print("attendance_file>>>>>>>>>>>>>>>>>>>>>>>>",attendance_file)
    
    with open(file_name,"w") as file:
        file.write(attendance_file)
    
    #print("attendance_file========================",attendance_file)
    
    # with pysftp.Connection(host="sftpodoo.rupiyatech.link", username="sftp_odoo", private_key=r'./rupiya-sftp-bucket/sftp_odoo/rupiya_attendance/') as sftp:
    #     with sftp.cd(r'/rupiya-sftp-bucket/sftp_odoo/rupiya_attendance'):#temporarily chdir to public
    #          sftp.put(attendance_file)  # upload file to public/ on remote
    #         # sftp.get('demo')
    # private_key = "~/.ssh/your-key.pem"  # can use password keyword in Connection instead

    
    #cnopts.hostkeys = None
    srv = pysftp.Connection(host="sftpodoo.rupiyatech.link",username="sftp_odoo",private_key='.\id_rsa_rupiya_sftpodoo')
    #srv = pysftp.Connection(host="sftp_odoo", username="sftpodoo.rupiyatech.link", password="",cnopts=cnopts)
    print("----------------------Connection Established Successfully")
    srv.cd('rupiya_attendance')
    #srv.remove('rupiya_attendance/'+file_name)
    srv.put(file_name,'rupiya_attendance/'+file_name)
    srv.put(file_name)  # To download a file, replace put with get
    srv.close()  # Close connection

if __name__ == '__main__':       
    attadance()

