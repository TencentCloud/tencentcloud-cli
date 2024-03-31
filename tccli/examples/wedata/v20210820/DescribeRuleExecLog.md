**Example 1: DescribeRuleExecResults**



Input: 

```
tccli wedata DescribeRuleExecLog --cli-unfold-argument  \
    --RuleGroupExecId 1 \
    --RuleExecId 1 \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Finished": true,
            "Log": "1"
        },
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

