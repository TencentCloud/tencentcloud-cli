**Example 1: 查询审计规则模板信息**

查询审计规则模板信息

Input: 

```
tccli cynosdb DescribeAuditRuleTemplates --cli-unfold-argument  \
    --RuleTemplateNames template_test \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateAt": "2022-12-06 00:54:01",
                "Description": "all_template_des",
                "RuleFilters": [
                    {
                        "Compare": "INC",
                        "Type": "sqlType",
                        "Value": [
                            "ALTER"
                        ]
                    },
                    {
                        "Compare": "EQS",
                        "Type": "host",
                        "Value": [
                            "10.0.0.2"
                        ]
                    },
                    {
                        "Compare": "NEQ",
                        "Type": "user",
                        "Value": [
                            "andy"
                        ]
                    },
                    {
                        "Compare": "INC",
                        "Type": "dbName",
                        "Value": [
                            "db1"
                        ]
                    }
                ],
                "RuleTemplateId": "cynosdb-art-lcpm4as3",
                "RuleTemplateName": "template_test"
            }
        ],
        "RequestId": "a19ebcfb-8b35-40f4-85ee-383109c9134b",
        "TotalCount": 1
    }
}
```

