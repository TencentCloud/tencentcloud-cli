**Example 1: 编辑灰度规则**

编辑灰度规则

Input: 

```
tccli tse ModifyCloudNativeAPIGatewayCanaryRule --cli-unfold-argument  \
    --GatewayId gateway-xxx \
    --ServiceId xxx \
    --Priority 10 \
    --CanaryRule.Priority 20 \
    --CanaryRule.Enabled True \
    --CanaryRule.ConditionList.0.Type body \
    --CanaryRule.ConditionList.0.Key b1 \
    --CanaryRule.ConditionList.0.Operator == \
    --CanaryRule.ConditionList.0.Value abc \
    --CanaryRule.BalancedServiceList.0.ServiceID xxx \
    --CanaryRule.BalancedServiceList.0.ServiceName abc \
    --CanaryRule.BalancedServiceList.0.UpstreamName  \
    --CanaryRule.BalancedServiceList.0.Percent 10
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

