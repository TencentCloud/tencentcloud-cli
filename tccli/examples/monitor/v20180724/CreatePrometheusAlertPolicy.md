**Example 1: 新增告警**

新增告警

Input: 

```
tccli monitor CreatePrometheusAlertPolicy --cli-unfold-argument  \
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
        "Id": "xx",
        "RequestId": "xx"
    }
}
```

**Example 2: 添加告警策略，告警渠道为Alertmanager**

添加告警策略，告警渠道为Alertmanager

Input: 

```
tccli monitor CreatePrometheusAlertPolicy --cli-unfold-argument  \
    --InstanceId xx \
    --AlertRule.Name xx \
    --AlertRule.Rules.0.Describe xx \
    --AlertRule.Rules.0.Name xx \
    --AlertRule.Rules.0.For xx \
    --AlertRule.Rules.0.Labels.0.Name xx \
    --AlertRule.Rules.0.Labels.0.Value xx \
    --AlertRule.Rules.0.Rule xx \
    --AlertRule.Rules.0.Template xx \
    --AlertRule.Rules.0.RuleState 0 \
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
    --AlertRule.Notification.ReceiverGroups xx \
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
        "Id": "alert-xxx",
        "RequestId": "3dfe620f-11b8-4301-b279-1fdadedf7a59"
    }
}
```

