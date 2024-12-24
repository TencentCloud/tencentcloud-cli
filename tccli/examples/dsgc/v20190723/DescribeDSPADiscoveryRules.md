**Example 1: 获取分类分级规则列表**



Input: 

```
tccli dsgc DescribeDSPADiscoveryRules --cli-unfold-argument  \
    --DspaId dspa-2asd28ax \
    --RuleId 1 \
    --Limit 10 \
    --Name 姓名 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Items": [
            {
                "RuleId": 1,
                "Name": "账户余额",
                "Description": "账户余额",
                "Source": 1,
                "Status": 1,
                "RDBRules": {
                    "Status": 0,
                    "MatchOperator": "or",
                    "MetaRule": {
                        "Operator": "and",
                        "Contents": [
                            {
                                "RuleType": "keyword",
                                "RuleContent": "账户|Account",
                                "ExtendParameters": [
                                    {
                                        "Name": "IsFullWordMatch",
                                        "Value": "false"
                                    },
                                    {
                                        "Name": "IsIgnoreCase",
                                        "Value": "true"
                                    }
                                ]
                            },
                            {
                                "RuleType": "keyword",
                                "RuleContent": "余额|Balance",
                                "ExtendParameters": [
                                    {
                                        "Name": "IsFullWordMatch",
                                        "Value": "false"
                                    },
                                    {
                                        "Name": "IsIgnoreCase",
                                        "Value": "true"
                                    }
                                ]
                            }
                        ]
                    },
                    "ContentRule": {
                        "Operator": "or",
                        "Contents": [
                            {
                                "RuleType": "regex",
                                "RuleContent": "^(((¥|\\$)?(0|(([0]|([1-9][0-9]*(,\\d{3})*))\\.\\d{1,2}))(yuan|.?元)?)|(人民币)?([圆角分零壹贰叁肆伍陆柒捌玖拾佰仟万亿]+[圆角分]))$",
                                "ExtendParameters": null
                            }
                        ]
                    }
                },
                "COSRules": {
                    "Status": 0,
                    "RegexRule": {
                        "Operator": "or",
                        "Contents": [
                            {
                                "RuleContent": "(?<=\\W)(((¥|\\$)?(0|(([0]|([1-9][0-9]*(,\\d{3})*))\\.\\d{1,2}))(yuan|.?元)?)|(人民币)?([圆角分零壹贰叁肆伍陆柒捌玖拾佰仟万亿]+[圆角分]))(?=\\W)",
                                "IsIgnoreCase": true
                            }
                        ]
                    },
                    "KeywordRule": {
                        "Operator": "or",
                        "Contents": [
                            {
                                "RuleContent": "账户余额",
                                "IsIgnoreCase": true
                            },
                            {
                                "RuleContent": "Account Balance",
                                "IsIgnoreCase": true
                            },
                            {
                                "RuleContent": "AccountBalance",
                                "IsIgnoreCase": true
                            },
                            {
                                "RuleContent": "Account_Balance",
                                "IsIgnoreCase": true
                            }
                        ]
                    },
                    "IgnoreStringRule": {
                        "Operator": "or",
                        "Contents": null
                    },
                    "MaxMatch": 0
                }
            }
        ],
        "RequestId": "5af5a48c-6eb7-4d81-8df6-6d0e316a32ef"
    }
}
```

