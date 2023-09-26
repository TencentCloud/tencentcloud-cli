**Example 1: 编辑灰度规则**

编辑灰度规则

Input: 

```
tccli tse ModifyCloudNativeAPIGatewayCanaryRule --cli-unfold-argument  \
    --GatewayId gateway-18f786a \
    --ServiceId 6abf620f-c6b9-4440-b90c-56c165225cfc \
    --Priority 10 \
    --CanaryRule.Priority 20 \
    --CanaryRule.Enabled True \
    --CanaryRule.ConditionList.0.Type body \
    --CanaryRule.ConditionList.0.Key b1 \
    --CanaryRule.ConditionList.0.Operator == \
    --CanaryRule.ConditionList.0.Value abc \
    --CanaryRule.BalancedServiceList.0.ServiceID 6abf620f-c6b9-4440-b90c-56c165225cfc \
    --CanaryRule.BalancedServiceList.0.ServiceName svc1 \
    --CanaryRule.BalancedServiceList.0.UpstreamName  \
    --CanaryRule.BalancedServiceList.0.Percent 10
```

Output: 
```
{
    "Response": {
        "RequestId": "741e4e82-371d-48de-a843-867c69ff114d"
    }
}
```

