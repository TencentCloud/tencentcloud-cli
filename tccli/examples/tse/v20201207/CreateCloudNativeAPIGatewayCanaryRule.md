**Example 1: 创建灰度规则**

创建灰度规则

Input: 

```
tccli tse CreateCloudNativeAPIGatewayCanaryRule --cli-unfold-argument  \
    --GatewayId gateway-xxx \
    --ServiceId xxxx \
    --CanaryRule.Priority 10 \
    --CanaryRule.Enabled True \
    --CanaryRule.ConditionList.0.Type query \
    --CanaryRule.ConditionList.0.Key q1 \
    --CanaryRule.ConditionList.0.Operator == \
    --CanaryRule.ConditionList.0.Value xxx \
    --CanaryRule.BalancedServiceList.0.ServiceID xxxx \
    --CanaryRule.BalancedServiceList.0.ServiceName xxxx \
    --CanaryRule.BalancedServiceList.0.UpstreamName  \
    --CanaryRule.BalancedServiceList.0.Percent 100
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

