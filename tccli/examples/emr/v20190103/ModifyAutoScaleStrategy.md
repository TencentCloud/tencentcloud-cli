**Example 1: 修改扩缩容规则**

修改扩缩容规则

Input: 

```
tccli emr ModifyAutoScaleStrategy --cli-unfold-argument  \
    --InstanceId emr-123 \
    --StrategyType 0 \
    --LoadAutoScaleStrategies.0.CalmDownTime 60 \
    --LoadAutoScaleStrategies.0.GraceDownFlag False \
    --LoadAutoScaleStrategies.0.GraceDownTime 0 \
    --LoadAutoScaleStrategies.0.GroupId 0 \
    --LoadAutoScaleStrategies.0.LoadMetricsConditions.LoadMetrics.0.Conditions.0.CompareMethod 1 \
    --LoadAutoScaleStrategies.0.LoadMetricsConditions.LoadMetrics.0.Conditions.0.Threshold 16 \
    --LoadAutoScaleStrategies.0.LoadMetricsConditions.LoadMetrics.0.LoadMetrics AvailableVCores#root.default \
    --LoadAutoScaleStrategies.0.LoadMetricsConditions.LoadMetrics.0.MetricId 1 \
    --LoadAutoScaleStrategies.0.LoadMetricsConditions.LoadMetrics.0.StatisticPeriod 60 \
    --LoadAutoScaleStrategies.0.LoadMetricsConditions.LoadMetrics.0.TriggerThreshold 1 \
    --LoadAutoScaleStrategies.0.MeasureMethod INSTANCE \
    --LoadAutoScaleStrategies.0.Priority 3 \
    --LoadAutoScaleStrategies.0.ProcessMethod 3 \
    --LoadAutoScaleStrategies.0.ScaleAction 2 \
    --LoadAutoScaleStrategies.0.ScaleNum 2 \
    --LoadAutoScaleStrategies.0.Soft yarn \
    --LoadAutoScaleStrategies.0.StrategyId 1521 \
    --LoadAutoScaleStrategies.0.StrategyName 负载缩容 \
    --LoadAutoScaleStrategies.0.StrategyStatus 3 \
    --TimeAutoScaleStrategies.0.CompensateFlag 1 \
    --TimeAutoScaleStrategies.0.ConfigGroupAssigned {"HDFS-2.8.5":-1,"YARN-2.8.5":-1} \
    --TimeAutoScaleStrategies.0.GraceDownFlag False \
    --TimeAutoScaleStrategies.0.GraceDownTime 0 \
    --TimeAutoScaleStrategies.0.GroupId 0 \
    --TimeAutoScaleStrategies.0.IntervalTime 0 \
    --TimeAutoScaleStrategies.0.MaxUse 8 \
    --TimeAutoScaleStrategies.0.MeasureMethod INSTANCE \
    --TimeAutoScaleStrategies.0.Priority 2 \
    --TimeAutoScaleStrategies.0.RepeatStrategy.Expire 2025-11-05 23:59:59 \
    --TimeAutoScaleStrategies.0.RepeatStrategy.NotRepeat.ExecuteAt 2024-11-06 09:10:00 \
    --TimeAutoScaleStrategies.0.RepeatStrategy.RepeatType NONE \
    --TimeAutoScaleStrategies.0.RetryValidTime 60 \
    --TimeAutoScaleStrategies.0.ScaleAction 1 \
    --TimeAutoScaleStrategies.0.ScaleNum 6 \
    --TimeAutoScaleStrategies.0.ServiceNodeInfo 7 \
    --TimeAutoScaleStrategies.0.SoftDeployInfo 1 2 \
    --TimeAutoScaleStrategies.0.StrategyId 1783 \
    --TimeAutoScaleStrategies.0.StrategyName 测试准实时任务扩容 \
    --TimeAutoScaleStrategies.0.StrategyStatus 3 \
    --TimeAutoScaleStrategies.0.Tags.0.TagKey group \
    --TimeAutoScaleStrategies.0.Tags.0.TagValue data \
    --TimeAutoScaleStrategies.0.TerminatePolicy TIMING
```

Output: 
```
{
    "Response": {
        "RequestId": "8833a2df-1487-4f78-89b6-eff26058a240"
    }
}
```

