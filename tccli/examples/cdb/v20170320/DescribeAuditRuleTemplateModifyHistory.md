**Example 1: 正确返回**



Input: 

```
tccli cdb DescribeAuditRuleTemplateModifyHistory --cli-unfold-argument  \
    --RuleTemplateIds cdb-art-8qx2kcr7 \
    --StartTime 2023-07-26 00:00:00 \
    --EndTime 2023-07-27 00:00:00 \
    --Limit 10 \
    --Offset 0 \
    --Order DESC
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Items": [
            {
                "TaskId": 1997098,
                "ModifyBeforeInfo": {
                    "RuleTemplateId": "cdb-art-8qx2kcr7",
                    "RuleTemplateName": "wy_1",
                    "RuleFilters": [
                        {
                            "Type": "sqlType",
                            "Compare": "EQS",
                            "Value": [
                                "DROP"
                            ]
                        }
                    ],
                    "AlarmLevel": 1,
                    "AlarmPolicy": 0,
                    "Description": "andyaudit"
                },
                "ModifyAfterInfo": {
                    "RuleTemplateId": "cdb-art-8qx2kcr7",
                    "RuleTemplateName": "wy_1",
                    "RuleFilters": [
                        {
                            "Type": "sqlType",
                            "Compare": "EQS",
                            "Value": [
                                "DROP",
                                "DELETE"
                            ]
                        }
                    ],
                    "AlarmLevel": 2,
                    "AlarmPolicy": 0,
                    "Description": "andyrule2"
                },
                "AffectedInstances": [
                    "cdb-nzg4gv35",
                    "cdb-12y4cjjd"
                ],
                "Operator": "700000579947",
                "UpdateTime": "2023-07-26 00:09:00"
            }
        ],
        "RequestId": "186905b7-756c-4aae-a403-a40568aa5952"
    }
}
```

