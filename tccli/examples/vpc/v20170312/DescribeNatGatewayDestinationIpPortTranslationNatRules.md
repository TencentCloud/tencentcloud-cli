**Example 1: Queries the port forwarding rule of a NAT gateway**

This example shows you how to use the Filter array to pull a NAT gateway’s port forwarding rules.

Input: 

```
tccli vpc DescribeNatGatewayDestinationIpPortTranslationNatRules --cli-unfold-argument  \
    --Filters.0.Name vpc-id \
    --Filters.0.Values vpc-0yi4hekt
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "NatGatewayDestinationIpPortTranslationNatRuleSet": [
            {
                "IpProtocol": "TCP",
                "PublicIpAddress": "139.199.232.238",
                "PublicPort": 8989,
                "PrivateIpAddress": "10.80.80.41",
                "PrivatePort": 8989,
                "Description": "test_dnapt",
                "CreatedTime": "2019-05-04 13:42:11",
                "NatGatewayId": "nat-3isn9hr0",
                "VpcId": "vpc-0yi4hekt"
            },
            {
                "IpProtocol": "UDP",
                "PublicIpAddress": "139.199.232.238",
                "PublicPort": 8989,
                "PrivateIpAddress": "10.80.80.41",
                "PrivatePort": 8989,
                "Description": "test_dnapt",
                "CreatedTime": "2019-05-04 13:20:20",
                "NatGatewayId": "nat-3isn9hr0",
                "VpcId": "vpc-0yi4hekt"
            }
        ],
        "RequestId": "eb203971-a7a0-45c1-9c72-36ad86688590"
    }
}
```

**Example 2: Queries the port forwarding rule of a NAT gateway-2**

This example shows you how to use the NatGatewayId array to pull the NAT gateway’s port forwarding rules.

Input: 

```
tccli vpc DescribeNatGatewayDestinationIpPortTranslationNatRules --cli-unfold-argument  \
    --NatGatewayIds nat-3isn9hr0 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "NatGatewayDestinationIpPortTranslationNatRuleSet": [
            {
                "IpProtocol": "TCP",
                "PublicIpAddress": "139.199.232.238",
                "PublicPort": 8989,
                "PrivateIpAddress": "10.80.80.41",
                "PrivatePort": 8989,
                "Description": "test_dnapt",
                "CreatedTime": "2019-05-04 13:09:25",
                "NatGatewayId": "nat-3isn9hr0",
                "VpcId": "vpc-0yi4hekt"
            },
            {
                "IpProtocol": "UDP",
                "PublicIpAddress": "139.199.232.238",
                "PublicPort": 8989,
                "PrivateIpAddress": "10.80.80.41",
                "PrivatePort": 8989,
                "Description": "test_dnapt",
                "CreatedTime": "2019-05-04 13:20:20",
                "NatGatewayId": "nat-3isn9hr0",
                "VpcId": "vpc-0yi4hekt"
            }
        ],
        "RequestId": "9b751ec3-d10a-4138-bdd9-fa5564684e60"
    }
}
```

