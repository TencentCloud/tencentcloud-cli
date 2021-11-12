**Example 1: 创建泳道规则**



Input: 

```
tccli tsf CreateLaneRule --cli-unfold-argument  \
    --Remark xx \
    --RuleTagList.0.UpdateTime 0 \
    --RuleTagList.0.TagId xx \
    --RuleTagList.0.TagOperator xx \
    --RuleTagList.0.TagValue xx \
    --RuleTagList.0.TagName xx \
    --RuleTagList.0.LaneRuleId xx \
    --RuleTagList.0.CreateTime 0 \
    --RuleName xx \
    --ProgramIdList xx \
    --LaneId xx \
    --RuleTagRelationship xx
```

Output: 
```
{
    "Response": {
        "Result": "xx",
        "RequestId": "xx"
    }
}
```

