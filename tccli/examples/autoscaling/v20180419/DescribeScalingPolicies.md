**Example 1: 查询简单策略**

指定策略ID查询简单类型告警触发策略

Input: 

```
tccli as DescribeScalingPolicies --cli-unfold-argument  \
    --AutoScalingPolicyIds asp-7mme2ule
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ScalingPolicySet": [
            {
                "EstimatedInstanceWarmup": null,
                "MetricAlarms": null,
                "AutoScalingGroupId": "asg-9dn1a5y6",
                "PredefinedMetricType": null,
                "ScalingPolicyType": "SIMPLE",
                "DisableScaleIn": null,
                "AutoScalingPolicyId": "asp-7mme2ule",
                "NotificationUserGroupIds": [],
                "Cooldown": 666,
                "ScalingPolicyName": "simple_policy_test",
                "AdjustmentType": "CHANGE_IN_CAPACITY",
                "MetricAlarm": {
                    "ComparisonOperator": "GREATER_THAN",
                    "Period": 60,
                    "ContinuousTime": 5,
                    "Threshold": 20,
                    "Statistic": "AVERAGE",
                    "PreciseThreshold": 20,
                    "MetricName": "CPU_UTILIZATION"
                },
                "TargetValue": null,
                "AdjustmentValue": 3
            }
        ],
        "RequestId": "297c6ed3-aa1c-43f4-be0f-10e513a86e6e"
    }
}
```

