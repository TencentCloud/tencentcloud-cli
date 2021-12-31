**Example 1: 创建一个关联VPC的NAT型专线网关**



Input: 

```
tccli vpc CreateDirectConnectGateway --cli-unfold-argument  \
    --DirectConnectGatewayName test \
    --NetworkType VPC \
    --NetworkInstanceId vpc-m7sr81gh \
    --GatewayType NAT
```

Output: 
```
{
    "Response": {
        "DirectConnectGateway": {
            "DirectConnectGatewayId": "dcg-gjug0kul",
            "DirectConnectGatewayName": "test",
            "DirectConnectGatewayIp": "10.21.0.5",
            "EnableBGPCommunity": false,
            "VpcId": "vpc-m7sr81gh",
            "CcnId": "",
            "EnableBGP": false,
            "CcnRouteType": "BGP",
            "NetworkType": "VPC",
            "NetworkInstanceId": "vpc-m7sr81gh",
            "GatewayType": "NAT",
            "VXLANSupport": [
                true
            ],
            "NatGatewayId": "nat-m7dr11gc",
            "LocalZone": false,
            "Zone": "ap-guangzhou-1",
            "ModeType": "standard",
            "NewAfc": 0,
            "FlowDetailsUpdateTime": "xx",
            "EnableFlowDetails": 0,
            "AccessNetworkType": "Unknown",
            "CreateTime": "2020-09-22 00:00:00"
        },
        "RequestId": "b8351d12-3c82-4d4b-9d88-972e02ca4620"
    }
}
```

**Example 2: 创建一个关联CCN的标准型专线网关**



Input: 

```
tccli vpc CreateDirectConnectGateway --cli-unfold-argument  \
    --DirectConnectGatewayName test \
    --NetworkType CCN \
    --NetworkInstanceId ccn-8j0phqix \
    --GatewayType NORMAL
```

Output: 
```
{
    "Response": {
        "DirectConnectGateway": {
            "DirectConnectGatewayId": "dcg-3vwxt61v",
            "DirectConnectGatewayName": "test",
            "VpcId": "vpc-ilii3ejt",
            "NetworkType": "CCN",
            "NetworkInstanceId": "ccn-c1aopa13",
            "GatewayType": "NORMAL",
            "EnableBGPCommunity": true,
            "EnableBGP": true,
            "CcnId": "ccn-8j0phqix",
            "CcnRouteType": "BGP",
            "NatGatewayId": "",
            "DirectConnectGatewayIp": "10.21.0.5",
            "LocalZone": false,
            "Zone": "ap-guangzhou-1",
            "ModeType": "standard",
            "VXLANSupport": [
                true
            ],
            "CreateTime": "0000-00-00 00:00:00",
            "NewAfc": 1,
            "FlowDetailsUpdateTime": "xx",
            "EnableFlowDetails": 0,
            "AccessNetworkType": "VXLAN"
        },
        "RequestId": "b8351d12-3c82-4d4b-9d88-972e02ca4620"
    }
}
```

