**Example 1: 按ID过滤查询私网NAT网关**

按ID过滤查询私网NAT网关

Input: 

```
tccli vpc DescribePrivateNatGateways --cli-unfold-argument  \
    --NatGatewayIds intranat-0g3blj80
```

Output: 
```
{
    "Response": {
        "PrivateNatGatewaySet": [
            {
                "NatGatewayId": "intranat-0g3blj80",
                "NatGatewayName": "test_nat",
                "NatType": "DCG",
                "VpcId": "vpc-noanwmed",
                "Status": "AVAILABLE",
                "CrossDomain": false,
                "CreatedTime": "2022-09-29 15:58:00",
                "DirectConnectGatewayIds": [],
                "TagSet": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "757e8409-faa3-4b7f-bfc3-7e1670bf40af"
    }
}
```

**Example 2: 按标签过滤查询私网NAT网关**

按标签过滤查询私网NAT网关

Input: 

```
tccli vpc DescribePrivateNatGateways --cli-unfold-argument  \
    --Filters.0.Name TagKey \
    --Filters.0.Values 负责人
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "PrivateNatGatewaySet": [
            {
                "NatGatewayId": "intranat-ryur99m8",
                "NatGatewayName": "example",
                "VpcId": "vpc-d3rrkwej",
                "Status": "AVAILABLE",
                "CrossDomain": false,
                "CreatedTime": "2023-03-09 16:19:24",
                "TagSet": [
                    {
                        "Key": "负责人",
                        "Value": "TencentCloud"
                    }
                ],
                "DirectConnectGatewayIds": [],
                "NatType": "DCG",
                "CrossDomainInfo": {
                    "CcnId": "ccn-123abcef",
                    "LocalVpcId": "vpc-12345678",
                    "PeerVpcId": "vpc-abcdefgh"
                }
            }
        ],
        "RequestId": "e13d67ca-4b7b-4337-b8c5-7df7707c89ca"
    }
}
```

