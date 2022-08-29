**Example 1: 测试获取云原生API网关节点列表**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayNodes --cli-unfold-argument  \
    --GatewayId <GatewayId>
```

Output: 
```
{
    "Response": {
        "RequestId": "adc44984-762c-42e0-b39a-80777e5c3bcc",
        "Result": {
            "TotalCount": 1,
            "NodeList": [
                {
                    "NodeId": "kong-0",
                    "NodeIp": "172.16.0.40"
                }
            ]
        }
    }
}
```

