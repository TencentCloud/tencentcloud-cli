**Example 1: 请求示例**



Input: 

```
tccli sms CallbackStatusStatistics --cli-unfold-argument  \
    --StartDateTime 2016090800 \
    --EndDataTime 2016090823 \
    --SmsSdkAppid 1400006874 \
    --Limit 0 \
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

