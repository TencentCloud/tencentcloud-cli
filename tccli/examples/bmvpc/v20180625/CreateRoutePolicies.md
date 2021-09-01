**Example 1: 新增自定义的路由条目**

新增自定义的路由条目

Input: 

```
tccli bmvpc CreateRoutePolicies --cli-unfold-argument  \
    --RouteTableId rtb-19yps3nz \
    --RoutePolicySet.0.DestinationCidrBlock 10.151.0.0/16 \
    --RoutePolicySet.0.GatewayType CPM \
    --RoutePolicySet.0.GatewayId 10.1.10.2 \
    --RoutePolicySet.0.RouteDescription test \
    --RoutePolicySet.0.RoutePolicyType USER \
    --RoutePolicySet.0.Enabled true
```

Output: 
```
{
    "Response": {
        "TaskId": 12312,
        "RequestId": "62735da7-4546-4d63-8d42-36ced3bd3d94"
    }
}
```

