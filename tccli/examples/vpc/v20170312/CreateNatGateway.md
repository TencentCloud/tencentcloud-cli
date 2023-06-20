**Example 1: 创建NAT网关**

创建一个传统型NAT网关并自动分配一个EIP

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
                "RestrictState": "NORMAL",
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

**Example 2: 创建标准型NAT网关**

创建一个标准型NAT网关并自动分配一个EIP

Input: 

```
tccli vpc CreateNatGateway --cli-unfold-argument  \
    --SubnetId subnet-q1b8fsg \
    --AddressCount 1 \
    --NatGatewayName xiaooliang_test \
    --VpcId vpc-bohigpb7
```

Output: 
```
{
    "Response": {
        "NatGatewaySet": [
            {
                "NatGatewayId": "nat-o49t53q2",
                "NatGatewayName": "xiaooliang_test",
                "VpcId": "vpc-bohigpb7",
                "State": "PENDING",
                "NetworkState": "AVAILABLE",
                "InternetMaxBandwidthOut": 100,
                "MaxConcurrentConnection": 1000000,
                "PublicIpAddressSet": [],
                "DestinationIpPortTranslationNatRuleSet": [],
                "CreatedTime": "0000-00-00 00:00:00",
                "Zone": "",
                "TagSet": [],
                "DirectConnectGatewayIds": [],
                "SubnetId": "subnet-q1b8fsgu",
                "SecurityGroupSet": [],
                "SourceIpTranslationNatRuleSet": [],
                "IsExclusive": false,
                "RestrictState": "NORMAL",
                "ExclusiveGatewayBandwidth": null
            }
        ],
        "TotalCount": 1,
        "RequestId": "7b00a07c-7358-4f0a-b81c-8ce5882a87b8"
    }
}
```

