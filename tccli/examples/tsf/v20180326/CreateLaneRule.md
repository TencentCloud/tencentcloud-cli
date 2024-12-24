**Example 1: 创建泳道规则**



Input: 

```
tccli tsf CreateLaneRule --cli-unfold-argument  \
    --RuleName app_rule \
    --Remark This is desc \
    --RuleTagList.0.TagName app_tag \
    --RuleTagList.0.TagOperator EQUAL \
    --RuleTagList.0.TagValue user \
    --RuleTagRelationship RELEATION_AND \
    --LaneId lane-y9o6w958
```

Output: 
```
{
    "Response": {
        "RequestId": "2d074caa-3966-42bd-a159-4bdd35534593",
        "Result": "lane-r-yojkwwpr"
    }
}
```

