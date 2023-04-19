**Example 1: 查询未恢复告警**

查询指定时间段内尚未恢复的告警

Input: 

```
tccli cls DescribeAlertRecordHistory --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --From 1681401600000 \
    --To 1681487999999 \
    --Filters.0.Key status \
    --Filters.0.Values 0
```

Output: 
```
{
    "Response": {
        "Records": [
            {
                "RecordId": "977c26df-d47f-404c-b0d2-c9ccd73f1407",
                "AlarmId": "alarm-98ba728c-3888-4049-b510-20e26de53894",
                "AlarmName": "TKE Demo事件日志告警策略_100001001014",
                "TopicId": "0337bf0c-7a38-456a-bd59-ba2feaa55195",
                "TopicName": "TKE Demo事件日志日志主题_100001001014",
                "Region": "ap-chongqing",
                "Trigger": "$1.Warning事件数 > 0",
                "TriggerCount": 1,
                "AlarmPeriod": 15,
                "Notices": [
                    {
                        "Name": "TKE Demo事件日志通知渠道组_100001001014",
                        "AlarmNoticeId": "notice-117dbad3-cc1b-4455-b112-76b0658dddc2"
                    }
                ],
                "Duration": 90,
                "Status": 0,
                "CreateTime": 1681439122000,
                "AlarmLevel": 0,
                "MonitorObjectType": 0,
                "GroupTriggerCondition": []
            },
            {
                "RecordId": "1be40239-505f-4f1a-a6aa-4b71a9757d8a",
                "AlarmId": "alarm-7be9386d-01e9-4b8b-a54e-fe00f6b15b1d",
                "AlarmName": "TKE Demo审计日志告警策略_100001001014",
                "TopicId": "6a4adc63-d145-4da4-a0e7-72bb1a9f8fcd",
                "TopicName": "TKE Demo审计日志日志主题_100001001014",
                "Region": "ap-chongqing",
                "Trigger": "$1.操作次数 >10",
                "TriggerCount": 1,
                "AlarmPeriod": 15,
                "Notices": [
                    {
                        "Name": "TKE Demo审计日志通知渠道组_100001001014",
                        "AlarmNoticeId": "notice-f7d09113-b870-4f98-b99d-38d8ecf5393b"
                    }
                ],
                "Duration": 90,
                "Status": 0,
                "CreateTime": 1681438941000,
                "AlarmLevel": 0,
                "MonitorObjectType": 0,
                "GroupTriggerCondition": []
            }
        ],
        "TotalCount": 2,
        "RequestId": "431449a5-95ab-4168-9a0e-7db48692d917"
    }
}
```

