**Example 1: 创建一个模板**



Input: 

```
tccli tke CreatePrometheusTemplate --cli-unfold-argument  \
    --Template.Name abc \
    --Template.Describe abc \
    --Template.Level abc \
    --Template.AlertRules.0.Name abc \
    --Template.AlertRules.0.Rule abc \
    --Template.AlertRules.0.Labels.0.Name abc \
    --Template.AlertRules.0.Labels.0.Value abc \
    --Template.AlertRules.0.Template abc \
    --Template.AlertRules.0.For abc \
    --Template.AlertRules.0.Describe abc \
    --Template.AlertRules.0.Annotations.0.Name abc \
    --Template.AlertRules.0.Annotations.0.Value abc \
    --Template.AlertRules.0.RuleState 0 \
    --Template.RecordRules.0.Name abc \
    --Template.RecordRules.0.Config abc \
    --Template.RecordRules.0.TemplateId abc \
    --Template.ServiceMonitors.0.Name abc \
    --Template.ServiceMonitors.0.Config abc \
    --Template.ServiceMonitors.0.TemplateId abc \
    --Template.PodMonitors.0.Name abc \
    --Template.PodMonitors.0.Config abc \
    --Template.PodMonitors.0.TemplateId abc \
    --Template.TemplateId abc \
    --Template.UpdateTime abc \
    --Template.Version abc \
    --Template.IsDefault True \
    --Template.AlertDetailRules.0.Name abc \
    --Template.AlertDetailRules.0.Rules.0.Name abc \
    --Template.AlertDetailRules.0.Rules.0.Rule abc \
    --Template.AlertDetailRules.0.Rules.0.Labels.0.Name abc \
    --Template.AlertDetailRules.0.Rules.0.Labels.0.Value abc \
    --Template.AlertDetailRules.0.Rules.0.Template abc \
    --Template.AlertDetailRules.0.Rules.0.For abc \
    --Template.AlertDetailRules.0.Rules.0.Describe abc \
    --Template.AlertDetailRules.0.Rules.0.RuleState 0 \
    --Template.AlertDetailRules.0.UpdatedAt abc \
    --Template.AlertDetailRules.0.Notification.Enabled True \
    --Template.AlertDetailRules.0.Notification.RepeatInterval abc \
    --Template.AlertDetailRules.0.Notification.TimeRangeStart abc \
    --Template.AlertDetailRules.0.Notification.TimeRangeEnd abc \
    --Template.AlertDetailRules.0.Notification.NotifyWay abc \
    --Template.AlertDetailRules.0.Notification.ReceiverGroups 1 \
    --Template.AlertDetailRules.0.Notification.PhoneNotifyOrder 1 \
    --Template.AlertDetailRules.0.Notification.PhoneCircleTimes 0 \
    --Template.AlertDetailRules.0.Notification.PhoneInnerInterval 0 \
    --Template.AlertDetailRules.0.Notification.PhoneCircleInterval 0 \
    --Template.AlertDetailRules.0.Notification.PhoneArriveNotice True \
    --Template.AlertDetailRules.0.Notification.Type abc \
    --Template.AlertDetailRules.0.Notification.WebHook abc \
    --Template.AlertDetailRules.0.Id abc \
    --Template.AlertDetailRules.0.TemplateId abc \
    --Template.AlertDetailRules.0.Interval abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc",
        "TemplateId": "temp"
    }
}
```

