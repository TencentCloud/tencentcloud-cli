**Example 1: 新增告警**

新增告警，并选择使用模板

Input: 

```
tccli tke CreatePrometheusAlertRule --cli-unfold-argument  \
    --InstanceId prom-test \
    --AlertRule.TemplateId temp-test \
    --AlertRule.Name test \
    --AlertRule.Rules.0.Describe pod处于NotReady状态超过15分钟 \
    --AlertRule.Rules.0.Name KubePodNotReady \
    --AlertRule.Rules.0.For  \
    --AlertRule.Rules.0.Labels.0.Name severity \
    --AlertRule.Rules.0.Labels.0.Value warning \
    --AlertRule.Rules.0.Rule sum by (cluster,namespace, pod) (
  max by(cluster,namespace, pod) (
    kube_pod_status_phase{job="kube-state-metrics", phase=~"Pending|Unknown"}
  ) * on(cluster,namespace, pod) group_left(owner_kind) topk by(cluster,namespace, pod) (
    1, max by(cluster,namespace, pod, owner_kind) (kube_pod_owner{owner_kind!="Job"})
  )
) > 0
 \
    --AlertRule.Rules.0.Template 集群 {{ $labels.cluster }}/namespace {{ $labels.namespace }}/Pod {{ $labels.pod }}处于NotReady状态超过15分钟 \
    --AlertRule.Rules.0.Annotations.0.Name content \
    --AlertRule.Rules.0.Annotations.0.Value pod crash \
    --AlertRule.Notification.RepeatInterval 5h \
    --AlertRule.Notification.TimeRangeStart 00:00:00 \
    --AlertRule.Notification.Enabled True \
    --AlertRule.Notification.PhoneNotifyOrder 1 \
    --AlertRule.Notification.PhoneInnerInterval 0 \
    --AlertRule.Notification.PhoneCircleInterval 0 \
    --AlertRule.Notification.NotifyWay SMS \
    --AlertRule.Notification.ReceiverGroups 1 \
    --AlertRule.Notification.PhoneArriveNotice True \
    --AlertRule.Notification.PhoneCircleTimes 0 \
    --AlertRule.Notification.Type amp \
    --AlertRule.Notification.TimeRangeEnd 23:59:59
```

Output: 
```
{
    "Response": {
        "Id": "alert-123",
        "RequestId": "85438a95-6e0d-422e-a099-123456789"
    }
}
```

