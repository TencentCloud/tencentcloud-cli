**Example 1: 示例**



Input: 

```
tccli wedata DescribeRuleGroupExecResultsByPageWithoutAuth --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Items": [
                {
                    "Status": 1,
                    "AlarmRuleCount": 1,
                    "DatabaseId": "xx",
                    "RuleGroupId": 1,
                    "RuleGroupExecId": 1,
                    "Permission": true,
                    "TableName": "xx",
                    "ExecDetail": "xx",
                    "ExecTime": "xx",
                    "TableId": "xx",
                    "TableOwnerName": "xx",
                    "TriggerType": 1,
                    "DatasourceId": "xx",
                    "TotalRuleCount": 1
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

