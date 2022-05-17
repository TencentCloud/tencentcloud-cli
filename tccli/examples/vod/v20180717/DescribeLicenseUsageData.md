**Example 1: 查询 DRM 加密播放 License 请求次数**



Input: 

```
tccli vod DescribeLicenseUsageData --cli-unfold-argument  \
    --LicenseType DRM \
    --StartTime 2020-09-07T00:00:00+08:00 \
    --EndTime 2020-09-09T23:59:59+08:00
```

Output: 
```
{
    "Response": {
        "LicenseUsageDataSet": [
            {
                "Time": "2020-09-07T00:00:00+08:00",
                "Count": 2
            },
            {
                "Time": "2020-09-08T00:00:00+08:00",
                "Count": 2
            },
            {
                "Time": "2020-09-09T00:00:00+08:00",
                "Count": 2
            }
        ],
        "RequestId": "requestId"
    }
}
```

