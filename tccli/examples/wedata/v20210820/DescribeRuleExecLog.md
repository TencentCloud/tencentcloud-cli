**Example 1: DescribeRuleExecResults**



Input: 

```
tccli wedata DescribeRuleExecLog --cli-unfold-argument  \
    --RuleGroupExecId 1 \
    --RuleExecId 1 \
    --ProjectId 19419899749824
```

Output: 
```
{
    "Response": {
        "Data": {
            "Finished": true,
            "Log": "[2024-04-09 21:10:24]-[INFO] the rule-sql list :"
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

