**Example 1: 搜索已经添加的域名**



Input: 

```
tccli sslpod DescribeDomains --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1000 \
    --SearchType none \
    --Tag  \
    --Grade  \
    --Brand  \
    --Code  \
    --Hash 
```

Output: 
```
{
    "Response": {
        "Data": {
            "SearchTotal": 3,
            "Total": 3,
            "Result": [
                {
                    "Id": 13079,
                    "Domain": "cloud.tencent.com",
                    "Ip": "1.1.1.1",
                    "AutoIP": true,
                    "Port": "443",
                    "ServerType": 0,
                    "Brand": "xxxxx",
                    "Status": "正常",
                    "Grade": "",
                    "GradeCode": 0,
                    "Notice": false,
                    "AccountDomainId": 15072,
                    "Tags": [
                        "123"
                    ]
                },
                {
                    "Id": 13078,
                    "Domain": "1.qcloud.com",
                    "Ip": "2.2.2.2",
                    "AutoIP": true,
                    "Port": "80",
                    "ServerType": 0,
                    "Brand": "",
                    "Status": "连接异常",
                    "Grade": "",
                    "GradeCode": 0,
                    "Notice": false,
                    "AccountDomainId": 15071,
                    "Tags": [
                        "123"
                    ]
                },
                {
                    "Id": 13077,
                    "Domain": "2.qcloud.com",
                    "Ip": "3.3.3.3",
                    "AutoIP": true,
                    "Port": "80",
                    "ServerType": 0,
                    "Brand": "",
                    "Status": "连接异常",
                    "Grade": "",
                    "GradeCode": 0,
                    "Notice": false,
                    "AccountDomainId": 15070,
                    "Tags": [
                        "123"
                    ]
                }
            ],
            "AllowMonitoringCount": 3,
            "CurrentMonitoringCount": 0,
            "AllowMaxAddDomain": 20
        },
        "RequestId": "b106abc5-de9e-48ea-b95b-871ac898edd7"
    }
}
```

