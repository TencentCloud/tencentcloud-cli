**Example 1: 获取示例**



Input: 

```
tccli cdn GetDisableRecords --cli-unfold-argument  \
    --StartTime '2018-12-12 10:24:00' \
    --EndTime '2018-12-14 10:24:00'
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "f13cf55b-69e6-4937-8856-bd8965beea8c",
        "UrlRecordList": [
            {
                "Status": "enable",
                "RealUrl": "https://www.example.com/7349199.txt",
                "CreateTime": "2018-12-13 12:25:07",
                "UpdateTime": "2018-12-13 12:25:07"
            },
            {
                "Status": "disable",
                "RealUrl": "http://www.example.com/v1/example1.jpg",
                "CreateTime": "2018-12-13 14:40:59",
                "UpdateTime": "2018-12-13 14:40:59"
            }
        ]
    }
}
```

