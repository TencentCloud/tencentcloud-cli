**Example 1: 新增告警**

新增告警

Input: 

```
tccli monitor CreatePrometheusAlertPolicy --cli-unfold-argument  \
    --InstanceId abc \
    --AlertRule.Id abc \
    --AlertRule.Name abc \
    --AlertRule.TemplateId abc \
    --AlertRule.Notification.Enabled True \
    --AlertRule.Notification.Type abc \
    --AlertRule.Notification.WebHook abc \
    --AlertRule.Notification.AlertManager.ClusterType abc \
    --AlertRule.Notification.AlertManager.ClusterId abc \
    --AlertRule.Notification.AlertManager.Url abc \
    --AlertRule.Notification.RepeatInterval abc \
    --AlertRule.Notification.TimeRangeStart abc \
    --AlertRule.Notification.TimeRangeEnd abc \
    --AlertRule.Notification.NotifyWay abc \
    --AlertRule.Notification.ReceiverGroups abc \
    --AlertRule.Notification.PhoneNotifyOrder 1 \
    --AlertRule.Notification.PhoneCircleTimes 0 \
    --AlertRule.Notification.PhoneInnerInterval 0 \
    --AlertRule.Notification.PhoneCircleInterval 0 \
    --AlertRule.Notification.PhoneArriveNotice True \
    --AlertRule.Rules.0.Name abc \
    --AlertRule.Rules.0.Rule abc \
    --AlertRule.Rules.0.Labels.0.Name abc \
    --AlertRule.Rules.0.Labels.0.Value abc \
    --AlertRule.Rules.0.Template abc \
    --AlertRule.Rules.0.For abc \
    --AlertRule.Rules.0.Describe abc \
    --AlertRule.Rules.0.Annotations.0.Name abc \
    --AlertRule.Rules.0.Annotations.0.Value abc \
    --AlertRule.Rules.0.RuleState 0 \
    --AlertRule.UpdatedAt abc \
    --AlertRule.ClusterId abc
```

Output: 
```
{
    "Response": {
        "Id": "ac",
        "RequestId": "ac"
    }
}
```

**Example 2: 添加告警策略，告警渠道为Alertmanager**

添加告警策略，告警渠道为Alertmanager

Input: 

```
tccli monitor CreatePrometheusAlertPolicy --cli-unfold-argument  \
    --InstanceId abc \
    --AlertRule.Id abc \
    --AlertRule.Name abc \
    --AlertRule.TemplateId abc \
    --AlertRule.Notification.Enabled True \
    --AlertRule.Notification.Type abc \
    --AlertRule.Notification.WebHook abc \
    --AlertRule.Notification.AlertManager.ClusterType abc \
    --AlertRule.Notification.AlertManager.ClusterId abc \
    --AlertRule.Notification.AlertManager.Url abc \
    --AlertRule.Notification.RepeatInterval abc \
    --AlertRule.Notification.TimeRangeStart abc \
    --AlertRule.Notification.TimeRangeEnd abc \
    --AlertRule.Notification.NotifyWay abc \
    --AlertRule.Notification.ReceiverGroups abc \
    --AlertRule.Notification.PhoneNotifyOrder 1 \
    --AlertRule.Notification.PhoneCircleTimes 0 \
    --AlertRule.Notification.PhoneInnerInterval 0 \
    --AlertRule.Notification.PhoneCircleInterval 0 \
    --AlertRule.Notification.PhoneArriveNotice True \
    --AlertRule.Rules.0.Name abc \
    --AlertRule.Rules.0.Rule abc \
    --AlertRule.Rules.0.Labels.0.Name abc \
    --AlertRule.Rules.0.Labels.0.Value abc \
    --AlertRule.Rules.0.Template abc \
    --AlertRule.Rules.0.For abc \
    --AlertRule.Rules.0.Describe abc \
    --AlertRule.Rules.0.Annotations.0.Name abc \
    --AlertRule.Rules.0.Annotations.0.Value abc \
    --AlertRule.Rules.0.RuleState 0 \
    --AlertRule.UpdatedAt abc \
    --AlertRule.ClusterId abc
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

