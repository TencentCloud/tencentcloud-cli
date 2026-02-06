**Example 1: 成功示例**



Input: 

```
tccli apm ModifyApmApplicationConfig --cli-unfold-argument  \
    --InstanceId apm-oJ7C40jYv \
    --ServiceName springboot-service \
    --UrlConvergenceSwitch 0 \
    --UrlConvergenceThreshold 1000 \
    --ExceptionFilter  \
    --UrlConvergence  \
    --ErrorCodeFilter  \
    --UrlExclude  \
    --IsRelatedLog 0 \
    --LogRegion  \
    --LogTopicID  \
    --LogSet  \
    --LogSource CLS \
    --IgnoreOperationName abc
ccc \
    --EnableSnapshot True \
    --SnapshotTimeout 2000 \
    --AgentEnable True \
    --TraceSquash True \
    --EventEnable False \
    --InstrumentList.0.Name apm-spring-annotations \
    --InstrumentList.0.Enable True \
    --AgentOperationConfigView.RetentionValid False \
    --AgentOperationConfigView.IgnoreOperation /test \
    --AgentOperationConfigView.RetentionOperation  \
    --EnableLogConfig False \
    --EnableDashboardConfig False \
    --IsRelatedDashboard 0 \
    --DashboardTopicID  \
    --LogIndexType 0 \
    --LogTraceIdKey  \
    --EnableSecurityConfig False \
    --IsSqlInjectionAnalysis 1 \
    --IsInstrumentationVulnerabilityScan 1 \
    --IsRemoteCommandExecutionAnalysis 0 \
    --IsMemoryHijackingAnalysis 0 \
    --IsDeleteAnyFileAnalysis 0 \
    --IsReadAnyFileAnalysis 0 \
    --IsUploadAnyFileAnalysis 0 \
    --IsIncludeAnyFileAnalysis 0 \
    --IsDirectoryTraversalAnalysis 0 \
    --IsTemplateEngineInjectionAnalysis 0 \
    --IsScriptEngineInjectionAnalysis 0 \
    --IsExpressionInjectionAnalysis 0 \
    --IsJNDIInjectionAnalysis 0 \
    --IsJNIInjectionAnalysis 0 \
    --IsWebshellBackdoorAnalysis 0 \
    --IsDeserializationAnalysis 0 \
    --UrlAutoConvergenceEnable False \
    --UrlLongSegmentThreshold 40 \
    --UrlNumberSegmentThreshold 5 \
    --DisableMemoryUsed 60 \
    --DisableCpuUsed 60 \
    --DbStatementParametersEnabled True
```

Output: 
```
{
    "Response": {
        "RequestId": "1514d407-9a83-4569-a9c6-0be6b2d6b9ca"
    }
}
```

