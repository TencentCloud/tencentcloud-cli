**Example 1: 重启网关实例节点**

重启网关实例节点

Input: 

```
tccli tse RestartNativeGatewayInstanceNode --cli-unfold-argument  \
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

