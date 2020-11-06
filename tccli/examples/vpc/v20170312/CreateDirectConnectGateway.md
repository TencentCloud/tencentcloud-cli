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
            "VpcId": "vpc-m7sr81gh",
            "NetworkType": "VPC",
            "NetworkInstanceId": "vpc-m7sr81gh",
            "GatewayType": "NAT",
            "DirectConnectTunnelCount": 8,
            "CreatedTime": "0000-00-00 00:00:00"
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
            "DirectConnectTunnelCount": 0,
            "CreateTime": "0000-00-00 00:00:00"
        },
        "RequestId": "b8351d12-3c82-4d4b-9d88-972e02ca4620"
    }
}
```

