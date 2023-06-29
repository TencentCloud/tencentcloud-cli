**Example 1: 编辑定时任务**



Input: 

```
tccli tcss ModifyCompliancePeriodTask --cli-unfold-argument  \
    --PeriodTaskId 12345 \
    --PeriodRule.ExecutionTime 04:00:00 \
    --PeriodRule.Frequency 1 \
    --StandardSettings.0.StandardId 12345 \
    --StandardSettings.0.Enable False
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxx"
    }
}
```

