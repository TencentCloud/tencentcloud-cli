**Example 1: 日志下载链接查询**



Input: 

```
tccli cdn DescribeCdnDomainLogs --cli-unfold-argument  \
    --StartTime '2019-09-04 00:00:00'\
    --EndTime '2019-09-04 12:00:00'\
    --Domain www.test.com
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
                "LogPath": "http://www.test.qcloud.com/20190904/23/201909042300-www.test.com.gz?st=hGzJr0QFpo3jYM2uj7kkjA&e=3135214538"
            }
        ],
        "TotalCount": 300
    }
}
```

