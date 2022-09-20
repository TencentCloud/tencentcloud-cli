**Example 1: 下载七层离线日志**



Input: 

```
tccli teo DownloadL7Logs --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --StartTime 2022-05-04T03:27:00+08:00 \
    --EndTime 2022-05-10T23:59:00+08:00
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "6f07d593-44d7-4bac-a119-e1923ab5b377",
        "Data": [
            {
                "Area": "mainland",
                "Domain": "test-add4.wellsjiang.com",
                "LogPacketName": "20220811-02-test-add4.wellsjiang.com",
                "LogTime": 1660183200,
                "Size": 7539,
                "Url": "https://log-down07-cn.edgeone.qcloud.com/2022081102-test-add4.wellsjiang.com.log.gz"
            }
        ]
    }
}
```

