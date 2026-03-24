**Example 1: 某个规则下资源的评估结果列表**

某个规则下资源的评估结果列表

Input: 

```
tccli config ListAggregateConfigRuleEvaluationResults --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --AccountGroupId ca-sdfs7734h24h3 \
    --ConfigRuleId cr-2d3brhnvyazqb9j1el6o \
    --ComplianceType NON_COMPLIANT
```

Output: 
```
{
    "Response": {
        "RequestId": "46e3ce2c-0fd0-4403-97de-590d85408248",
        "Items": [
            {
                "Annotation": {
                    "Configuration": "0",
                    "DesiredValue": "1",
                    "Operator": "GreaterOrEquals",
                    "Property": "$User.GroupBindNum"
                },
                "ResourceOwnerId": 1,
                "CompliancePackId": "",
                "ComplianceType": "NON_COMPLIANT",
                "ConfigRuleId": "cr-2d3brhnvyazqb9j1el6o",
                "ConfigRuleInvokedTime": "2022-11-16 11:36:47",
                "ConfigRuleName": "CAM访问管理子用户必须关联用户组",
                "InvokingEventMessageType": "[{\"messageType\":\"ScheduledNotification\",\"maximumExecutionFrequency\":{\"value\":\"TwentyFour_Hours\"}}]",
                "ResourceId": "100028282616",
                "ResourceOwnerName": "User1",
                "ResourceName": "2",
                "ResourceRegion": "global",
                "ResourceType": "QCS::CAM::User",
                "ResultRecordedTime": "2022-11-16 11:36:44",
                "RiskLevel": 3
            }
        ],
        "Total": 1
    }
}
```

