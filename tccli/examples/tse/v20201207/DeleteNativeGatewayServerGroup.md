**Example 1: 删除网关实例分组**

删除网关实例分组

Input: 

```
tccli tse DeleteNativeGatewayServerGroup --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --GroupId group-4se0czf7
```

Output: 
```
{
    "Response": {
        "Result": {
            "GatewayId": "gateway-dde03767",
            "GroupId": "group-4se0czf7",
            "Status": "Deleting",
            "TaskId": "task-z31df1dz"
        },
        "RequestId": "ffadafb6-545d-461c-ad8c-baa26c0f8955"
    }
}
```

