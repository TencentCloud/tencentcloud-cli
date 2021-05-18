**Example 1: 请求示例**



Input: 

```
tccli sms SendStatusStatistics --cli-unfold-argument  \
    --SmsSdkAppId 1400006874 \
    --EndTime 2021050123 \
    --Limit 0 \
    --BeginTime 2021050113 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "SendStatusStatistics": {
            "FeeCount": 1880,
            "RequestCount": 1880,
            "RequestSuccessCount": 1880
        },
        "RequestId": "f36e4f00-605e-49b1-ad0d-bfaba81c7325"
    }
}
```

