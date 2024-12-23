**Example 1: 创建单元化规则**

创建单元化规则

Input: 

```
tccli tsf CreateUnitRuleWithDetailResp --cli-unfold-argument  \
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
        "RequestId": "ef567ab9-7b1b-43d7-92bc-67399ad748e4",
        "Result": {
            "UpdatedTime": null,
            "CreatedTime": null,
            "Description": null,
            "GatewayInstanceId": "gw-ins-szesmg28",
            "Id": "unit-rl-cgd3l6jo",
            "Name": "unit_provider",
            "Status": "disabled",
            "UnitRuleItemList": [
                {
                    "UpdatedTime": null,
                    "CreatedTime": null,
                    "Description": "this is desc",
                    "DestNamespaceId": "namespace-vk5blxnv",
                    "DestNamespaceName": "heihuli-global_default",
                    "Id": "unit-item-ghpuh9rn",
                    "ItemIndex": 1,
                    "Name": "Rule1",
                    "Priority": 0,
                    "Relationship": "AND",
                    "UnitRuleId": "unit-rl-cgd3l6jo",
                    "UnitRuleTagList": [
                        {
                            "Id": "unit-tag-vmhijoic",
                            "TagField": "user",
                            "TagOperator": "IN",
                            "TagType": "U",
                            "TagValue": "1",
                            "UnitRuleItemId": "unit-item-ghpuh9rn"
                        }
                    ]
                }
            ]
        }
    }
}
```

