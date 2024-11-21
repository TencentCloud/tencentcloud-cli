**Example 1: 编辑定时任务**



Input: 

```
tccli tcss ModifyCompliancePeriodTask --cli-unfold-argument  \
    --PeriodTaskId 1001 \
    --PeriodRule.ExecutionTime 04:00:00 \
    --PeriodRule.Frequency 1 \
    --StandardSettings.0.StandardId 1001 \
    --StandardSettings.0.Enable False
```

Output: 
```
{
    "Response": {
        "RequestId": "8a64a4f9-864c-49c6-adcb-21b483de477a"
    }
}
```

