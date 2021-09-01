**Example 1: 新增告警**



Input: 

```
tccli tke CreatePrometheusAlertRule --cli-unfold-argument  \
    --InstanceId xx \
    --AlertRule.TemplateId xx \
    --AlertRule.Name xx \
    --AlertRule.Rules.0.Describe xx \
    --AlertRule.Rules.0.Name xx \
    --AlertRule.Rules.0.For xx \
    --AlertRule.Rules.0.Labels.0.Name xx \
    --AlertRule.Rules.0.Labels.0.Value xx \
    --AlertRule.Rules.0.Rule xx \
    --AlertRule.Rules.0.Template xx \
    --AlertRule.Rules.0.Annotations.0.Name xx \
    --AlertRule.Rules.0.Annotations.0.Value xx \
    --AlertRule.Notification.WebHook xx \
    --AlertRule.Notification.RepeatInterval xx \
    --AlertRule.Notification.TimeRangeStart xx \
    --AlertRule.Notification.Enabled True \
    --AlertRule.Notification.PhoneNotifyOrder 1 \
    --AlertRule.Notification.PhoneInnerInterval 0 \
    --AlertRule.Notification.PhoneCircleInterval 0 \
    --AlertRule.Notification.NotifyWay xx \
    --AlertRule.Notification.ReceiverGroups 1 \
    --AlertRule.Notification.PhoneArriveNotice True \
    --AlertRule.Notification.PhoneCircleTimes 0 \
    --AlertRule.Notification.Type xx \
    --AlertRule.Notification.TimeRangeEnd xx \
    --AlertRule.Interval xx \
    --AlertRule.UpdatedAt xx \
    --AlertRule.Id xx
```

Output: 
```
{
    "Response": {
        "Id": "xx",
        "RequestId": "xx"
    }
}
```

