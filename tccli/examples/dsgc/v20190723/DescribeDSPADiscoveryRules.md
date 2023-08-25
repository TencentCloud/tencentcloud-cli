**Example 1: 获取分类分级规则列表**

xx

Input: 

```
tccli dsgc DescribeDSPADiscoveryRules --cli-unfold-argument  \
    --DspaId casb_1 \
    --RuleId 1 \
    --Limit 10 \
    --Name test_rule \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Items": [
            {
                "RuleId": 0,
                "Name": "abc",
                "Description": "abc",
                "Source": 0,
                "RDBRules": {
                    "Status": 0,
                    "MatchOperator": "abc",
                    "MetaRule": {
                        "Operator": "abc",
                        "Contents": [
                            {
                                "RuleType": "abc",
                                "RuleContent": "abc",
                                "ExtendParameters": [
                                    {
                                        "Name": "abc",
                                        "Value": "abc"
                                    }
                                ]
                            }
                        ]
                    },
                    "ContentRule": {
                        "Operator": "abc",
                        "Contents": [
                            {
                                "RuleType": "abc",
                                "RuleContent": "abc",
                                "ExtendParameters": [
                                    {
                                        "Name": "abc",
                                        "Value": "abc"
                                    }
                                ]
                            }
                        ]
                    }
                },
                "COSRules": {
                    "Status": 0,
                    "RegexRule": {
                        "Operator": "abc",
                        "Contents": [
                            {
                                "RuleContent": "abc",
                                "IsIgnoreCase": true
                            }
                        ]
                    },
                    "KeywordRule": {
                        "Operator": "abc",
                        "Contents": [
                            {
                                "RuleContent": "abc",
                                "IsIgnoreCase": true
                            }
                        ]
                    },
                    "IgnoreStringRule": {
                        "Operator": "abc",
                        "Contents": [
                            {
                                "RuleContent": "abc",
                                "IsIgnoreCase": true
                            }
                        ]
                    },
                    "MaxMatch": 0
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

