**Example 1: 编辑云原生API网关实例规格示例**

修改云原生API网关实例规格

Input: 

```
tccli tse UpdateCloudNativeAPIGatewaySpec --cli-unfold-argument  \
    --GatewayId gateway-xxxx1234 \
    --GroupId abc \
    --NodeConfig.Specification abc \
    --NodeConfig.Number 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "GatewayId": "gateway-xxxx1234",
            "Status": "Updating",
            "TaskId": "task-xxxx1234"
        },
        "RequestId": "abc"
    }
}
```

