**Example 1: 修改扩缩容规则**

修改扩缩容规则

Input: 

```
tccli emr ModifyAutoScaleStrategy --cli-unfold-argument  \
    --InstanceId abc \
    --StrategyType 0 \
    --TimeAutoScaleStrategies.0.StrategyId 1 \
    --TimeAutoScaleStrategies.0.StrategyName abc \
    --TimeAutoScaleStrategies.0.IntervalTime 1 \
    --TimeAutoScaleStrategies.0.ScaleAction 1 \
    --TimeAutoScaleStrategies.0.ScaleNum 1 \
    --TimeAutoScaleStrategies.0.StrategyStatus 1 \
    --TimeAutoScaleStrategies.0.Priority 1 \
    --TimeAutoScaleStrategies.0.RetryValidTime 1 \
    --TimeAutoScaleStrategies.0.RepeatStrategy.RepeatType abc \
    --TimeAutoScaleStrategies.0.RepeatStrategy.DayRepeat.ExecuteAtTimeOfDay abc \
    --TimeAutoScaleStrategies.0.RepeatStrategy.DayRepeat.Step 1 \
    --TimeAutoScaleStrategies.0.RepeatStrategy.WeekRepeat.ExecuteAtTimeOfDay abc \
    --TimeAutoScaleStrategies.0.RepeatStrategy.WeekRepeat.DaysOfWeek 1 \
    --TimeAutoScaleStrategies.0.RepeatStrategy.MonthRepeat.ExecuteAtTimeOfDay abc \
    --TimeAutoScaleStrategies.0.RepeatStrategy.MonthRepeat.DaysOfMonthRange 1 \
    --TimeAutoScaleStrategies.0.RepeatStrategy.NotRepeat.ExecuteAt abc \
    --TimeAutoScaleStrategies.0.RepeatStrategy.Expire abc \
    --TimeAutoScaleStrategies.0.GraceDownFlag True \
    --TimeAutoScaleStrategies.0.GraceDownTime 0 \
    --TimeAutoScaleStrategies.0.Tags.0.TagKey abc \
    --TimeAutoScaleStrategies.0.Tags.0.TagValue abc \
    --TimeAutoScaleStrategies.0.ConfigGroupAssigned abc \
    --TimeAutoScaleStrategies.0.MeasureMethod abc \
    --TimeAutoScaleStrategies.0.TerminatePolicy abc \
    --TimeAutoScaleStrategies.0.MaxUse 0 \
    --TimeAutoScaleStrategies.0.SoftDeployInfo 0 \
    --TimeAutoScaleStrategies.0.ServiceNodeInfo 0 \
    --TimeAutoScaleStrategies.0.CompensateFlag 0
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

**Example 2: 修改扩缩容规则成功示例**

修改扩缩容规则

Input: 

```
tccli emr ModifyAutoScaleStrategy --cli-unfold-argument  \
    --InstanceId emr-3ap64zl6 \
    --StrategyType 1 \
    --LoadAutoScaleStrategies.0.StrategyId 52 \
    --LoadAutoScaleStrategies.0.ScaleNum 4 \
    --LoadAutoScaleStrategies.0.ScaleAction 2 \
    --LoadAutoScaleStrategies.0.Priority 1
```

Output: 
```
{
    "Response": {
        "RequestId": "23108dcf-506a-4246-b0bf-dca8ef2b0845"
    }
}
```

