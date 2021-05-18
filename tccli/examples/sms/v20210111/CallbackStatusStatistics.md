**Example 1: 请求示例**



Input: 

```
tccli sms CallbackStatusStatistics --cli-unfold-argument  \
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
        "CallbackStatusStatistics": {
            "CallbackCount": 1745,
            "RequestSuccessCount": 1880,
            "CallbackFailCount": 401,
            "CallbackSuccessCount": 1344,
            "InternalErrorCount": 0,
            "InvalidNumberCount": 0,
            "ShutdownErrorCount": 401,
            "BlackListCount": 0,
            "FrequencyLimitCount": 0
        },
        "RequestId": "3314836f-0b10-45cb-b7be-593e84c1c197"
    }
}
```

