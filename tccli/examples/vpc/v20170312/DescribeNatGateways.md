**Example 1: 查询 NAT 网关信息**

用Filters进行查询NAT网关信息。

Input: 

```
tccli vpc DescribeNatGateways --cli-unfold-argument  \
    --Filters.0.Name vpc-id \
    --Filters.0.Values vpc-0yi4hekt \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "NatGatewaySet": [
            {
                "NatGatewayId": "nat-3isn9hr0",
                "NatGatewayName": "NatDemo",
                "VpcId": "vpc-0yi4hekt",
                "CreatedTime": "2017-09-20 20:28:24",
                "State": "AVAILABLE",
                "NetworkState": "AVAILABLE",
                "SmartScheduleMode": true,
                "DedicatedClusterId": "cluster-8zkaer1h",
                "InternetMaxBandwidthOut": 100,
                "MaxConcurrentConnection": 1000000,
                "DeletionProtectionEnabled": false,
                "PublicIpAddressSet": [
                    {
                        "AddressId": "eip-7qcdm91q",
                        "PublicIpAddress": "139.199.232.238",
                        "IsBlocked": false,
                        "BlockType": ""
                    }
                ],
                "DestinationIpPortTranslationNatRuleSet": [
                    {
                        "IpProtocol": "TCP",
                        "PublicIpAddress": "139.199.232.238",
                        "PublicPort": 8586,
                        "PrivateIpAddress": "10.80.80.41",
                        "PrivatePort": 8989,
                        "Description": "test_modify"
                    },
                    {
                        "IpProtocol": "UDP",
                        "PublicIpAddress": "139.199.232.238",
                        "PublicPort": 8989,
                        "PrivateIpAddress": "10.80.80.41",
                        "PrivatePort": 8989,
                        "Description": "dnapt"
                    }
                ],
                "Zone": "ap-guangzhou-1",
                "TagSet": [
                    {
                        "Key": "Creator",
                        "Value": "TencentCloud"
                    }
                ],
                "SecurityGroupSet": [],
                "ExclusiveGatewayBandwidth": 1,
                "IsExclusive": true,
                "SubnetId": "sub-er88uji9",
                "DirectConnectGatewayIds": [],
                "SourceIpTranslationNatRuleSet": [],
                "RestrictState": "NORMAL",
                "NatProductVersion": 1
            },
            {
                "NatGatewayId": "nat-7xh58vea",
                "NatGatewayName": "Nat-create",
                "VpcId": "vpc-0yi4hekt",
                "CreatedTime": "2019-05-04 15:01:11",
                "State": "PENDING",
                "NetworkState": "AVAILABLE",
                "SmartScheduleMode": true,
                "DedicatedClusterId": "",
                "InternetMaxBandwidthOut": 100,
                "MaxConcurrentConnection": 1000000,
                "DeletionProtectionEnabled": false,
                "PublicIpAddressSet": [],
                "DestinationIpPortTranslationNatRuleSet": [],
                "Zone": "ap-guangzhou-2",
                "TagSet": [
                    {
                        "Key": "Creator",
                        "Value": "TencentCloud"
                    }
                ],
                "SecurityGroupSet": [],
                "ExclusiveGatewayBandwidth": 1,
                "IsExclusive": true,
                "SubnetId": "sub-er88uji9",
                "DirectConnectGatewayIds": [],
                "SourceIpTranslationNatRuleSet": [],
                "RestrictState": "NORMAL",
                "NatProductVersion": 2
            }
        ],
        "TotalCount": 2,
        "VerboseLevel": "DETAIL",
        "RequestId": "a3964872-e2f5-4180-8607-0b49ec8e0109"
    }
}
```

**Example 2: 查询 NAT 网关信息-2**

用NatGatewayIds进行查询NAT网关信息。

Input: 

```
tccli vpc DescribeNatGateways --cli-unfold-argument  \
    --NatGatewayIds nat-3isn9hr0 nat-mxkohguo \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "NatGatewaySet": [
            {
                "NatGatewayId": "nat-3isn9hr0",
                "NatGatewayName": "PublicDemo",
                "VpcId": "vpc-0yi4hekt",
                "CreatedTime": "2017-09-20 20:28:24",
                "State": "AVAILABLE",
                "NetworkState": "AVAILABLE",
                "SmartScheduleMode": true,
                "DedicatedClusterId": "cluster-acdz123k",
                "InternetMaxBandwidthOut": 100,
                "MaxConcurrentConnection": 1000000,
                "DeletionProtectionEnabled": false,
                "SecurityGroupSet": [],
                "ExclusiveGatewayBandwidth": 1,
                "IsExclusive": true,
                "SubnetId": "sub-er88uji9",
                "DirectConnectGatewayIds": [],
                "SourceIpTranslationNatRuleSet": [],
                "PublicIpAddressSet": [
                    {
                        "AddressId": "eip-7qcdm91q",
                        "PublicIpAddress": "139.199.232.238",
                        "IsBlocked": false,
                        "BlockType": ""
                    }
                ],
                "DestinationIpPortTranslationNatRuleSet": [
                    {
                        "IpProtocol": "TCP",
                        "PublicIpAddress": "139.199.232.238",
                        "PublicPort": 8586,
                        "PrivateIpAddress": "10.80.80.41",
                        "PrivatePort": 8989,
                        "Description": "test_modify"
                    },
                    {
                        "IpProtocol": "UDP",
                        "PublicIpAddress": "139.199.232.238",
                        "PublicPort": 8989,
                        "PrivateIpAddress": "10.80.80.41",
                        "PrivatePort": 8989,
                        "Description": "test_dnapt"
                    }
                ],
                "Zone": "ap-guangzhou-1",
                "TagSet": [
                    {
                        "Key": "Creator",
                        "Value": "TencentCloud"
                    }
                ],
                "RestrictState": "NORMAL",
                "NatProductVersion": 1
            },
            {
                "NatGatewayId": "nat-mxkohguo",
                "NatGatewayName": "Nat_Demo",
                "VpcId": "vpc-m7sihqw5",
                "CreatedTime": "2018-07-25 11:37:29",
                "State": "PENDING",
                "NetworkState": "UNAVAILABLE",
                "SmartScheduleMode": true,
                "DedicatedClusterId": "",
                "InternetMaxBandwidthOut": 100,
                "MaxConcurrentConnection": 1000000,
                "DeletionProtectionEnabled": false,
                "PublicIpAddressSet": [],
                "DestinationIpPortTranslationNatRuleSet": [],
                "Zone": "ap-guangzhou-1",
                "TagSet": [
                    {
                        "Key": "Creator",
                        "Value": "TencentCloud"
                    }
                ],
                "SecurityGroupSet": [],
                "ExclusiveGatewayBandwidth": 1,
                "IsExclusive": true,
                "SubnetId": "sub-er88uji9",
                "DirectConnectGatewayIds": [],
                "SourceIpTranslationNatRuleSet": [],
                "RestrictState": "NORMAL",
                "NatProductVersion": 1
            }
        ],
        "TotalCount": 2,
        "VerboseLevel": "DETAIL",
        "RequestId": "fed7e087-083f-49e4-8754-17fb130828e0"
    }
}
```

