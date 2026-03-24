**Example 1: 获取规则详情**



Input: 

```
tccli config DescribeConfigRule --cli-unfold-argument  \
    --RuleId cr-25yzg5my0ggw5zxuxkhe
```

Output: 
```
{
    "Response": {
        "RequestId": "e4cd38fd-3c1c-415f-8b9a-d56332d1a3c7",
        "ConfigRule": {
            "Annotation": null,
            "CompliancePackId": "",
            "CompliancePackName": null,
            "ComplianceResult": null,
            "ConfigRuleId": "cr-2d3brhnvyazqb9j1el6o",
            "ConfigRuleInvokedTime": "2022-11-16 14:11:50",
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
    }
}
```

