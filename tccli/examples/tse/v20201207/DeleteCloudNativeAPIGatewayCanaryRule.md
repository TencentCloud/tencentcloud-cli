**Example 1: 删除灰度规则**

删除灰度规则

Input: 

```
tccli tse DeleteCloudNativeAPIGatewayCanaryRule --cli-unfold-argument  \
    --GatewayId gateway-xxx \
    --ServiceId xxxx \
    --Priority 10
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

