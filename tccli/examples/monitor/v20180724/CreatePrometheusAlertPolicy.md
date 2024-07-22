**Example 1: 新增告警**

新增告警

Input: 

```
tccli monitor CreatePrometheusAlertPolicy --cli-unfold-argument  \
    --InstanceId prom-kshrsdf \
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
        "Id": "alert-ojnfb",
        "RequestId": "ac-khgr-iohvr"
    }
}
```

**Example 2: 添加告警策略，告警渠道为Alertmanager**

添加告警策略，告警渠道为Alertmanager

Input: 

```
tccli monitor CreatePrometheusAlertPolicy --cli-unfold-argument  \
    --InstanceId prom-kshrsdf \
    --AlertRule.Id alert-odhjeg \
    --AlertRule.Name 资源告警 \
    --AlertRule.TemplateId temp-cjhger \
    --AlertRule.Notification.AlertManager.ClusterId cls-ksjbr \
    --AlertRule.Notification.AlertManager.ClusterType eks \
    --AlertRule.Notification.AlertManager.Url http://10.0.0.1:9000/api/v1/alerts \
    --AlertRule.Notification.Enabled True \
    --AlertRule.Notification.NotifyWay None \
    --AlertRule.Notification.PhoneArriveNotice False \
    --AlertRule.Notification.PhoneCircleInterval 0 \
    --AlertRule.Notification.PhoneCircleTimes 0 \
    --AlertRule.Notification.PhoneInnerInterval 0 \
    --AlertRule.Notification.PhoneNotifyOrder None \
    --AlertRule.Notification.ReceiverGroups None \
    --AlertRule.Notification.RepeatInterval 5m \
    --AlertRule.Notification.TimeRangeEnd 23:59:59 \
    --AlertRule.Notification.TimeRangeStart 00:00:00 \
    --AlertRule.Notification.Type alertmanager \
    --AlertRule.Notification.WebHook  \
    --AlertRule.Rules.0.Annotations.0.Name summary \
    --AlertRule.Rules.0.Annotations.0.Value MySQL High CPU Usage \
    --AlertRule.Rules.0.Describe  \
    --AlertRule.Rules.0.For 5m \
    --AlertRule.Rules.0.Labels.0.Name severity \
    --AlertRule.Rules.0.Labels.0.Value warning \
    --AlertRule.Rules.0.Name MySQL High CPU Usage \
    --AlertRule.Rules.0.Rule avg by (instance_id,cluster_id,instance_region) (qce_cynosdb_mysql_cpuuserate_max) > 85 \
    --AlertRule.Rules.0.RuleState 0 \
    --AlertRule.Rules.0.Template MySQL cpu usage is higher than 85%. Instance ID: {{ $labels.instance_id }}, cluster ID: {{ $labels.cluster_id }}, region: {{ $labels.instance_region }} \
    --AlertRule.ClusterId cls-iehgr
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

