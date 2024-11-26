**Example 1: 编辑云原生API网关实例规格示例**

修改云原生API网关实例规格

Input: 

```
tccli tse UpdateCloudNativeAPIGatewaySpec --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --GroupId group-4se0czf7 \
    --NodeConfig.Specification 1c2g \
    --NodeConfig.Number 5
```

Output: 
```
{
    "Response": {
        "Result": {
            "GatewayId": "gateway-dde03767",
            "Status": "Updating",
            "TaskId": "task-z31df1dz"
        },
        "RequestId": "ffadafb6-545d-461c-ad8c-baa26c0f8955"
    }
}
```

