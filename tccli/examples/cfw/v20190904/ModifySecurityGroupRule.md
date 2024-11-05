**Example 1: 编辑单条安全组规则**

编辑单条安全组规则

Input: 

```
tccli cfw ModifySecurityGroupRule --cli-unfold-argument  \
    --Data.0.BothWay 0 \
    --Data.0.Detail ignore 88.88.88.88 \
    --Data.0.OrderIndex 1 \
    --Data.0.Port -1/-1 \
    --Data.0.Protocol ANY \
    --Data.0.SourceId 88.88.88.88 \
    --Data.0.SourceType 0 \
    --Data.0.Strategy 2 \
    --Data.0.TargetId 0.0.0.0/0 \
    --Data.0.TargetType 9 \
    --Direction 1 \
    --Enable 1 \
    --SgRuleOriginSequence 1
```

Output: 
```
{
    "Response": {
        "NewRuleId": 51733,
        "RequestId": "c2baae07-ec29-445c-992f-a30ff49b64ba",
        "Status": 0
    }
}
```

