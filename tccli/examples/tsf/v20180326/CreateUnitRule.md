**Example 1: 创建单元化规则**



Input: 

```
tccli tsf CreateUnitRule --cli-unfold-argument  \
    --GatewayInstanceId gw-ins-szesmg28 \
    --Name unit_provider \
    --UnitRuleItemList.0.Relationship AND \
    --UnitRuleItemList.0.DestNamespaceId namespace-vk5blxnv \
    --UnitRuleItemList.0.DestNamespaceName heihuli-global_default \
    --UnitRuleItemList.0.Name Rule1 \
    --UnitRuleItemList.0.Description this is desc \
    --UnitRuleItemList.0.UnitRuleTagList.0.TagType U \
    --UnitRuleItemList.0.UnitRuleTagList.0.TagField user \
    --UnitRuleItemList.0.UnitRuleTagList.0.TagOperator IN \
    --UnitRuleItemList.0.UnitRuleTagList.0.TagValue 1
```

Output: 
```
{
    "Response": {
        "RequestId": "e3c4528c-0703-47da-8ef4-956d67463a6c",
        "Result": true
    }
}
```

