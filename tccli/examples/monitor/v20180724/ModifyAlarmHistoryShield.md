**Example 1: 测试**

测试

Input: 

```
tccli monitor ModifyAlarmHistoryShield --cli-unfold-argument  \
    --Module xyz \
    --Name exampleName \
    --MonitorType exampleMonitorType \
    --NameSpace exampleNamespace \
    --ShieldObject exampleObject \
    --ShieldPolicyId examplePolicyId \
    --ShieldId shield-xxx \
    --ShieldTimeType exampleTimeType \
    --StartTime 1620000000 \
    --EndTime 1620003600 \
    --LoopStartDate 1620000000 \
    --LoopEndDate 1620003600 \
    --ShieldAlarmLevel high \
    --TimeZone 8 \
    --MetricName exampleMetricName
```

Output: 
```
{
    "Response": {
        "RequestId": "55591ca4-f797-43ac-b1af-3b09ca24091f"
    }
}
```

