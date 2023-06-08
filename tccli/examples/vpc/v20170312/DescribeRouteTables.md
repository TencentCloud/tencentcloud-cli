**Example 1: 查看路由表对象列表**

查看路由表对象列表

Input: 

```
tccli vpc DescribeRouteTables --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values vpc-2at5y1pn \
    --Filters.0.Name vpc-id \
    --Filters.1.Values rtb-l2h8d7c2 \
    --Filters.1.Name route-table-id \
    --Filters.2.Values true \
    --Filters.2.Name association.main \
    --Filters.3.Values TestRouteTable \
    --Filters.3.Name route-table-name \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RouteTableSet": [
            {
                "VpcId": "vpc-2at5y1pn",
                "RouteTableId": "rtb-l2h8d7c2",
                "RouteTableName": "TestRouteTable",
                "AssociationSet": [],
                "RouteSet": [
                    {
                        "RouteId": 0,
                        "RouteItemId": "rti6-12345678",
                        "DestinationCidrBlock": "",
                        "DestinationIpv6CidrBlock": "2402:4e00:1000:810b::/64",
                        "GatewayType": "CCN",
                        "GatewayId": "ccn-12345678",
                        "RouteDescription": ""
                    },
                    {
                        "RouteId": 14915,
                        "RouteItemId": "rti-12345678",
                        "DestinationCidrBlock": "169.254.64.0/23",
                        "GatewayType": "NORMAL_CVM",
                        "GatewayId": "172.16.0.25",
                        "RouteDescription": ""
                    },
                    {
                        "RouteId": 14916,
                        "RouteItemId": "rti-22345678",
                        "DestinationCidrBlock": "10.254.64.0/24",
                        "GatewayType": "NORMAL_CVM",
                        "GatewayId": "172.16.0.26",
                        "RouteDescription": ""
                    },
                    {
                        "RouteId": 14917,
                        "RouteItemId": "rti-32345678",
                        "DestinationCidrBlock": "10.254.100.0/24",
                        "GatewayType": "NORMAL_CVM",
                        "GatewayId": "172.16.0.26",
                        "RouteDescription": "whoIam"
                    },
                    {
                        "RouteId": 16642,
                        "RouteItemId": "rti-42345678",
                        "DestinationCidrBlock": "10.200.0.0/18",
                        "GatewayType": "PEERCONNECTION",
                        "GatewayId": "pcx-4n2m594s",
                        "RouteDescription": "bb"
                    }
                ],
                "Main": false,
                "TagSet": [
                    {
                        "Value": "test",
                        "Key": "test"
                    }
                ],
                "LocalCidrForCcn": [
                    {
                        "Cidr": "10.1.0.0/16",
                        "PublishedToVbc": true
                    }
                ],
                "CreatedTime": "2017-06-30 19:52:03"
            }
        ],
        "TotalCount": 16,
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

**Example 2: 查询绑定了标签的路由表列表**

查询绑定了标签的路由表列表

Input: 

```
tccli vpc DescribeRouteTables --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values shanghai \
    --Filters.0.Name tag:city \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RouteTableSet": [
            {
                "VpcId": "vpc-2at5y1pn",
                "RouteTableId": "rtb-l2h8d7c2",
                "RouteTableName": "TestRouteTable",
                "AssociationSet": [],
                "RouteSet": [
                    {
                        "RouteId": 14915,
                        "RouteItemId": "rti-12345678",
                        "DestinationCidrBlock": "169.254.64.0/23",
                        "GatewayType": "NORMAL_CVM",
                        "GatewayId": "172.16.0.25",
                        "RouteDescription": ""
                    },
                    {
                        "RouteId": 14916,
                        "RouteItemId": "rti-22345678",
                        "DestinationCidrBlock": "10.254.64.0/24",
                        "GatewayType": "NORMAL_CVM",
                        "GatewayId": "172.16.0.26",
                        "RouteDescription": ""
                    },
                    {
                        "RouteId": 14917,
                        "RouteItemId": "rti-32345678",
                        "DestinationCidrBlock": "10.254.100.0/24",
                        "GatewayType": "NORMAL_CVM",
                        "GatewayId": "172.16.0.26",
                        "RouteDescription": "whoIam"
                    },
                    {
                        "RouteId": 16642,
                        "RouteItemId": "rti-42345678",
                        "DestinationCidrBlock": "10.200.0.0/18",
                        "GatewayType": "PEERCONNECTION",
                        "GatewayId": "pcx-4n2m594s",
                        "RouteDescription": "bb"
                    }
                ],
                "TagSet": [
                    {
                        "Key": "city",
                        "Value": "shanghai"
                    }
                ],
                "LocalCidrForCcn": [
                    {
                        "Cidr": "10.1.0.0/16",
                        "PublishedToVbc": true
                    }
                ],
                "Main": false,
                "CreatedTime": "2017-06-30 19:52:03"
            }
        ],
        "TotalCount": 16,
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

