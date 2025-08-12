**Example 1: 更新灰度发布规则**



Input: 

```
tccli tsf ModifyLaneRule --cli-unfold-argument  \
    --RuleId lane-r-yqg4kmbd \
    --RuleName rule_app \
    --Remark This is desc \
    --RuleTagList.0.TagName user_tag \
    --RuleTagList.0.TagOperator EQUAL \
    --RuleTagList.0.TagValue 1 \
    --RuleTagRelationship RELEATION_AND \
    --LaneId lane-ap62k7ol \
    --Enable True
```

Output: 
```
{
    "Response": {
        "RequestId": "3ab21a41-5ab1-4988-8092-904541aa6877",
        "Result": true
    }
}
```

