**Example 1: 更新单元化规则**



Input: 

```
tccli tsf UpdateUnitRule --cli-unfold-argument  \
    --Id unit-rl-cgd3l6jo \
    --Name user_unit \
    --Description This is desc \
    --UnitRuleItemList.0.Relationship AND \
    --UnitRuleItemList.0.DestNamespaceId namespace-vk5blxnv \
    --UnitRuleItemList.0.DestNamespaceName global_default \
    --UnitRuleItemList.0.Name unit_provider \
    --UnitRuleItemList.0.Priority 1 \
    --UnitRuleItemList.0.Description This is desc
```

Output: 
```
{
    "Response": {
        "RequestId": "487a19d8-1021-44a9-8350-52fee46686c4",
        "Result": true
    }
}
```

