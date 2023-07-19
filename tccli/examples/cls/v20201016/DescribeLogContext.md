**Example 1: 检索上下文日志**

检索上下文日志

Input: 

```
tccli cls DescribeLogContext --cli-unfold-argument  \
    --TopicId 682d0718-07bb-4ec0-9fda-f1e9a2767e0b \
    --BTime 2021-04-25 14:25:00.000 \
    --PkgId 528C1318606EFEB8-1A7 \
    --PkgLogId 65536 \
    --PrevLogs 10 \
    --NextLogs 10
```

Output: 
```
{
    "Response": {
        "NextOver": false,
        "PrevOver": false,
        "LogContextInfos": [
            {
                "Content": "xxxxxxx",
                "HostName": "abc",
                "Filename": "/usr/local/services/cls_cgi_api3-1.0/log/cls_cgi.log.20210425",
                "PkgId": "528C1318606EFEB8-1A0",
                "PkgLogId": 196609,
                "Source": "100.105.60.255",
                "BTime": 323232323
            },
            {
                "Content": "x1x2x3",
                "HostName": "abcd",
                "Filename": "/usr/local/services/cls_cgi_api3-1.0/log/cls_cgi.log.20210425",
                "PkgId": "528C1318606EFEB8-1A1",
                "PkgLogId": 196609,
                "Source": "100.105.60.255",
                "BTime": 323232323
            }
        ],
        "RequestId": "b276cb6e-4687-11eb-b378-0242ac130002"
    }
}
```

