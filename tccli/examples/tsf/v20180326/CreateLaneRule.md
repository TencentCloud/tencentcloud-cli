**Example 1: 创建泳道规则**



Input: 

```
tccli tsf CreateLaneRule --cli-unfold-argument  \
    --RuleName 111 \
    --Remark 111 \
    --RuleTagList.0.TagName 11 \
    --RuleTagList.0.TagOperator EQUAL \
    --RuleTagList.0.TagValue 111 \
    --RuleTagRelationship RELEATION_AND \
    --LaneId lane-6ymrl42a
```

Output: 
```
{
    "RequestId": "643dda99-d5ca-4b6e-a394-a049e7478ae9",
    "Result": "lane-r-jy92q54a"
}
```

