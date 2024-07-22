**Example 1: 查询实例告警列表**

查询实例告警列表

Input: 

```
tccli monitor DescribePrometheusAlertPolicy --cli-unfold-argument  \
    --InstanceId prom-as3d2s1a \
    --Limit 1 \
    --Filters.0.Name Name \
    --Filters.0.Values alert-test \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "AlertRules": [
            {
                "Id": "alert-23a6d2ga",
                "Name": "alert-test",
                "TemplateId": "temp-as12sf12",
                "ClusterId": "",
                "Notification": {
                    "Enabled": true,
                    "Type": "amp",
                    "RepeatInterval": "5m",
                    "TimeRangeStart": "0:00:00",
                    "TimeRangeEnd": "23:59:59",
                    "ReceiverGroups": [
                        "notice-13hs61s2"
                    ],
                    "WebHook": "http://127.0.0.1:9090/alert",
                    "AlertManager": {
                        "ClusterType": "tke",
                        "ClusterId": "cls-a2df21xa",
                        "Url": "http://127.0.0.1:9090"
                    },
                    "PhoneNotifyOrder": [
                        1
                    ],
                    "PhoneCircleTimes": 0,
                    "PhoneInnerInterval": 0,
                    "PhoneCircleInterval": 0,
                    "PhoneArriveNotice": true,
                    "NotifyWay": [
                        "abc"
                    ]
                },
                "Rules": [
                    {
                        "Name": "rule-1",
                        "Rule": "up{} != 1",
                        "Labels": [
                            {
                                "Name": "level",
                                "Value": "warnning"
                            }
                        ],
                        "Template": "test alert",
                        "For": "5m",
                        "Describe": "test alert",
                        "Annotations": [
                            {
                                "Name": "creator",
                                "Value": "programer"
                            }
                        ],
                        "RuleState": 1
                    }
                ],
                "UpdatedAt": "2024-07-21 18:10:14"
            }
        ],
        "Total": 1,
        "RequestId": "3f04883c-eda1-4498-b024-d266baec6040"
    }
}
```

