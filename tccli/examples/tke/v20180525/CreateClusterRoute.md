**Example 1: 创建集群路由**



Input: 

```
tccli tke CreateClusterRoute --cli-unfold-argument  \
    --RouteTableName MANAGED_CLUSTER \
    --DestinationCidrBlock 10.4.0.0/24 \
    --GatewayIp 10.0.0.3
```

Output: 
```
{
    "Response": {
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

