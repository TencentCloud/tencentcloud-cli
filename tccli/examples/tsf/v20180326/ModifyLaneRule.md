**Example 1: 更新泳道规则**



Input: 

```
tccli tsf ModifyLaneRule --cli-unfold-argument  \
    --RuleId 1 \
    --RuleName 1 \
    --Remark 1 \
    --RuleTagList 1 \
    --RuleTagRelationship RELEATION_AND \
    --LaneId lane-fdsjakhfds \
    --Enable 1
```

Output: 
```
{
    "RequestId": "e448ce99-83af-47cd-b422-a203aa18d862",
    "Result": true
}
```

