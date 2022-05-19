**Example 1: 修改告警**



Input: 

```
tccli tke ModifyPrometheusAlertPolicy --cli-unfold-argument  \
    --InstanceId xx \
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
    --AlertRule.Notification.AlertManager.Url xx \
    --AlertRule.Notification.AlertManager.ClusterId xx \
    --AlertRule.Notification.AlertManager.ClusterType xx \
    --AlertRule.Notification.RepeatInterval xx \
    --AlertRule.Notification.WebHook xx \
    --AlertRule.Notification.Enabled True \
    --AlertRule.Notification.PhoneNotifyOrder 1 \
    --AlertRule.Notification.PhoneInnerInterval 0 \
    --AlertRule.Notification.PhoneCircleInterval 0 \
    --AlertRule.Notification.NotifyWay xx \
    --AlertRule.Notification.ReceiverGroups 1 \
    --AlertRule.Notification.PhoneArriveNotice True \
    --AlertRule.Notification.PhoneCircleTimes 0 \
    --AlertRule.Notification.TimeRangeStart xx \
    --AlertRule.Notification.Type xx \
    --AlertRule.Notification.TimeRangeEnd xx \
    --AlertRule.TemplateId xx \
    --AlertRule.ClusterId xx \
    --AlertRule.UpdatedAt xx \
    --AlertRule.Id xx
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

