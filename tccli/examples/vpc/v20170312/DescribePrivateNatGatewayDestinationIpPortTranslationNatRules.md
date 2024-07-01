**Example 1: 查询私网NAT网关目的端口转换规则**



Input: 

```
tccli vpc DescribePrivateNatGatewayDestinationIpPortTranslationNatRules --cli-unfold-argument  \
    --NatGatewayId intranat-0g3blj80 \
    --Filters.0.Name Description \
    --Filters.0.Values desc
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "LocalDestinationIpPortTranslationNatRuleSet": [
            {
                "Protocol": "TCP",
                "TranslationIp": "10.0.0.34",
                "TranslationPort": 5666,
                "OriginalIp": "10.0.0.88",
                "OriginalPort": 8888,
                "Description": "chdesc",
                "CreateTime": "2022-09-30 14:23:10",
                "UpdateTime": "2022-09-30 14:33:16"
            },
            {
                "Protocol": "TCP",
                "TranslationIp": "10.0.0.35",
                "TranslationPort": 5666,
                "OriginalIp": "10.0.0.26",
                "OriginalPort": 8888,
                "Description": "desc",
                "CreateTime": "2022-09-30 14:24:38",
                "UpdateTime": "2022-09-30 14:24:38"
            }
        ],
        "RequestId": "cd37ad3b-6b94-41f4-bd83-8a2b0d801aae"
    }
}
```

