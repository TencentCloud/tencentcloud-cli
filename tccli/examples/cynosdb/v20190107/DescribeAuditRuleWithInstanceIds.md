**Example 1: 获取实例的审计规则**



Input: 

```
tccli cynosdb DescribeAuditRuleWithInstanceIds --cli-unfold-argument  \
    --InstanceIds cynosdbmysql-ins-6990cckk
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AuditRule": true,
                "AuditRuleFilters": [
                    {
                        "RuleFilters": [
                            {
                                "Compare": "INC",
                                "Type": "sql",
                                "Value": [
                                    "select"
                                ]
                            },
                            {
                                "Compare": "EQS",
                                "Type": "dbName",
                                "Value": [
                                    "testdb"
                                ]
                            }
                        ]
                    }
                ],
                "InstanceId": "cynosdbmysql-ins-6990cckk"
            }
        ],
        "RequestId": "a94950e4-7929-493d-97a6-4cd59dba466e",
        "TotalCount": 1
    }
}
```

