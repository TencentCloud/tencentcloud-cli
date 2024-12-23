**Example 1: 查询单元化规则列表**



Input: 

```
tccli tsf DescribeUnitRules --cli-unfold-argument  \
    --GatewayInstanceId gw-ins-szesmg28 \
    --SearchWord gwInsName \
    --Status disabled \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "2cb64889-e6d8-45af-afdf-c12f874a6d08",
        "Result": [
            {
                "Content": [
                    {
                        "CreatedTime": "2024-12-23 11:14:17",
                        "Description": null,
                        "GatewayInstanceId": "gw-ins-szesmg28",
                        "Id": "unit-rl-cgd3l6jo",
                        "Name": "gwInsName",
                        "Status": "disabled",
                        "UnitRuleItemList": [
                            {
                                "CreatedTime": "2024-12-23 11:14:17",
                                "Description": "this is desc",
                                "DestNamespaceId": "namespace-vk5blxnv",
                                "DestNamespaceName": "global_default",
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
                                ],
                                "UpdatedTime": "2024-12-23 11:14:17"
                            }
                        ],
                        "UpdatedTime": "2024-12-23 11:14:17"
                    }
                ],
                "TotalCount": 1
            }
        ]
    }
}
```

