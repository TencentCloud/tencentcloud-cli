**Example 1: 修改简单类型告警触发策略**

指定策略ID，修改简单策略相关属性。

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
    --MetricAlarm.MetricName CPU_UTILIZATION \
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

**Example 2: 修改目标追踪类型告警触发策略**

指定策略ID，修改目标追踪策略相关属性。

Input: 

```
tccli as ModifyScalingPolicy --cli-unfold-argument  \
    --AutoScalingPolicyId asp-9uroe7ta \
    --ScalingPolicyName target-trackiing-test-policy \
    --DisableScaleIn False \
    --EstimatedInstanceWarmup 300 \
    --TargetValue 60 \
    --PredefinedMetricType ASG_AVG_CPU_UTILIZATION
```

Output: 
```
{
    "Response": {
        "RequestId": "881a6752-55e8-4485-878a-a80065732a9f"
    }
}
```

