**Example 1: 查询NAT网关SNAT转发规则**

用Filter数组拉取NAT网关的SNAT转发规则

Input: 

```
tccli vpc DescribeNatGatewaySourceIpTranslationNatRules --cli-unfold-argument  \
    --NatGatewayId nat-3isn9hr0 \
    --Filters.0.Name resource-id \
    --Filters.0.Values subnet-0yi4hekt
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SourceIpTranslationNatRuleSet": [
            {
                "NatGatewaySnatId": "subnet-0yi4hekt",
                "ResourceId": "subnet-0yi4hekt",
                "ResourceType": "SUBNET",
                "PublicIpAddresses": [
                    "139.199.232.238"
                ],
                "PrivateIpAddress": "10.80.80.0/24",
                "Description": "test_snat",
                "CreatedTime": "2019-05-04 13:42:11",
                "NatGatewayId": "nat-3isn9hr0",
                "VpcId": "vpc-0yi4hekt"
            }
        ],
        "RequestId": "eb203971-a7a0-45c1-9c72-36ad86688590"
    }
}
```

