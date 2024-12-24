**Example 1: 查询单元化规则详情**



Input: 

```
tccli tsf DescribeUnitRule --cli-unfold-argument  \
    --Id unit-rl-cgd3l6jo
```

Output: 
```
{
    "Response": {
        "RequestId": "02d58cd1-7651-4c6e-9836-e87ec8dadbcd",
        "Result": {
            "CreatedTime": "2024-12-23 11:14:17",
            "Description": null,
            "GatewayInstanceId": "gw-ins-szesmg28",
            "Id": "unit-rl-cgd3l6jo",
            "Name": "unit_provider",
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
    }
}
```

