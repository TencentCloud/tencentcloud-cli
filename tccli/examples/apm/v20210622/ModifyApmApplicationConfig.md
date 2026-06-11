**Example 1: 修改应用配置**



Input: 

```
tccli apm ModifyApmApplicationConfig --cli-unfold-argument  \
    --InstanceId apm-eDyXPD6FF \
    --ServiceName quote \
    --UrlConvergenceSwitch 0 \
    --ExceptionFilter  \
    --UrlConvergence  \
    --ErrorCodeFilter  \
    --UrlExclude  \
    --IsRelatedLog 0 \
    --LogRegion  \
    --LogTopicID  \
    --IgnoreOperationName  \
    --EnableSnapshot False \
    --SnapshotTimeout 2000 \
    --AgentEnable True \
    --TraceSquash True \
    --EventEnable False \
    --InstrumentList.0.Name apm-spring-annotations \
    --InstrumentList.0.Enable True \
    --AgentOperationConfigView.RetentionValid False \
    --AgentOperationConfigView.IgnoreOperation  \
    --AgentOperationConfigView.RetentionOperation  \
    --EnableLogConfig False \
    --EnableDashboardConfig False \
    --IsRelatedDashboard 0 \
    --DashboardTopicID  \
    --LogIndexType 0 \
    --LogTraceIdKey  \
    --EnableSecurityConfig False \
    --IsSqlInjectionAnalysis 0 \
    --IsInstrumentationVulnerabilityScan 0 \
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
    --DisableMemoryUsed 100 \
    --DisableCpuUsed 100 \
    --DbStatementParametersEnabled False \
    --SlowSQLThresholds.0.Key default \
    --SlowSQLThresholds.0.Value 2001 \
    --EnableDesensitizationRule 0 \
    --DesensitizationRule  \
    --LogSpanIdKey  \
    --AutoProfilingConfig.CpuProfilingEnable False \
    --AutoProfilingConfig.MemoryProfilingEnable False \
    --AutoProfilingConfig.CpuProfilingThreshold 80 \
    --AutoProfilingConfig.MemoryProfilingThreshold 80 \
    --AutoProfilingConfig.CpuProfilingDuration 60000 \
    --AutoProfilingConfig.MemoryProfilingDuration 60000 \
    --EnableThresholdConfig False \
    --ErrRateThreshold 5 \
    --ResponseDurationWarningThreshold 500 \
    --UseDefaultFuseConfig True
```

Output: 
```
{
    "Response": {
        "RequestId": "7f53b1e8-a093-4150-9720-a0d9e887d89f"
    }
}
```

