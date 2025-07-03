**Example 1: 获取 APM 业务系统列表**

获取 APM 业务系统列表

Input: 

```
tccli apm DescribeApmInstances --cli-unfold-argument  \
    --Tags.0.Key appId \
    --Tags.0.Value 251005942
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "AmountOfUsedStorage": 100,
                "AppId": 251005942,
                "BillingInstance": 0,
                "ClientCount": 0,
                "CountOfReportSpanPerDay": 0,
                "CreateUin": "1500000686",
                "CustomShowTags": [],
                "DashboardTopicID": "",
                "DefaultTSF": 0,
                "Description": "",
                "ErrRateThreshold": 5,
                "ErrorSample": 1,
                "Free": 2,
                "InstanceId": "apm-u6HNYVXhz",
                "IsDeleteAnyFileAnalysis": 1,
                "IsDeserializationAnalysis": 1,
                "IsDirectoryTraversalAnalysis": 1,
                "IsExpressionInjectionAnalysis": 1,
                "IsIncludeAnyFileAnalysis": 1,
                "IsInstrumentationVulnerabilityScan": 1,
                "IsJNDIInjectionAnalysis": 1,
                "IsJNIInjectionAnalysis": 1,
                "IsMemoryHijackingAnalysis": 1,
                "IsReadAnyFileAnalysis": 1,
                "IsRelatedDashboard": 0,
                "IsRelatedLog": 0,
                "IsRemoteCommandExecutionAnalysis": 1,
                "IsScriptEngineInjectionAnalysis": 1,
                "IsSqlInjectionAnalysis": 1,
                "IsTemplateEngineInjectionAnalysis": 1,
                "IsUploadAnyFileAnalysis": 1,
                "IsWebshellBackdoorAnalysis": 1,
                "LogIndexType": 0,
                "LogRegion": "",
                "LogSet": "",
                "LogSource": "",
                "LogTopicID": "",
                "LogTraceIdKey": "",
                "MetricDuration": 3,
                "Name": "test1",
                "PayMode": 0,
                "PayModeEffective": true,
                "Region": "ap-guangzhou",
                "ResponseDurationWarningThreshold": 500,
                "SampleRate": 100,
                "ServiceCount": 0,
                "SlowRequestSavedThreshold": 500,
                "SpanDailyCounters": 0,
                "Status": 1,
                "StopReason": 0,
                "Tags": [
                    {
                        "Key": "负责人",
                        "Value": "archerkang"
                    },
                    {
                        "Key": "运营产品",
                        "Value": "云监控产品"
                    },
                    {
                        "Key": "运营部门",
                        "Value": "/../../../../../../../../../../../../../../../../../../../../etc/./////.////.///.//./passwd"
                    }
                ],
                "TotalCount": 0,
                "TraceDuration": 7
            }
        ],
        "RequestId": "1afaff9e-88c9-4949-9c84-fd5eae88a88a"
    }
}
```

