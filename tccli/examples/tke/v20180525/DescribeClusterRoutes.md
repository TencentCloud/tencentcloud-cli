**Example 1: 查询集群路由**



Input: 

```
tccli tke DescribeClusterRoutes --cli-unfold-argument  \
    --RouteTableName MANAGED_CLUSTER
```

Output: 
```
{
    "Response": {
        "RouteSet": [
            {
                "RouteTableName": "MANAGED_CLUSTER",
                "DestinationCidrBlock": "10.4.0.0/24",
                "GatewayIp": "10.0.0.3"
            }
        ],
        "TotalCount": 1,
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

