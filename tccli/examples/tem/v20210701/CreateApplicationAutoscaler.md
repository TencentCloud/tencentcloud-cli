**Example 1: 创建弹性伸缩策略组合**

创建弹性伸缩策略组合

Input: 

```
tccli tem CreateApplicationAutoscaler --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --SourceChannel 0 \
    --EnvironmentId en-xxxxxx \
    --Autoscaler.MinReplicas 0 \
    --Autoscaler.MaxReplicas 0 \
    --Autoscaler.HorizontalAutoscaler.0.MinReplicas 0 \
    --Autoscaler.HorizontalAutoscaler.0.MaxReplicas 0 \
    --Autoscaler.HorizontalAutoscaler.0.Metrics abc \
    --Autoscaler.HorizontalAutoscaler.0.Threshold 0 \
    --Autoscaler.HorizontalAutoscaler.0.Enabled True \
    --Autoscaler.HorizontalAutoscaler.0.DoubleThreshold 0 \
    --Autoscaler.CronHorizontalAutoscaler.0.Name abc \
    --Autoscaler.CronHorizontalAutoscaler.0.Period abc \
    --Autoscaler.CronHorizontalAutoscaler.0.Schedules.0.StartAt abc \
    --Autoscaler.CronHorizontalAutoscaler.0.Schedules.0.TargetReplicas 0 \
    --Autoscaler.CronHorizontalAutoscaler.0.Enabled True \
    --Autoscaler.CronHorizontalAutoscaler.0.Priority 0 \
    --Autoscaler.AutoscalerId abc \
    --Autoscaler.AutoscalerName abc \
    --Autoscaler.Description abc \
    --Autoscaler.CreateDate abc \
    --Autoscaler.ModifyDate abc \
    --Autoscaler.EnableDate abc \
    --Autoscaler.Enabled True
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

