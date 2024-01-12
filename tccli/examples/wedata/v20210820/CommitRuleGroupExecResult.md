**Example 1: runner 结果上报**



Input: 

```
tccli wedata CommitRuleGroupExecResult --cli-unfold-argument  \
    --ProjectId 11 \
    --RuleGroupExecId 15 \
    --RuleGroupState COMPLETED \
    --RuleExecResults.0.RuleId 2 \
    --RuleExecResults.0.RuleExecId 9 \
    --RuleExecResults.0.State COMPLETED \
    --RuleExecResults.0.Data 100
```

Output: 
```
{
    "Response": {
        "Data": null,
        "RequestId": "abc"
    }
}
```

