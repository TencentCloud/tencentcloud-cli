**Example 1: 创建一个私网NAT网关**

创建一个私网NAT网关

Input: 

```
tccli vpc CreatePrivateNatGateway --cli-unfold-argument  \
    --NatGatewayName PrivateNatDemo \
    --VpcId vpc-m7sr81gh
```

Output: 
```
{
    "Response": {
        "PrivateNatGatewaySet": [
            {
                "NatType": "DCG",
                "Status": "AVILIABLE",
                "VpcId": "vpc-noanwmed",
                "CrossDomain": false,
                "NatGatewayName": "PrivateNatDemo",
                "NatGatewayId": "intranat-0g3blj80",
                "TagSet": [],
                "DirectConnectGatewayIds": [],
                "CreatedTime": "2022-10-01 00:00:00"
            }
        ],
        "RequestId": "cd37ad3b-6b94-41f4-bd83-8a2b0d801aae",
        "TotalCount": 1
    }
}
```

