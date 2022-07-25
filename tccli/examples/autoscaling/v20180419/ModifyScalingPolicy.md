**Example 1: 修改告警触发策略**



Input: 

```
tccli as ModifyScalingPolicy --cli-unfold-argument  \
    --AutoScalingPolicyId asp-iir70sxv \
    --Cooldown 60 \
    --ScalingPolicyName cpu_policy_test \
    --AdjustmentType CHANGE_IN_CAPACITY \
    --MetricAlarm.Period 60 \
    --MetricAlarm.ContinuousTime 5 \
    --MetricAlarm.ComparisonOperator GREATER_THAN \
    --MetricAlarm.Statistic AVERAGE \
    --MetricAlarm.Threshold 50 \
    --MetricAlarm.MetricName CPU_USAGE \
    --NotificationUserGroupIds 1678 \
    --AdjustmentValue 1
```

Output: 
```
{
    "Response": {
        "RequestId": "91413a64-9587-486b-aef4-9aba5e8a0068"
    }
}
```

