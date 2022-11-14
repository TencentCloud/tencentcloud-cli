**Example 1: 规则执行结果列表查询**



Input: 

```
tccli wedata DescribeRuleExecResults --cli-unfold-argument  \
    --RuleGroupExecId 1 \
    --ProjectId 123456
```

Output: 
```
{
    "Response": {
        "Data": [
            {}
        ],
        "RequestId": "xx"
    }
}
```

