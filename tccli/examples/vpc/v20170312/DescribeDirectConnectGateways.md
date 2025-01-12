**Example 1: 按ID过滤查询专线网关**



Input: 

```
tccli vpc DescribeDirectConnectGateways --cli-unfold-argument  \
    --DirectConnectGatewayIds dcg-dimeg9zd dcg-6eeis68f dcg-94cdyvfr
```

Output: 
```
{
    "Response": {
        "DirectConnectGatewaySet": [
            {
                "LocalZone": true,
                "NewAfc": 1,
                "EnableBGPCommunity": true,
                "Zone": "demo",
                "FlowDetailsUpdateTime": "demo",
                "AccessNetworkType": "demo",
                "VXLANSupport": [
                    true
                ],
                "ModeType": "demo",
                "NatGatewayId": "demo",
                "DirectConnectGatewayId": "dcg-6eeis68f",
                "DirectConnectGatewayName": "我的网关01",
                "DirectConnectGatewayIp": "10.6.223.4",
                "GatewayType": "NORMAL",
                "NetworkType": "CCN",
                "NetworkInstanceId": "",
                "VpcId": "vpc-jkmjx7pd",
                "CcnId": "",
                "CcnRouteType": "STATIC",
                "EnableBGP": false,
                "CreateTime": "2018-10-22 21:22:26",
                "HaZoneList": [
                    "demo"
                ],
                "EnableFlowDetails": 1
            },
            {
                "DirectConnectGatewayId": "dcg-94cdyvfr",
                "DirectConnectGatewayName": "我的网关02",
                "DirectConnectGatewayIp": "10.144.25.62",
                "GatewayType": "NORMAL",
                "NetworkType": "CCN",
                "NetworkInstanceId": "",
                "EnableFlowDetails": 1,
                "VpcId": "vpc-f796it7v",
                "CcnId": "",
                "CcnRouteType": "STATIC",
                "EnableBGP": false,
                "CreateTime": "2018-08-21 11:40:09",
                "HaZoneList": [
                    "demo"
                ],
                "LocalZone": true,
                "NewAfc": 1,
                "EnableBGPCommunity": true,
                "Zone": "demo",
                "FlowDetailsUpdateTime": "demo",
                "AccessNetworkType": "demo",
                "VXLANSupport": [
                    true
                ],
                "ModeType": "demo",
                "NatGatewayId": "demo"
            },
            {
                "DirectConnectGatewayId": "dcg-dimeg9zd",
                "DirectConnectGatewayName": "我的网关03",
                "DirectConnectGatewayIp": "10.144.25.62",
                "GatewayType": "NORMAL",
                "NetworkType": "CCN",
                "NetworkInstanceId": "ccn-atw2c2j1",
                "VpcId": "vpc-eg3eig77",
                "CcnId": "ccn-atw2c2j1",
                "CcnRouteType": "STATIC",
                "EnableFlowDetails": 1,
                "EnableBGP": false,
                "CreateTime": "2018-08-21 11:36:50",
                "HaZoneList": [
                    "demo"
                ],
                "LocalZone": true,
                "NewAfc": 1,
                "EnableBGPCommunity": true,
                "Zone": "demo",
                "FlowDetailsUpdateTime": "demo",
                "AccessNetworkType": "demo",
                "VXLANSupport": [
                    true
                ],
                "ModeType": "demo",
                "NatGatewayId": "nat"
            }
        ],
        "TotalCount": 3,
        "RequestId": "1b64d03b-7d2d-4d9b-b46e-49de115ac283"
    }
}
```

**Example 2: 多条件过滤查询专线网关列表**



Input: 

```
tccli vpc DescribeDirectConnectGateways --cli-unfold-argument  \
    --Filters.0.Name direct-connect-gateway-name \
    --Filters.0.Values 我的网关 \
    --Filters.1.Name gateway-type \
    --Filters.1.Values NORMAL \
    --Filters.2.Name vpc-id \
    --Filters.2.Values vpc-f796it7v vpc-jkmjx7pd
```

Output: 
```
{
    "Response": {
        "DirectConnectGatewaySet": [
            {
                "DirectConnectGatewayId": "dcg-94cdyvfr",
                "DirectConnectGatewayName": "我的网关",
                "DirectConnectGatewayIp": "10.144.25.62",
                "GatewayType": "NORMAL",
                "NetworkType": "CCN",
                "NetworkInstanceId": "",
                "VpcId": "vpc-f796it7v",
                "CcnId": "",
                "CcnRouteType": "STATIC",
                "EnableBGP": false,
                "EnableFlowDetails": 1,
                "CreateTime": "2018-08-21 11:40:09",
                "HaZoneList": [
                    "demo"
                ],
                "LocalZone": true,
                "NewAfc": 1,
                "EnableBGPCommunity": true,
                "Zone": "demo",
                "FlowDetailsUpdateTime": "demo",
                "AccessNetworkType": "demo",
                "VXLANSupport": [
                    true
                ],
                "ModeType": "demo",
                "NatGatewayId": "demo"
            },
            {
                "DirectConnectGatewayId": "dcg-6eeis68f",
                "DirectConnectGatewayName": "我的网关",
                "DirectConnectGatewayIp": "10.6.223.4",
                "GatewayType": "NORMAL",
                "NetworkType": "CCN",
                "NetworkInstanceId": "",
                "VpcId": "vpc-jkmjx7pd",
                "CcnId": "",
                "CcnRouteType": "STATIC",
                "EnableBGP": false,
                "CreateTime": "2018-10-22 21:22:26",
                "HaZoneList": [
                    "demo"
                ],
                "LocalZone": true,
                "NewAfc": 1,
                "EnableBGPCommunity": true,
                "Zone": "demo",
                "FlowDetailsUpdateTime": "demo",
                "AccessNetworkType": "demo",
                "EnableFlowDetails": 1,
                "VXLANSupport": [
                    true
                ],
                "ModeType": "demo",
                "NatGatewayId": "demo"
            }
        ],
        "TotalCount": 2,
        "RequestId": "8c77ce69-68e2-4dfa-94ea-a6df5c914f52"
    }
}
```

