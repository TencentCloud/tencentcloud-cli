**Example 1: 获取应用配置**

获取应用配置

Input: 

```
tccli apm DescribeApmApplicationConfig --cli-unfold-argument  \
    --InstanceId apm-eDyXPD6FF \
    --ServiceName java-order-service
```

Output: 
```
{
    "Response": {
        "ApmAppConfig": {
            "AgentEnable": true,
            "AgentOperationConfigView": {
                "IgnoreOperation": "",
                "RetentionOperation": "",
                "RetentionValid": false
            },
            "Components": "io.opentelemetry.tomcat-10.0",
            "DashboardTopicID": "",
            "DisableCpuUsed": 0,
            "DisableMemoryUsed": 0,
            "EnableDashboardConfig": false,
            "EnableLogConfig": true,
            "EnableSecurityConfig": false,
            "EnableSnapshot": false,
            "ErrorCodeFilter": "",
            "EventEnable": false,
            "ExceptionFilter": "",
            "IgnoreOperationName": "",
            "InstanceKey": "apm-eDyXPD6FF",
            "InstrumentList": [
                {
                    "Enable": true,
                    "Name": "apm-spring-annotations"
                }
            ],
            "IsDeleteAnyFileAnalysis": 0,
            "IsDeserializationAnalysis": 0,
            "IsDirectoryTraversalAnalysis": 0,
            "IsExpressionInjectionAnalysis": 0,
            "IsIncludeAnyFileAnalysis": 0,
            "IsInstrumentationVulnerabilityScan": 0,
            "IsJNDIInjectionAnalysis": 0,
            "IsJNIInjectionAnalysis": 0,
            "IsMemoryHijackingAnalysis": 0,
            "IsReadAnyFileAnalysis": 0,
            "IsRelatedDashboard": 0,
            "IsRelatedLog": 1,
            "IsRemoteCommandExecutionAnalysis": 0,
            "IsScriptEngineInjectionAnalysis": 0,
            "IsSqlInjectionAnalysis": 0,
            "IsTemplateEngineInjectionAnalysis": 0,
            "IsUploadAnyFileAnalysis": 0,
            "IsWebshellBackdoorAnalysis": 0,
            "LogIndexType": 0,
            "LogRegion": "ap-guangzhou",
            "LogSet": "",
            "LogSource": "",
            "LogTopicID": "cbfe8676-9251-4915-a4ea-92d7f905da63",
            "LogTraceIdKey": "",
            "ServiceID": "svc-ELHkoErzzc",
            "ServiceName": "java-order-service",
            "SnapshotTimeout": 500,
            "TraceRateLimit": 0,
            "TraceSquash": true,
            "UrlAutoConvergenceEnable": false,
            "UrlConvergence": "",
            "UrlConvergenceSwitch": 0,
            "UrlConvergenceThreshold": 0,
            "UrlExclude": "",
            "UrlLongSegmentThreshold": 40,
            "UrlNumberSegmentThreshold": 5
        },
        "RequestId": "9c2b84d6-c0e8-4bd2-8094-b4d427308397"
    }
}
```

