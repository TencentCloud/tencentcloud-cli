**Example 1: 创建泳道规则**



Input: 

```
tccli tsf CreateLaneRule --cli-unfold-argument  \
    --RuleName abc \
    --Remark abc \
    --RuleTagList.0.TagId abc \
    --RuleTagList.0.TagName abc \
    --RuleTagList.0.TagOperator abc \
    --RuleTagList.0.TagValue abc \
    --RuleTagList.0.LaneRuleId abc \
    --RuleTagList.0.CreateTime 0 \
    --RuleTagList.0.UpdateTime 0 \
    --RuleTagRelationship abc \
    --LaneId abc \
    --ProgramIdList abc
```

Output: 
```
{
    "Response": {
        "Result": "abc",
        "RequestId": "abc"
    }
}
```

