**Example 1: 查询生效的单元化规则**



Input: 

```
tccli tsf DescribeEnabledUnitRule --cli-unfold-argument  \
    --GatewayInstanceId gw-ins-szesmg28
```

Output: 
```
{
    "Response": {
        "RequestId": "480c7535-a008-4851-8a36-2d921893ea1e",
        "Result": {
            "CreatedTime": "2023-01-17 11:41:36",
            "Description": "sssase",
            "GatewayInstanceId": "gw-ins-szesmg28",
            "Id": "unit-rl-2kdqa2my",
            "Name": "test",
            "Status": "enabled",
            "UnitRuleItemList": [
                {
                    "CreatedTime": "2023-02-10 16:36:12",
                    "Description": "gsshhshs",
                    "DestNamespaceId": "namespace-vk5blxnv",
                    "DestNamespaceName": "heihuli-global_default",
                    "Id": "unit-item-04futugp",
                    "ItemIndex": 1,
                    "Name": "Rule1",
                    "Priority": 0,
                    "Relationship": "AND",
                    "UnitRuleId": "unit-rl-2kdqa2my",
                    "UnitRuleTagList": [
                        {
                            "Id": "unit-tag-s2v06uy5",
                            "TagField": "test",
                            "TagOperator": "IN",
                            "TagType": "U",
                            "TagValue": "test222",
                            "UnitRuleItemId": "unit-item-04futugp"
                        }
                    ],
                    "UpdatedTime": "2023-02-10 16:36:12"
                }
            ],
            "UpdatedTime": "2023-02-23 17:42:23"
        }
    }
}
```

