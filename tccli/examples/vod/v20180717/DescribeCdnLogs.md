**Example 1: 查询CDN日志下载链接**



Input: 

```
tccli vod DescribeCdnLogs --cli-unfold-argument  \
    --DomainName test.vod2.myqcloud.com \
    --StartTime 2021-03-01T00:00:00+08:00 \
    --EndTime 2021-03-02T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "TotalCount": 202,
        "DomesticCdnLogs": [
            {
                "Date": "2021-03-01",
                "Name": "2018120213-test.vod2.myqcloud.com",
                "Url": "http: //test.log.cdn/2018120213-test.vod2.myqcloud.com.tar.gz",
                "StartTime": "2021-03-01T15:00:00+08:00",
                "EndTime": "2021-03-01T15:59:59+08:00"
            }
        ],
        "OverseaCdnLogs": [],
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

