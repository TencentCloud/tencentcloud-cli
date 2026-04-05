**Example 1: 示例1**



Input: 

```
tccli wedata UpdateStreamTaskAlarmInfo --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --AlarmInfo.MetricInfo.0.Metric BUSINESS_DELAY \
    --AlarmInfo.MetricInfo.0.Content {"TriggerType":120,"Duration":5,"Operator":5,"DurationUnit":"minute"} \
    --AlarmInfo.ChannelInfo.AlarmGroups.0.ChannelId 80255772556165939 \
    --AlarmInfo.ChannelInfo.AlarmGroups.0.ChannelName frankjl@tencent.com \
    --AlarmInfo.ChannelInfo.AlarmGroups.0.IsEmailChannel True \
    --AlarmInfo.ChannelInfo.AlarmGroups.0.AlarmConditions FAILURE \
    --AlarmInfo.ChannelInfo.AlarmGroups.0.ChannelType 1 \
    --TaskId ta-ad218e6d \
    --Enable 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": true
        },
        "RequestId": "c4fed4a8-ca1b-4f02-9a0b-89b78635d02c"
    }
}
```

