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
            "Log": "xx"
        },
        "RequestId": "xx"
    }
}
```

