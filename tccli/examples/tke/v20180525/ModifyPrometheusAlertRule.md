**Example 1: 修改告警**

修改告警

Input: 

```
tccli tke ModifyPrometheusAlertRule --cli-unfold-argument  \
    --InstanceId prom-sdgfsdhg \
    --AlertRule.TemplateId  \
    --AlertRule.Name test \
    --AlertRule.Rules.0.Describe pod处于NotReady状态超过15分钟 \
    --AlertRule.Rules.0.Name KubePodNotReady \
    --AlertRule.Rules.0.For 15m \
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
    --AlertRule.Rules.0.Template  \
    --AlertRule.Rules.0.Annotations.0.Name content \
    --AlertRule.Rules.0.Annotations.0.Value pod not ready \
    --AlertRule.Notification.RepeatInterval 5h \
    --AlertRule.Notification.TimeRangeStart 00:00:00 \
    --AlertRule.Notification.Enabled True \
    --AlertRule.Notification.PhoneNotifyOrder 1 \
    --AlertRule.Notification.PhoneInnerInterval 180 \
    --AlertRule.Notification.PhoneCircleInterval 180 \
    --AlertRule.Notification.NotifyWay CALL \
    --AlertRule.Notification.ReceiverGroups 1 \
    --AlertRule.Notification.PhoneArriveNotice True \
    --AlertRule.Notification.PhoneCircleTimes 3 \
    --AlertRule.Notification.Type amp \
    --AlertRule.Notification.TimeRangeEnd 23:59:59 \
    --AlertRule.Id alert-dsdafg
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

