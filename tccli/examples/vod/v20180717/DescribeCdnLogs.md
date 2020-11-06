**Example 1: Querying CDN log download links**



Input: 

```
tccli vod DescribeCdnLogs --cli-unfold-argument  \
    --DomainName test.vod2.myqcloud.com \
    --StartTime 2018-12-0116:00:00Z \
    --EndTime 2018-12-0316:00:00Z
```

Output: 
```
{
    "Response": {
        "DomesticCdnLogs": [
            {
                "Date": "2018-12-02",
                "Name": "2018120213-test.vod2.myqcloud.com",
                "Url": "http: //test.log.cdn/2018120213-test.vod2.myqcloud.com.tar.gz"
            }
        ],
        "OverseaCdnLogs": null,
        "RequestId": "requestId"
    }
}
```

