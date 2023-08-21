**Example 1: 测试修改云原生API网关实例基础信息**

测试修改云原生API网关实例基础信息

Input: 

```
tccli tse ModifyCloudNativeAPIGateway --cli-unfold-argument  \
    --GatewayId <GatewayId> \
    --Name <Name> \
    --Description <Description>
```

Output: 
```
{
    "Response": {
        "RequestId": "9922cab4-4ad3-4146-9535-cbc788082899"
    }
}
```

