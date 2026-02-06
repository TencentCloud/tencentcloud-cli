**Example 1: 查询私网NAT网关源端转换规则**



Input: 

```
tccli vpc DescribePrivateNatGatewayTranslationNatRules --cli-unfold-argument  \
    --NatGatewayId intranat-0g3blj80 \
    --Filters.0.Name TranslationIp \
    --Filters.0.Values 10.0.0.24 \
    --Filters.1.Name Description \
    --Filters.1.Values desc
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "TranslationNatRuleSet": [
            {
                "Description": "desc",
                "CreateTime": "2022-09-29 20:48:28",
                "UpdateTime": "2022-09-29 20:48:28",
                "TranslationDirection": "PEER",
                "TranslationType": "NETWORK_LAYER",
                "TranslationIp": "10.0.0.222",
                "OriginalIp": "10.0.0.86"
            },
            {
                "Description": "desc",
                "CreateTime": "2022-09-29 20:48:28",
                "UpdateTime": "2022-09-29 20:48:28",
                "TranslationDirection": "PEER",
                "TranslationType": "NETWORK_LAYER",
                "TranslationIp": "10.0.0.56",
                "OriginalIp": "10.0.0.34"
            }
        ],
        "RequestId": "35dc4665-6c7a-474d-bd4a-8c0ed92f1d02"
    }
}
```

