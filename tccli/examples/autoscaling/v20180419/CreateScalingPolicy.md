**Example 1: Increasing the desired capacity by one if the average CPU utilization is over 50% within 1 minute for 5 consecutive occurrences**



Input: 

```
tccli as CreateScalingPolicy --cli-unfold-argument  \
    --AutoScalingGroupId asg-12wjuh0s\
    --ScalingPolicyName cpu_policy_test\
    --AdjustmentType ' CHANGE_IN_CAPACITY'\
    --AdjustmentValue 1\
    --Cooldown 60\
    --MetricAlarm.ComparisonOperator GREATER_THAN\
    --MetricAlarm.MetricName CPU_UTILIZATION\
    --MetricAlarm.Statistic AVERAGE\
    --MetricAlarm.Threshold 50\
    --MetricAlarm.Period 60\
    --MetricAlarm.ContinuousTime 5\
    --NotificationUserGroupIds 1678
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

**Example 2: Removing 50% instances if the average memory utilization is below 35% within 1 minute for 5 consecutive occurrences**



Input: 

```
tccli as CreateScalingPolicy --cli-unfold-argument  \
    --AutoScalingGroupId asg-12wjuh0s\
    --ScalingPolicyName mem_policy_test\
    --AdjustmentType ' PERCENT_CHANGE_IN_CAPACITY'\
    --AdjustmentValue -50\
    --Cooldown 300\
    --MetricAlarm.ComparisonOperator LESS_THAN\
    --MetricAlarm.MetricName MEM_UTILIZATION\
    --MetricAlarm.Statistic AVERAGE\
    --MetricAlarm.Threshold 50\
    --MetricAlarm.Period 60\
    --MetricAlarm.ContinuousTime 5\
    --NotificationUserGroupIds 1678
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

