**Example 1: ListOpsAlarmRule**

test1

Input: 

```
tccli wedata ListOpsAlarmRules --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --PageNumber 1 \
    --PageSize 10 \
    --AlarmType overtime
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
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
                    "AlarmRuleId": "4453641b-3051-4c66-9ff9-a73734c1d1c5",
                    "AlarmRuleName": "ruleName111",
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
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 24,
            "TotalPageNumber": 3
        },
        "RequestId": "ebabd563-dd4c-41e9-a184-68d3730d4038"
    }
}
```

