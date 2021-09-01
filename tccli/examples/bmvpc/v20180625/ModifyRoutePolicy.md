**Example 1: 修改路由表路由条目**

修改路由表路由条目

Input: 

```
tccli bmvpc ModifyRoutePolicy --cli-unfold-argument  \
    --RouteTableId rtb-19yps3nz \
    --RoutePolicy.DestinationCidrBlock 10.151.0.0/16 \
    --RoutePolicy.GatewayType CPM \
    --RoutePolicy.GatewayId 10.1.10.2 \
    --RoutePolicy.RouteDescription test \
    --RoutePolicy.RoutePolicyId rti-3xx8yzru \
    --RoutePolicy.RoutePolicyType USER \
    --RoutePolicy.Enabled true
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

