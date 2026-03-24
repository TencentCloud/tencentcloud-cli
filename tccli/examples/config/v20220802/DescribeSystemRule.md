**Example 1: 获取预设规则详情**



Input: 

```
tccli config DescribeSystemRule --cli-unfold-argument  \
    --Identifier cam-user-group-bound
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "SystemConfigRule": {
            "UpdateTime": "xx",
            "SourceCondition": [
                {
                    "Operator": "xx",
                    "Required": true,
                    "EmptyAs": "xx",
                    "DesiredValue": "xx",
                    "SelectPath": "xx"
                }
            ],
            "ResourceType": [
                "cxzzcxzcx",
                "QCS::CAM::Policy",
                "QCS::CAM::Role"
            ],
            "TriggerType": [
                "ScheduledNotification",
                "ConfigurationItemChangeNotification"
            ],
            "RuleName": "xx",
            "Label": [
                "3"
            ],
            "RiskLevel": 3,
            "IdentifierType": "xx",
            "ReferenceCount": 1,
            "Identifier": "xx",
            "InputParameter": [
                {
                    "ValueType": "xx",
                    "Type": "xx",
                    "DefaultValue": "xx",
                    "ParameterKey": "xx",
                    "Description": "xx"
                }
            ],
            "CreateTime": "xx",
            "ServiceFunction": "xx",
            "Description": "xx"
        }
    }
}
```

