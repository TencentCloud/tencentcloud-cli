**Example 1: 创建NAT网关**



Input: 

```
tccli vpc CreateNatGateway --cli-unfold-argument  \
    --VpcId vpc-abcdefgh \
    --PublicIpAddresses 139.199.232.119 \
    --MaxConcurrentConnection 1000000 \
    --Tags.0.Value shanghai \
    --Tags.0.Key city \
    --InternetMaxBandwidthOut 10 \
    --NatGatewayName test_name \
    --AddressCount 1
```

Output: 
```
{
    "Response": {
        "NatGatewaySet": [
            {
                "NatGatewayId": "nat-cqbn23ju",
                "NatGatewayName": "11111",
                "VpcId": "vpc-qi4ja3sx",
                "CreatedTime": "2019-07-16 09:40:00",
                "State": "AVAILABLE",
                "NetworkState": "AVAILABLE",
                "InternetMaxBandwidthOut": 10,
                "MaxConcurrentConnection": 1000000,
                "SecurityGroupSet": [],
                "PublicIpAddressSet": [
                    {
                        "AddressId": "eip-9uw5fwsu",
                        "PublicIpAddress": "139.199.232.119",
                        "IsBlocked": false
                    },
                    {
                        "AddressId": "eip-9uw5fsss",
                        "PublicIpAddress": "139.199.232.221",
                        "IsBlocked": false
                    }
                ],
                "DestinationIpPortTranslationNatRuleSet": [],
                "DirectConnectGatewayIds": [],
                "Zone": "ap-guangzhou-2",
                "ExclusiveGatewayBandwidth": 1,
                "IsExclusive": true,
                "SourceIpTranslationNatRuleSet": [],
                "SubnetId": "1215354",
                "TagSet": [
                    {
                        "Key": "city",
                        "Value": "shanghai"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "6f2a42cf-2905-4fa5-af49-0f01612550de"
    }
}
```

