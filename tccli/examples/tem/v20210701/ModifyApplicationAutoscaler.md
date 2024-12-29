**Example 1: 修改弹性伸缩策略组合**

修改弹性伸缩策略组合

Input: 

```
tccli tem ModifyApplicationAutoscaler --cli-unfold-argument  \
    --ApplicationId app-xxxxxx \
    --EnvironmentId en-xxxxxx \
    --AutoscalerId scaler-xxxxxx \
    --Autoscaler.MinReplicas 0 \
    --Autoscaler.MaxReplicas 4 \
    --Autoscaler.AutoscalerName pk-test-clb \
    --Autoscaler.Description  \
    --Autoscaler.Enabled False \
    --Autoscaler.HorizontalAutoscaler.0.MinReplicas 0 \
    --Autoscaler.HorizontalAutoscaler.0.MaxReplicas 4 \
    --Autoscaler.HorizontalAutoscaler.0.Metrics CPU \
    --Autoscaler.HorizontalAutoscaler.0.DoubleThreshold 50 \
    --Autoscaler.HorizontalAutoscaler.0.Enabled True \
    --Autoscaler.CronHorizontalAutoscaler.0.Name pk-test \
    --Autoscaler.CronHorizontalAutoscaler.0.Period * * * \
    --Autoscaler.CronHorizontalAutoscaler.0.Schedules.0.StartAt 02:00 \
    --Autoscaler.CronHorizontalAutoscaler.0.Schedules.0.TargetReplicas 1 \
    --Autoscaler.CronHorizontalAutoscaler.0.Enabled False \
    --Autoscaler.CronHorizontalAutoscaler.0.Priority 0
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abbd6b63-xxx-xxx-xxx"
    }
}
```

