**Example 1: 测试**

测试

Input: 

```
tccli monitor CreateAlarmHistoryShield --cli-unfold-argument  \
    --Module xyz \
    --Name exampleName \
    --MonitorType exampleMonitorType \
    --NameSpace exampleNamespace \
    --ShieldObject exampleObject \
    --ShieldPolicyId examplePolicyId \
    --ShieldMetric exampleMetric \
    --ShieldTimeType exampleTimeType \
    --StartTime 1620000000 \
    --EndTime 1620003600 \
    --LoopStartDate 1620000000 \
    --LoopEndDate 1620003600 \
    --ShieldAlarmLevel high \
    --Description This is an example description. \
    --TimeZone 8 \
    --MetricName exampleMetricName
```

Output: 
```
{
    "Response": {
        "RequestId": "83716565-3baf-4d13-b633-73707dd93d02",
        "ShieldId": "Shield-3ham9evt0k"
    }
}
```

