**Example 1: 修改弹性伸缩策略组合**

修改弹性伸缩策略组合

Input: 

```
tccli tem ModifyApplicationAutoscaler --cli-unfold-argument  \
    --SourceChannel 0 \
    --AutoscalerId xx \
    --Autoscaler.ModifyDate xx \
    --Autoscaler.Description xx \
    --Autoscaler.CronHorizontalAutoscaler.0.Priority 0 \
    --Autoscaler.CronHorizontalAutoscaler.0.Schedules.0.StartAt xx \
    --Autoscaler.CronHorizontalAutoscaler.0.Schedules.0.TargetReplicas 0 \
    --Autoscaler.CronHorizontalAutoscaler.0.Enabled True \
    --Autoscaler.CronHorizontalAutoscaler.0.Period xx \
    --Autoscaler.CronHorizontalAutoscaler.0.Name xx \
    --Autoscaler.MinReplicas 0 \
    --Autoscaler.AutoscalerId xx \
    --Autoscaler.Enabled True \
    --Autoscaler.HorizontalAutoscaler.0.MinReplicas 0 \
    --Autoscaler.HorizontalAutoscaler.0.Metrics xx \
    --Autoscaler.HorizontalAutoscaler.0.Enabled True \
    --Autoscaler.HorizontalAutoscaler.0.Threshold 0 \
    --Autoscaler.HorizontalAutoscaler.0.MaxReplicas 0 \
    --Autoscaler.EnableDate xx \
    --Autoscaler.AutoscalerName xx \
    --Autoscaler.CreateDate xx \
    --Autoscaler.MaxReplicas 0 \
    --ApplicationId xx \
    --EnvironmentId xx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "xx"
    }
}
```

