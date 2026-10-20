**Example 1: 请求示例**



Input: 

```
tccli live DescribeStreamPackageRemuxStatistics --cli-unfold-argument  \
    --StartTime 2026-08-24T00:00:00+08:00 \
    --EndTime 2026-08-25T00:00:00+08:00 \
    --Dimension False \
    --Granularity 5
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "ChannelId": "/v1/019810d5882d1ea506ec36a2054bc5",
                "Remux": 35545189124
            }
        ],
        "TotalRemux": 1461990040036,
        "RequestId": "d7f31029-c8a3-4fe5-b5bd-85810bcc22b6"
    }
}
```

