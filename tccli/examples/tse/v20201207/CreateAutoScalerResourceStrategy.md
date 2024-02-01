**Example 1: 创建弹性伸缩策略**

创建弹性伸缩策略

Input: 

```
tccli tse CreateAutoScalerResourceStrategy --cli-unfold-argument  \
    --GatewayId gateway-4a34cf5f \
    --StrategyName strategy-test \
    --Description desc \
    --MaxReplicas 15 \
    --Config.Enabled True \
    --Config.Metrics.0.Type Resource \
    --Config.Metrics.0.ResourceName cpu \
    --Config.Metrics.0.TargetType Utilization \
    --Config.Metrics.0.TargetValue 50 \
    --Config.Metrics.1.Type Pods \
    --Config.Metrics.1.ResourceName tcp-connection-num \
    --Config.Metrics.1.TargetType AverageValue \
    --Config.Metrics.1.TargetValue 5 \
    --CronScalerConfig.Enabled True \
    --CronScalerConfig.Params.0.Period 1 * * \
    --CronScalerConfig.Params.0.StartAt 17:00 \
    --CronScalerConfig.Params.0.TargetReplicas 10
```

Output: 
```
{
    "Response": {
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d",
        "Result": true
    }
}
```

