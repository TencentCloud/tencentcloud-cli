**Example 1: 修改云原生API网关实例分组基础信息**

修改云原生API网关实例分组基础信息

Input: 

```
tccli tse ModifyNativeGatewayServerGroup --cli-unfold-argument  \
    --GatewayId <GatewayId> \
    --Name <Name> \
    --Description <Description> \
    --GroupId <GroupId>
```

Output: 
```
{
    "Response": {
        "RequestId": "9922cab4-4ad3-4146-9535-cbc788082899"
    }
}
```

