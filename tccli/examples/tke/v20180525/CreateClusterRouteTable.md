**Example 1: 创建集群路由表**



Input: 

```
tccli tke CreateClusterRouteTable --cli-unfold-argument  \
    --RouteTableName MANAGED_CLUSTER \
    --RouteTableCidrBlock 10.4.0.0/16 \
    --VpcId vpc-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

