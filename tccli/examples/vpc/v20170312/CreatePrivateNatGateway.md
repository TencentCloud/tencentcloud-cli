**Example 1: 创建一个私网NAT网关**

创建一个私网NAT网关

Input: 

```
tccli vpc CreatePrivateNatGateway --cli-unfold-argument  \
    --NatGatewayName test \
    --VpcId vpc-m7sr81gh
```

Output: 
```
{
    "Response": {
        "PrivateNatGatewaySet": [
            {
                "Status": "AVILIABLE",
                "VpcId": "vpc-noanwmed",
                "CrossDomain": false,
                "NatGatewayName": "test_nat",
                "NatGatewayId": "intranat-0g3blj80",
                "TagSet": [],
                "CreatedTime": "2022-10-01 00:00:00"
            }
        ],
        "RequestId": "cd37ad3b-6b94-41f4-bd83-8a2b0d801aae",
        "TotalCount": 1
    }
}
```

