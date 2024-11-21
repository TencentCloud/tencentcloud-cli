**Example 1: 查询路由策略冲突列表**

查询路由策略冲突列表

Input: 

```
tccli vpc DescribeRouteConflicts --cli-unfold-argument  \
    --RouteTableId rtb-q8o2z892 \
    --DestinationCidrBlocks 192.168.0.0/24 10.11.0.0/24
```

Output: 
```
{
    "Response": {
        "RouteConflictSet": [
            {
                "RouteTableId": "rtb-q8o2z892",
                "DestinationCidrBlock": "192.168.0.0/24",
                "ConflictSet": [
                    {
                        "RouteTableId": "rtb-q8o2z892",
                        "RouteId": 20662,
                        "RouteItemId": "rti-hj3he929",
                        "DestinationCidrBlock": "192.168.0.0/24",
                        "GatewayId": "ccn-h0fk8lfc",
                        "GatewayType": "CCN",
                        "RouteDescription": "",
                        "Enabled": true,
                        "RouteType": "CCN",
                        "DestinationIpv6CidrBlock": "",
                        "PublishedToVbc": true,
                        "CreatedTime": "2020-09-22 00:00:00",
                        "CdcId": ""
                    }
                ]
            }
        ],
        "RequestId": "cf11a8a4-e7c6-42cf-a35a-649c1789868b"
    }
}
```

