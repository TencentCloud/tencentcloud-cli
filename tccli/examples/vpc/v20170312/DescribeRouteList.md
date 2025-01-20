**Example 1: 查询路由条目**

通过路由表ID作为过滤条件，查询1条路由条目

Input: 

```
tccli vpc DescribeRouteList --cli-unfold-argument  \
    --Filters.0.Name route-table-id \
    --Filters.0.Values rtb-la2qkgku \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "4525a651-aa66-451e-bb20-839c967e9172",
        "RouteSet": [
            {
                "CdcId": "",
                "CreatedTime": "2024-12-27 16:44:44",
                "DestinationCidrBlock": "",
                "DestinationIpv6CidrBlock": "2402:4e00:1717:bc00::/64",
                "Enabled": true,
                "GatewayId": "ccn-j0w29irz",
                "GatewayType": "CCN",
                "PublishedToVbc": false,
                "RouteDescription": "",
                "RouteId": 0,
                "RouteItemId": "rti6-exmyaywi",
                "RouteTableId": "rtb-la2qkgku",
                "RouteType": "CCN"
            }
        ],
        "TotalCount": 7
    }
}
```

