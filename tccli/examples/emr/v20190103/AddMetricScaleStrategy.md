**Example 1: 添加扩缩容规则成功示例**



Input: 

```
tccli emr AddMetricScaleStrategy --cli-unfold-argument  \
    --InstanceId emr-123 \
    --StrategyType 0 \
    --LoadAutoScaleStrategy.CalmDownTime 0 \
    --LoadAutoScaleStrategy.ConfigGroupAssigned {"HDFS-3.2.2":-1,"YARN-3.2.2":-1} \
    --LoadAutoScaleStrategy.GraceDownFlag False \
    --LoadAutoScaleStrategy.LoadMetricsConditions.LoadMetrics.0.Conditions.0.CompareMethod 1 \
    --LoadAutoScaleStrategy.LoadMetricsConditions.LoadMetrics.0.Conditions.0.Threshold 0 \
    --LoadAutoScaleStrategy.LoadMetricsConditions.LoadMetrics.0.LoadMetrics AvailableMB#root \
    --LoadAutoScaleStrategy.LoadMetricsConditions.LoadMetrics.0.MetricId 3 \
    --LoadAutoScaleStrategy.LoadMetricsConditions.LoadMetrics.0.StatisticPeriod 60 \
    --LoadAutoScaleStrategy.LoadMetricsConditions.LoadMetrics.0.TriggerThreshold 1 \
    --LoadAutoScaleStrategy.Priority 0 \
    --LoadAutoScaleStrategy.MeasureMethod INSTANCE \
    --LoadAutoScaleStrategy.ScaleAction 2 \
    --LoadAutoScaleStrategy.ScaleNum 1 \
    --LoadAutoScaleStrategy.StrategyName 并行负载-re04 \
    --LoadAutoScaleStrategy.StrategyStatus 1 \
    --TimeAutoScaleStrategy.CompensateFlag 0 \
    --TimeAutoScaleStrategy.ConfigGroupAssigned {"HDFS-3.2.2":-1,"YARN-3.2.2":-1} \
    --TimeAutoScaleStrategy.GraceDownFlag False \
    --TimeAutoScaleStrategy.GroupId 27 \
    --TimeAutoScaleStrategy.IntervalTime 0 \
    --TimeAutoScaleStrategy.MeasureMethod INSTANCE \
    --TimeAutoScaleStrategy.RepeatStrategy.Expire 2025-11-05 23:59:59 \
    --TimeAutoScaleStrategy.RepeatStrategy.NotRepeat.ExecuteAt 2024-11-05 14:43:00 \
    --TimeAutoScaleStrategy.RepeatStrategy.RepeatType NONE \
    --TimeAutoScaleStrategy.Priority 0 \
    --TimeAutoScaleStrategy.RetryValidTime 60 \
    --TimeAutoScaleStrategy.ScaleAction 1 \
    --TimeAutoScaleStrategy.ScaleNum 10 \
    --TimeAutoScaleStrategy.ServiceNodeInfo 7 \
    --TimeAutoScaleStrategy.SoftDeployInfo 1 2 \
    --TimeAutoScaleStrategy.StrategyName add \
    --TimeAutoScaleStrategy.StrategyStatus 1 \
    --TimeAutoScaleStrategy.TerminatePolicy DEFAULT
```

Output: 
```
{
    "Response": {
        "RequestId": "e3f82d54-6fa6-49c2-a479-8d2f5cf77f91"
    }
}
```

