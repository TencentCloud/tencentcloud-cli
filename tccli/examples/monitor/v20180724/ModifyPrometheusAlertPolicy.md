**Example 1: 修改告警**

修改告警

Input: 

```
tccli monitor ModifyPrometheusAlertPolicy --cli-unfold-argument  \
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
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

