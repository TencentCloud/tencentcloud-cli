**Example 1: 请求示例**



Input: 

```
tccli live DescribePlayErrorCodeDetailInfoList --cli-unfold-argument  \
    --StatType 4xx \
    --EndTime 2019-03-01T00:01:00+08:00 \
    --StartTime 2019-03-01T00:00:00+08:00 \
    --PlayDomains 5000.playdomain.com \
    --Granularity 1
```

Output: 
```
{
    "Response": {
        "HttpCodeList": [
            {
                "HttpCode": "4xx",
                "ValueList": [
                    {
                        "Time": "2019-03-01T00:00:00+08:00",
                        "Numbers": 20,
                        "Percentage": 0.96
                    }
                ]
            }
        ],
        "StatType": "4xx",
        "RequestId": "e6628973-db6a-48f1-9fcd-fe0b3ba54bc9"
    }
}
```

