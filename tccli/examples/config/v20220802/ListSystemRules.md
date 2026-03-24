**Example 1: 获取规则列表**



Input: 

```
tccli config ListSystemRules --cli-unfold-argument  \
    --Limit 1 \
    --Keyword 测试2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": "2022-11-10 18:56:39",
                "Description": "帐号访问管理中用户至少关联一个用户组，则符合规则。",
                "Identifier": "cam-user-group-bound",
                "IdentifierType": "SYSTEM",
                "InputParameter": [],
                "Label": [
                    "用户",
                    "用户组"
                ],
                "ReferenceCount": 1,
                "ResourceType": [
                    "QCS::CAM::User"
                ],
                "RiskLevel": 3,
                "RuleName": "CAM访问管理子用户必须关联用户组",
                "ServiceFunction": "",
                "SourceCondition": [
                    {
                        "DesiredValue": "1",
                        "EmptyAs": "COMPLIANT",
                        "Operator": "GreaterOrEquals",
                        "Required": false,
                        "SelectPath": "$User.GroupBindNum"
                    }
                ],
                "TriggerType": [
                    "ScheduledNotification"
                ],
                "UpdateTime": "2022-11-10 18:56:39"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

