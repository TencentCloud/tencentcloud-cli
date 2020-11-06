**Example 1: Modifying an alarm trigger policy**



Input: 

```
tccli as ModifyScalingPolicy --cli-unfold-argument  \
    --AutoScalingPolicyId asp-iir70sxv \
    --ScalingPolicyName cpu_policy_test \
    --AdjustmentType CHANGE_IN_CAPACITY \
    --AdjustmentValue 1 \
    --Cooldown 60 \
    --MetricAlarm.ComparisonOperator GREATER_THAN \
    --MetricAlarm.MetricName CPU_USAGE \
    --MetricAlarm.Statistic AVERAGE \
    --MetricAlarm.Threshold 50 \
    --MetricAlarm.Period 60 \
    --MetricAlarm.ContinuousTime 5 \
    --NotificationUserGroupIds 1678
```

Output: 
```
{
    "Response": {
        "RequestId": "91413a64-9587-486b-aef4-9aba5e8a0068"
    }
}
```

