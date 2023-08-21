**Example 1: 测试删除云原生API网关实例**



Input: 

```
tccli tse DeleteCloudNativeAPIGateway --cli-unfold-argument  \
    --GatewayId <GatewayId>
```

Output: 
```
{
    "Response": {
        "RequestId": "9922cab4-4ad3-4146-9535-cbc788082899",
        "Result": {
            "GatewayId": "gateway-8d8b6b2d",
            "Status": "Deleting"
        }
    }
}
```

