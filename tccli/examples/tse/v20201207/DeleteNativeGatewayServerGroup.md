**Example 1: 删除网关实例分组**

删除网关实例分组

Input: 

```
tccli tse DeleteNativeGatewayServerGroup --cli-unfold-argument  \
    --GatewayId gateway-xxx \
    --GroupId group-xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "GatewayId": "abc",
            "GroupId": "abc",
            "Status": "abc",
            "TaskId": "abc"
        },
        "RequestId": "abc"
    }
}
```

