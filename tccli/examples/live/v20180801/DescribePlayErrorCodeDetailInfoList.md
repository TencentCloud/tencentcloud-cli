**Example 1: 请求示例**



Input: 

```
tccli live DescribePlayErrorCodeDetailInfoList --cli-unfold-argument  \
    --PlayDomains 5000.playdomain.com \
    --StartTime '2019-03-01 00:00:00' \
    --EndTime '2019-03-01 00:01:00' \
    --Granularity 1 \
    --StatType 4xx
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
                        "Time": "2019-03-01 00:00:00",
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

