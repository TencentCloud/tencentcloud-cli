**Example 1: 查询域名日志下载链接**



Input: 

```
tccli ecdn DescribeEcdnDomainLogs --cli-unfold-argument  \
    --StartTime '2019-09-04 00:00:00' \
    --EndTime '2019-09-04 12:00:00' \
    --Domain www.test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "13d41d37-546f-42ed-a3b9-ff82a51ecd0a",
        "DomainLogs": [
            {
                "StartTime": "2019-09-04 23:00:00",
                "EndTime": "2019-09-04 23:59:59",
                "LogPath": "http://www.test.qcloud.com/20190904/23/201909042300-www.test.com.gz?st=hGzJr0QFpo3jYM2uj7kkjA&e=3135214538"
            }
        ],
        "TotalCount": 300
    }
}
```

