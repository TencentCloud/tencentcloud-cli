**Example 1: 日志下载链接查询**

查询域名指定时间段的日志列表

Input: 

```
tccli cdn DescribeCdnDomainLogs --cli-unfold-argument  \
    --Domain www.test.com \
    --EndTime 2019-09-04 12:00:00 \
    --StartTime 2019-09-04 00:00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "DomainLogs": [
            {
                "Area": "mainland",
                "StartTime": "2019-09-04 23:00:00",
                "EndTime": "2019-09-04 23:59:59",
                "LogPath": "http://www.test.qcloud.com/20190904/23/201909042300-www.test.com.gz?st=hGzJr0QFpo3jYM2uj7kkjA&e=3135214538",
                "LogName": "2019090423",
                "FileSize": 9999
            }
        ],
        "TotalCount": 300
    }
}
```

