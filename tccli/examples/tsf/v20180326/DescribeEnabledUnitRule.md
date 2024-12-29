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
        "RequestId": "b378cebf-7ee2-4105-9ea0-58413051ea8e",
        "Result": {
            "CreatedTime": "2024-12-25 11:46:00",
            "Description": "this is desc",
            "GatewayInstanceId": "gw-ins-szesmg28",
            "Id": "unit-rl-u0643wrg",
            "Name": "rule_app",
            "Status": "enabled",
            "UnitRuleItemList": [
                {
                    "CreatedTime": "2024-12-25 11:46:00",
                    "Description": "this is desc",
                    "DestNamespaceId": "namespace-aem6w6nv",
                    "DestNamespaceName": "heihuli-c_default",
                    "Id": "unit-item-vnj5nf3m",
                    "ItemIndex": 1,
                    "Name": "rule_user",
                    "Priority": 0,
                    "Relationship": "AND",
                    "UnitRuleId": "unit-rl-u0643wrg",
                    "UnitRuleTagList": [
                        {
                            "Id": "unit-tag-8p9bpwh4",
                            "TagField": "user",
                            "TagOperator": "IN",
                            "TagType": "U",
                            "TagValue": "1",
                            "UnitRuleItemId": "unit-item-vnj5nf3m"
                        }
                    ],
                    "UpdatedTime": "2024-12-25 11:46:00"
                }
            ],
            "UpdatedTime": "2024-12-25 11:50:01"
        }
    }
}
```

