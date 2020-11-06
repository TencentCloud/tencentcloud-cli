**Example 1: 请求示例**



Input: 

```
tccli live DescribeLogDownloadList --cli-unfold-argument  \
    --PlayDomains 5000.liveplay.com \
    --StartTime '2019-03-12 00:00:00' \
    --EndTime '2019-03-12 12:00:00'
```

Output: 
```
{
    "Response": {
        "LogInfoList": [
            {
                "LogName": "test",
                "LogUrl": "http://test.log.com",
                "LogTime": "2019-03-13 00:00:00",
                "FileSize": 1000
            }
        ],
        "TotalNum": 1,
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

