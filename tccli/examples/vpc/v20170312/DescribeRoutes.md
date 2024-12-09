**Example 1: 查询路由列表**

查询路由列表

Input: 

```
tccli vpc DescribeRoutes --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RouteSet": [
            {
                "RouteId": 14915,
                "RouteType": "USER",
                "DestinationCidrBlock": "172.16.0.0/28",
                "GatewayType": "NORMAL_CVM",
                "GatewayId": "172.16.0.25",
                "Enabled": true,
                "PublishedToVbc": true,
                "RouteTableId": "rtb-nswq8wkq",
                "RouteItemId": "rti-hj3he929",
                "RouteDescription": "",
                "CreatedTime": "2020-01-01 10:00:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

