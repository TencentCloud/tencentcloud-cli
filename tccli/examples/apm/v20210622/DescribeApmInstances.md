**Example 1: 拉取APM实例列表**

拉取APM实例列表

Input: 

```
tccli apm DescribeApmInstances --cli-unfold-argument  \
    --Tags.0.Key appid \
    --Tags.0.Value 1231
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "Name": "APM自动化测试",
                "InstanceId": "apm-OzNrwxuDj",
                "Description": "test123",
                "TraceDuration": 1,
                "AppId": 251226959,
                "CreateUin": "700000357122",
                "Tags": [
                    {
                        "Key": "AutoTest",
                        "Value": "cvm"
                    }
                ],
                "ServiceCount": 5,
                "ClientCount": 5,
                "TotalCount": 0,
                "CountOfReportSpanPerDay": 0,
                "AmountOfUsedStorage": 100,
                "Status": 2,
                "Region": "ap-guangzhou",
                "ErrRateThreshold": 5,
                "SampleRate": 100,
                "ErrorSample": 1,
                "SlowRequestSavedThreshold": 500,
                "SpanDailyCounters": 0,
                "BillingInstance": 1,
                "MetricDuration": 30,
                "LogSource": "",
                "LogRegion": "",
                "IsRelatedLog": 0,
                "LogTopicID": "",
                "LogSet": ""
            }
        ],
        "RequestId": "7uv7qo2mmm1e3ao94113zuvm2sehp7mm"
    }
}
```

