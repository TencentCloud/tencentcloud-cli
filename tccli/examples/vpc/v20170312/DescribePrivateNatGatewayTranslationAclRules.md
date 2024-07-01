**Example 1: 查询私网NAT网关源端转换访问控制规则**

查询私网NAT网关源端转换访问控制规则

Input: 

```
tccli vpc DescribePrivateNatGatewayTranslationAclRules --cli-unfold-argument  \
    --NatGatewayId intranat-0g3blj80 \
    --TranslationDirection LOCAL \
    --TranslationType NETWORK_LAYER \
    --TranslationIp 10.0.0.24 \
    --OriginalIp 10.0.0.14
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "TranslationAclRuleSet": [
            {
                "Protocol": "ALL",
                "Action": 0,
                "AclRuleId": 1,
                "SourcePort": "0-65535",
                "SourceCidr": "0.0.0.0/0",
                "DestinationPort": "0-65535",
                "DestinationCidr": "0.0.0.0/0"
            },
            {
                "Protocol": "TCP",
                "Action": 0,
                "AclRuleId": 26,
                "SourcePort": "5666",
                "SourceCidr": "10.0.0.14",
                "DestinationPort": "8888",
                "DestinationCidr": "10.0.0.24"
            }
        ],
        "RequestId": "41fe53eb-6f90-4fde-9e37-c48fa4f8f2ed"
    }
}
```

