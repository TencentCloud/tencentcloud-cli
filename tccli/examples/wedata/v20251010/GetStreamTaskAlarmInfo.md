**Example 1: shili1**



Input: 

```
tccli wedata GetStreamTaskAlarmInfo --cli-unfold-argument  \
    --TaskId ta-ad218e6d \
    --WorkspaceId 17663856806379896 \
    --TaskVersion tv-c54d0523
```

Output: 
```
{
    "Response": {
        "Data": {
            "AlarmInfo": {
                "ChannelInfo": {
                    "AlarmGroups": [
                        {
                            "AlarmConditions": [
                                "FAILURE"
                            ],
                            "ChannelId": "80255772556165939",
                            "ChannelName": "frankjl@tencent.com",
                            "ChannelType": 1,
                            "IsEmailChannel": true
                        }
                    ],
                    "AlarmId": "",
                    "AlarmMonitorType": "",
                    "DoNotDisturbWhenManuallyTerminated": false,
                    "DoNotDisturbWhenSkipped": false
                },
                "MetricInfo": [
                    {
                        "Content": "{\"TriggerType\":120,\"Duration\":5,\"Operator\":5,\"DurationUnit\":\"minute\"}",
                        "Metric": "BUSINESS_DELAY"
                    }
                ]
            }
        },
        "RequestId": "5a4b091d-04e3-406a-904a-ff51781296cc"
    }
}
```

