**Example 1: 获取规则列表**



Input: 

```
tccli config ListConfigRules --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --OrderType  \
    --State ACTIVE \
    --RuleName 
```

Output: 
```
{
    "Response": {
        "RequestId": "149e116a-90ef-45f3-9d5d-3d77fd1c9eb3",
        "Items": [
            {
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
            },
            {
                "Annotation": null,
                "CompliancePackId": "",
                "CompliancePackName": null,
                "ComplianceResult": "NON_COMPLIANT",
                "ConfigRuleId": "cr-bdunf5kx3aywn0ac5bkk",
                "ConfigRuleInvokedTime": null,
                "CreateTime": "2022-11-16 14:22:59",
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
            },
            {
                "Annotation": null,
                "CompliancePackId": "",
                "CompliancePackName": null,
                "ComplianceResult": "NON_COMPLIANT",
                "ConfigRuleId": "cr-2d3brhnvyazqb9j1el6o",
                "ConfigRuleInvokedTime": null,
                "CreateTime": "2022-11-16 11:36:45",
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
        "Total": 3
    }
}
```

