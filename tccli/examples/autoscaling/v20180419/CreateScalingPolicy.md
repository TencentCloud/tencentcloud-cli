**Example 1: 创建简单策略： CPU 平均利用率**

1分钟内，CPU平均利用率大于50%，连续发生5次，期望实例数增加1。

Input: 

```
tccli as CreateScalingPolicy --cli-unfold-argument  \
    --AutoScalingGroupId asg-12wjuh0s \
    --Cooldown 60 \
    --ScalingPolicyType SIMPLE \
    --ScalingPolicyName cpu_policy_test \
    --AdjustmentType  CHANGE_IN_CAPACITY \
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
        "AutoScalingPolicyId": "asp-iir70sxv",
        "RequestId": "fb02c8bd-5f38-4786-91b6-0c6e06a88832"
    }
}
```

**Example 2: 创建简单策略：内存平均利用率**

1分钟内，内存平均利用率小于35%，连续发生5次，减少50%实例。

Input: 

```
tccli as CreateScalingPolicy --cli-unfold-argument  \
    --AutoScalingGroupId asg-12wjuh0s \
    --Cooldown 300 \
    --ScalingPolicyType SIMPLE \
    --ScalingPolicyName mem_policy_test \
    --AdjustmentType  PERCENT_CHANGE_IN_CAPACITY \
    --MetricAlarm.Period 60 \
    --MetricAlarm.ContinuousTime 5 \
    --MetricAlarm.ComparisonOperator LESS_THAN \
    --MetricAlarm.Statistic AVERAGE \
    --MetricAlarm.Threshold 50 \
    --MetricAlarm.MetricName MEM_UTILIZATION \
    --NotificationUserGroupIds 1678 \
    --AdjustmentValue -50
```

Output: 
```
{
    "Response": {
        "AutoScalingPolicyId": "asp-f59pppuh",
        "RequestId": "116213d6-2269-44cc-af76-c4a8dc7dbdf9"
    }
}
```

**Example 3: 创建目标追踪策略：CPU 平均利用率**

保持伸缩组 CPU 平均利用率接近60%，告警触发的扩容实例预热300秒，关闭禁用缩容。

Input: 

```
tccli as CreateScalingPolicy --cli-unfold-argument  \
    --AutoScalingGroupId asg-9dn1a5y6 \
    --ScalingPolicyName cpu_target_tracking_test \
    --ScalingPolicyType TARGET_TRACKING \
    --PredefinedMetricType ASG_AVG_CPU_UTILIZATION \
    --EstimatedInstanceWarmup 300 \
    --DisableScaleIn False \
    --TargetValue 60
```

Output: 
```
{
    "Response": {
        "AutoScalingPolicyId": "asp-ljr51ssq",
        "RequestId": "58a8ac17-e864-4bf6-81c7-c5dc63b0057d"
    }
}
```

