**Example 1: 更新弹性伸缩策略**

更新弹性伸缩策略

Input: 

```
tccli tse ModifyAutoScalerResourceStrategy --cli-unfold-argument  \
    --GatewayId gateway-4a34cf5f \
    --StrategyId strategy-7bb4fcb0 \
    --StrategyName strategy-test \
    --Description desc \
    --MaxReplicas 5 \
    --Config.Metrics.0.Type Resource \
    --Config.Metrics.0.ResourceName cpu \
    --Config.Metrics.0.TargetType Utilization \
    --Config.Metrics.0.TargetValue 80 \
    --CronScalerConfig.Enabled True \
    --CronScalerConfig.Params.0.Period 1 * * \
    --CronScalerConfig.Params.0.StartAt 17:00 \
    --CronScalerConfig.Params.0.TargetReplicas 10
```

Output: 
```
{
    "Response": {
        "RequestId": "adc44984-762c-42e0-b39a-80777e5c3bcc",
        "Result": true
    }
}
```

