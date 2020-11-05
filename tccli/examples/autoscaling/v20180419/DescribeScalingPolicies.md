**Example 1: Querying alarm trigger policies**



Input: 

```
tccli as DescribeScalingPolicies --cli-unfold-argument  \
    --AutoScalingPolicyIds asp-5zffv598
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ScalingPolicySet": [
            {
                "AutoScalingGroupId": "asg-gbqa1n66",
                "AutoScalingPolicyId": "asp-5zffv598",
                "Cooldown": 100,
                "ScalingPolicyName": "cpu-test",
                "AdjustmentType": "CHANGE_IN_CAPACITY",
                "MetricAlarm": {
                    "Period": 60,
                    "ContinuousTime": 5,
                    "ComparisonOperator": "GREATER_THAN_OR_EQUAL_TO",
                    "Statistic": "AVERAGE",
                    "Threshold": 60,
                    "MetricName": "CPU_UTILIZATION"
                },
                "NotificationUserGroupIds": [],
                "AdjustmentValue": 10
            }
        ],
        "RequestId": "351dd0ef-27bc-4312-9287-48cd0835274b"
    }
}
```

