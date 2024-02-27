**Example 1: 添加扩缩容规则成功示例**



Input: 

```
tccli emr AddMetricScaleStrategy --cli-unfold-argument  \
    --InstanceId abc \
    --StrategyType 0 \
    --TimeAutoScaleStrategy.StrategyId 1 \
    --TimeAutoScaleStrategy.StrategyName abc \
    --TimeAutoScaleStrategy.IntervalTime 1 \
    --TimeAutoScaleStrategy.ScaleAction 1 \
    --TimeAutoScaleStrategy.ScaleNum 1 \
    --TimeAutoScaleStrategy.StrategyStatus 1 \
    --TimeAutoScaleStrategy.Priority 1 \
    --TimeAutoScaleStrategy.RetryValidTime 1 \
    --TimeAutoScaleStrategy.RepeatStrategy.RepeatType abc \
    --TimeAutoScaleStrategy.RepeatStrategy.DayRepeat.ExecuteAtTimeOfDay abc \
    --TimeAutoScaleStrategy.RepeatStrategy.DayRepeat.Step 1 \
    --TimeAutoScaleStrategy.RepeatStrategy.WeekRepeat.ExecuteAtTimeOfDay abc \
    --TimeAutoScaleStrategy.RepeatStrategy.WeekRepeat.DaysOfWeek 1 \
    --TimeAutoScaleStrategy.RepeatStrategy.MonthRepeat.ExecuteAtTimeOfDay abc \
    --TimeAutoScaleStrategy.RepeatStrategy.MonthRepeat.DaysOfMonthRange 1 \
    --TimeAutoScaleStrategy.RepeatStrategy.NotRepeat.ExecuteAt abc \
    --TimeAutoScaleStrategy.RepeatStrategy.Expire abc \
    --TimeAutoScaleStrategy.GraceDownFlag True \
    --TimeAutoScaleStrategy.GraceDownTime 0 \
    --TimeAutoScaleStrategy.Tags.0.TagKey abc \
    --TimeAutoScaleStrategy.Tags.0.TagValue abc \
    --TimeAutoScaleStrategy.ConfigGroupAssigned abc \
    --TimeAutoScaleStrategy.MeasureMethod abc \
    --TimeAutoScaleStrategy.TerminatePolicy abc \
    --TimeAutoScaleStrategy.MaxUse 0 \
    --TimeAutoScaleStrategy.SoftDeployInfo 0 \
    --TimeAutoScaleStrategy.ServiceNodeInfo 0 \
    --TimeAutoScaleStrategy.CompensateFlag 0 \
    --TimeAutoScaleStrategy.GroupId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "41ac1575-64fa-4e23-b6df-6c1f509dd528"
    }
}
```

