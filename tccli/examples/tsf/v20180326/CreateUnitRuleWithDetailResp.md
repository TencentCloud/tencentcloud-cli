**Example 1: 创建单元化规则**

创建单元化规则

Input: 

```
tccli tsf CreateUnitRuleWithDetailResp --cli-unfold-argument  \
    --GatewayInstanceId abc \
    --Name abc \
    --Description abc \
    --UnitRuleItemList.0.Id abc \
    --UnitRuleItemList.0.UnitRuleId abc \
    --UnitRuleItemList.0.Relationship abc \
    --UnitRuleItemList.0.DestNamespaceId abc \
    --UnitRuleItemList.0.DestNamespaceName abc \
    --UnitRuleItemList.0.Name abc \
    --UnitRuleItemList.0.Priority 0 \
    --UnitRuleItemList.0.Description abc \
    --UnitRuleItemList.0.UnitRuleTagList.0.UnitRuleItemId abc \
    --UnitRuleItemList.0.UnitRuleTagList.0.Id abc \
    --UnitRuleItemList.0.UnitRuleTagList.0.TagType abc \
    --UnitRuleItemList.0.UnitRuleTagList.0.TagField abc \
    --UnitRuleItemList.0.UnitRuleTagList.0.TagOperator abc \
    --UnitRuleItemList.0.UnitRuleTagList.0.TagValue abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "Id": "abc",
            "GatewayInstanceId": "abc",
            "Name": "abc",
            "Description": "abc",
            "Status": "abc",
            "UnitRuleItemList": [
                {
                    "Id": "abc",
                    "UnitRuleId": "abc",
                    "Relationship": "abc",
                    "DestNamespaceId": "abc",
                    "DestNamespaceName": "abc",
                    "Name": "abc",
                    "Priority": 0,
                    "Description": "abc",
                    "UnitRuleTagList": [
                        {
                            "UnitRuleItemId": "abc",
                            "Id": "abc",
                            "TagType": "abc",
                            "TagField": "abc",
                            "TagOperator": "abc",
                            "TagValue": "abc"
                        }
                    ],
                    "ItemIndex": 0,
                    "CreatedTime": "abc",
                    "UpdatedTime": "abc"
                }
            ],
            "CreatedTime": "abc",
            "UpdatedTime": "abc"
        },
        "RequestId": "abc"
    }
}
```

