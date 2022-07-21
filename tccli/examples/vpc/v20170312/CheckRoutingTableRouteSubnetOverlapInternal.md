**Example 1: 判断和路由表网段是否冲突**



Input: 

```
tccli vpc CheckRoutingTableRouteSubnetOverlapInternal --cli-unfold-argument  \
    --UniqueVpcId vpc-jmaywf6r \
    --Subnet 10.0.0.0 \
    --IntMask 16
```

Output: 
```
{
    "Response": {
        "CheckCode": 0,
        "OverlapList": [
            {
                "Subnet": "10.2.0.0",
                "VpcId": 6,
                "Name": "testss2",
                "UniqueVpcId": "vpc-pe0kssdp",
                "VirtualGatewayType": 4,
                "UniqueVpcGatewayIndex": "pcx-qjtzxwhm",
                "Mask": "255.255.0.0",
                "RoutingTableId": 29,
                "IntMask": 16,
                "VpcGatewayIndex": "19",
                "Owner": "toyacao",
                "UniqueRoutingTableId": "rtb-o9u877nw"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

