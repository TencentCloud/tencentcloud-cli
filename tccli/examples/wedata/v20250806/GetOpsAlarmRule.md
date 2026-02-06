**Example 1: GetOpsAlarmRuleDetail**



Input: 

```
tccli wedata GetOpsAlarmRule --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --AlarmRuleId d736b8ba-b6d9-4a21-824a-84bdda3d9731
```

Output: 
```
{
    "Response": {
        "Data": {
            "AlarmGroups": [
                {
                    "AlarmEscalationInterval": 0,
                    "AlarmEscalationRecipientIds": [],
                    "AlarmRecipientIds": [],
                    "AlarmRecipientType": 2,
                    "AlarmWays": [
                        "1"
                    ],
                    "NotificationFatigue": {
                        "NotifyCount": 1,
                        "NotifyInterval": 5,
                        "QuietIntervals": []
                    },
                    "WebHooks": []
                }
            ],
            "AlarmLevel": 1,
            "AlarmRuleDetail": {
                "DataBackfillOrRerunTimeOutExtInfo": null,
                "DataBackfillOrRerunTrigger": 1,
                "ProjectInstanceStatisticsAlarmInfoList": null,
                "ReconciliationExtInfo": null,
                "TimeOutExtInfo": [
                    {
                        "Hour": null,
                        "Min": 1,
                        "RuleType": 1,
                        "ScheduleTimeZone": null,
                        "Type": 1
                    }
                ],
                "Trigger": 2
            },
            "AlarmRuleId": "d736b8ba-b6d9-4a21-824a-84bdda3d9731",
            "AlarmRuleName": "ruleName222",
            "AlarmTypes": [
                "failure"
            ],
            "BundleId": "",
            "BundleInfo": "",
            "Description": "",
            "MonitorObjectIds": [
                "832b83ea-d285-43bd-b4bb-5a268aa8cb50"
            ],
            "MonitorObjectType": 2,
            "Status": 1
        },
        "RequestId": "2bd5ce52-4cc5-4338-aa40-b203ef6160ff"
    }
}
```

