**Example 1: 修改告警**

修改告警

Input: 

```
tccli monitor ModifyPrometheusAlertPolicy --cli-unfold-argument  \
    --InstanceId prom-jsgref \
    --AlertRule.Id alert-odhjeg \
    --AlertRule.Name 资源告警 \
    --AlertRule.TemplateId temp-cjhger \
    --AlertRule.Notification.Enabled True \
    --AlertRule.Notification.Type amp \
    --AlertRule.Notification.WebHook  \
    --AlertRule.Notification.AlertManager.ClusterType eks \
    --AlertRule.Notification.AlertManager.ClusterId cls-ojeg \
    --AlertRule.Notification.AlertManager.Url http://10.0.0.1:9000 \
    --AlertRule.Notification.RepeatInterval 5m \
    --AlertRule.Notification.TimeRangeStart 00:00:00 \
    --AlertRule.Notification.TimeRangeEnd 23:59:59 \
    --AlertRule.Notification.NotifyWay wechat \
    --AlertRule.Notification.ReceiverGroups skjehrsheb \
    --AlertRule.Notification.PhoneNotifyOrder 1 \
    --AlertRule.Notification.PhoneCircleTimes 0 \
    --AlertRule.Notification.PhoneInnerInterval 0 \
    --AlertRule.Notification.PhoneCircleInterval 0 \
    --AlertRule.Notification.PhoneArriveNotice True \
    --AlertRule.Rules.0.Annotations.0.Name summary \
    --AlertRule.Rules.0.Annotations.0.Value 磁盘使用率过高 \
    --AlertRule.Rules.0.Describe  \
    --AlertRule.Rules.0.For 2m \
    --AlertRule.Rules.0.Labels.0.Name severity \
    --AlertRule.Rules.0.Labels.0.Value warning \
    --AlertRule.Rules.0.Name 磁盘使用率过高 \
    --AlertRule.Rules.0.Rule 1- node_filesystem_avail_bytes  / node_filesystem_size_bytes > 0.85 \
    --AlertRule.Rules.0.RuleState 0 \
    --AlertRule.Rules.0.Template 磁盘使用率过高，实例: {{$labels.instance}}，ID: {{$labels.instance_id}}，当前值: {{ $value | humanizePercentage }}。 \
    --AlertRule.UpdatedAt 2024-07-15T16:46:42+08:00 \
    --AlertRule.ClusterId cls-iehgr
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

