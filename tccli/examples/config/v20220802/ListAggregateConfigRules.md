**Example 1: 账号组获取规则列表**

账号组获取规则列表

Input: 

```
tccli config ListAggregateConfigRules --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --OrderType  \
    --State ACTIVE \
    --ComplianceResult abc \
    --RuleName  \
    --RuleOwnerId 1 \
    --AccountGroupId ca-sdfs7734h24h3
```

Output: 
```
{
    "Response": {
        "RequestId": "149e116a-90ef-45f3-9d5d-3d77fd1c9eb3",
        "Items": [
            {
                "RegionsScope": [
                    "ap-shanghai"
                ],
                "TagsScope": [
                    {
                        "TagKey": "tag1",
                        "TagValue": "tag2"
                    }
                ],
                "ExcludeResourceIdsScope": [
                    "ins-asdasd"
                ],
                "Annotation": null,
                "CompliancePackId": "cp-xzfz0vu007feuhwi8auv",
                "CompliancePackName": "合规1",
                "ComplianceResult": "NON_COMPLIANT",
                "ConfigRuleId": "cr-13vkg9c31dixgabkepxe",
                "ConfigRuleInvokedTime": null,
                "CreateTime": "2022-11-16 14:25:01",
                "Description": "帐号访问管理中用户至少关联一个用户组，则符合规则。",
                "Identifier": "cam-user-group-bound",
                "IdentifierType": "SYSTEM",
                "InputParameter": [],
                "Labels": [],
                "ManageInputParameter": [],
                "ResourceType": [
                    "QCS::CAM::User"
                ],
                "RiskLevel": 3,
                "RuleName": "CAM访问管理子用户必须关联用户组",
                "ServiceFunction": null,
                "SourceCondition": [
                    {
                        "DesiredValue": "1",
                        "EmptyAs": "COMPLIANT",
                        "Operator": "GreaterOrEquals",
                        "Required": false,
                        "SelectPath": "$User.GroupBindNum"
                    }
                ],
                "Status": "ACTIVE",
                "TriggerType": [
                    {
                        "MaximumExecutionFrequency": "TwentyFour_Hours",
                        "MessageType": "ScheduledNotification"
                    }
                ]
            }
        ],
        "Total": 1
    }
}
```

