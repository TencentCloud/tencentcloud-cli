**Example 1: 获取诊断任务列表**



Input: 

```
tccli cdn ListDiagnoseReport --cli-unfold-argument  \
    --KeyWords test.com/
```

Output: 
```
{
    "Response": {
        "RequestId": "b3eee570-0d5f-46b2-89a3-160f4e654eaf",
        "Data": [
            {
                "DiagnoseUrl": "http://www.test.com/2.txt",
                "DiagnoseLink": "http://cdn.cloud.tencent.com/self_diagnose/xx2",
                "CreateTime": "2020-09-21 12:00:08",
                "ExpireDate": "2020-09-22 12:00:08",
                "Area": "manland",
                "VisitCount": 9,
                "ClientList": [
                    {
                        "CreateTime": "2020-09-21 12:00:16",
                        "ReportId": "1",
                        "DiagnoseTag": "xx2",
                        "ClientInfo": [
                            {
                                "ProvName": "广东省",
                                "Country": "中国",
                                "IspName": "中国电信",
                                "Ip": "1.1.1.1"
                            }
                        ],
                        "FinalDiagnose": 2
                    }
                ]
            }
        ]
    }
}
```

