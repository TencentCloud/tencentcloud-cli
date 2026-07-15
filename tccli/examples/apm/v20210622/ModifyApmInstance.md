**Example 1: 示例**



Input: 

```
tccli apm ModifyApmInstance --cli-unfold-argument  \
    --InstanceId apm-UUGYsY6rL \
    --Name test-for-access \
    --Tags.0.Key 负责人 \
    --Tags.0.Value leonnchen \
    --Tags.1.Key 运营产品 \
    --Tags.1.Value 云监控产品 \
    --Tags.2.Key 运营部门 \
    --Tags.2.Value 云监控产品中心_1120 \
    --TraceDuration 7 \
    --SpanDailyCounters 0 \
    --ErrRateThreshold 5 \
    --SlowRequestSavedThreshold 500 \
    --ErrorSample 1 \
    --IsRelatedLog 0 \
    --LogTopicID  \
    --LogRegion  \
    --PayMode 0 \
    --ResponseDurationWarningThreshold 500 \
    --IsInstrumentationVulnerabilityScan 1 \
    --IsSqlInjectionAnalysis 1 \
    --IsRelatedDashboard 0 \
    --DashboardTopicID  \
    --Free 0 \
    --LogTraceIdKey  \
    --IsRemoteCommandExecutionAnalysis 0 \
    --IsMemoryHijackingAnalysis 0 \
    --IsTemplateEngineInjectionAnalysis 0 \
    --IsScriptEngineInjectionAnalysis 0 \
    --IsExpressionInjectionAnalysis 0 \
    --IsJNDIInjectionAnalysis 0 \
    --IsJNIInjectionAnalysis 0 \
    --IsWebshellBackdoorAnalysis 0 \
    --IsDeserializationAnalysis 0 \
    --IsDeleteAnyFileAnalysis 0 \
    --IsReadAnyFileAnalysis 0 \
    --IsUploadAnyFileAnalysis 0 \
    --IsIncludeAnyFileAnalysis 0 \
    --IsDirectoryTraversalAnalysis 0 \
    --UrlLongSegmentThreshold 40 \
    --UrlNumberSegmentThreshold 5 \
    --LogSpanIdKey  \
    --EnableHeadSampler True \
    --HeadSamplerArg 12 \
    --HeadSamplerType parentbased_traceidratio
```

Output: 
```
{
    "Response": {
        "RequestId": "1c728538-41ba-486d-ae09-60dd08183e46"
    }
}
```

