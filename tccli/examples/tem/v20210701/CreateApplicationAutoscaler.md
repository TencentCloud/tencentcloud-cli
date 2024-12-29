**Example 1: 创建弹性伸缩策略组合**

创建弹性伸缩策略组合

Input: 

```
tccli tem CreateApplicationAutoscaler --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --SourceChannel 0 \
    --EnvironmentId en-xxxxxx \
    --Autoscaler.MinReplicas 1 \
    --Autoscaler.MaxReplicas 3 \
    --Autoscaler.AutoscalerName pk-test-1 \
    --Autoscaler.Description 这是一个描述 \
    --Autoscaler.Enabled False \
    --Autoscaler.HorizontalAutoscaler.0.MinReplicas 1 \
    --Autoscaler.HorizontalAutoscaler.0.MaxReplicas 3 \
    --Autoscaler.HorizontalAutoscaler.0.Metrics CPU \
    --Autoscaler.HorizontalAutoscaler.0.DoubleThreshold 50 \
    --Autoscaler.HorizontalAutoscaler.0.Enabled True \
    --Autoscaler.CronHorizontalAutoscaler.0.Name policy-test \
    --Autoscaler.CronHorizontalAutoscaler.0.Period * * * \
    --Autoscaler.CronHorizontalAutoscaler.0.Schedules.0.StartAt 00:00 \
    --Autoscaler.CronHorizontalAutoscaler.0.Schedules.0.TargetReplicas 1 \
    --Autoscaler.CronHorizontalAutoscaler.0.Enabled True \
    --Autoscaler.CronHorizontalAutoscaler.0.Priority 0
```

Output: 
```
{
    "Response": {
        "Result": "scaler-xxxxxx",
        "RequestId": "ab-xx"
    }
}
```

