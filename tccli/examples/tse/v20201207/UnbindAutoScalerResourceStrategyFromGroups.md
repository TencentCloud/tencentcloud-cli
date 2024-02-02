**Example 1: 弹性伸缩策略批量解绑网关分组**



Input: 

```
tccli tse UnbindAutoScalerResourceStrategyFromGroups --cli-unfold-argument  \
    --GatewayId <GatewayId> \
    --StrategyId strategy-7bb4fcb0 \
    --GroupIds group-2e781178
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

