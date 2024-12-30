**Example 1: 拉取 APM 业务系统列表**

拉取 APM 业务系统列表

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
                "Name": "ss1123",
                "InstanceId": "zE7Yu-g7R",
                "Description": "ssd",
                "TraceDuration": 3,
                "AppId": 251005942,
                "CreateUin": "1500000686",
                "Tags": [],
                "ServiceCount": 0,
                "ClientCount": 0,
                "TotalCount": 0,
                "CountOfReportSpanPerDay": 0,
                "AmountOfUsedStorage": 100,
                "Status": 2,
                "Region": "ap-guangzhou",
                "ErrRateThreshold": 5,
                "SampleRate": 100,
                "ErrorSample": 0,
                "SlowRequestSavedThreshold": 500,
                "SpanDailyCounters": 1,
                "BillingInstance": 0,
                "MetricDuration": 30,
                "CustomShowTags": [],
                "PayMode": 1,
                "PayModeEffective": true,
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

