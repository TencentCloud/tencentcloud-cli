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
                        "RouteId": 20662,
                        "DestinationCidrBlock": "192.168.0.0/24",
                        "GatewayId": "135",
                        "GatewayType": "11",
                        "RouteDescription": ""
                    }
                ]
            },
            {
                "RouteTableId": "rtb-q8o2z892",
                "DestinationCidrBlock": "10.11.0.0/24",
                "ConflictSet": [
                    {
                        "RouteId": 20661,
                        "DestinationCidrBlock": "10.11.0.0/24",
                        "GatewayId": "135",
                        "GatewayType": "11",
                        "RouteDescription": ""
                    }
                ]
            }
        ],
        "RequestId": "cf11a8a4-e7c6-42cf-a35a-649c1789868b"
    }
}
```

