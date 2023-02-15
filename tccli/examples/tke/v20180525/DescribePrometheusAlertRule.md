**Example 1: 告警列表**

告警列表

Input: 

```
tccli tke DescribePrometheusAlertRule --cli-unfold-argument  \
    --InstanceId prom-dsjfhjgf
```

Output: 
```
{
    "Response": {
        "AlertRules": [
            {
                "Name": "test",
                "Rules": [
                    {
                        "Describe": "pod处于NotReady状态超过15分钟",
                        "Name": "KubePodNotReady",
                        "For": "15m",
                        "Labels": [
                            {
                                "Name": "severity",
                                "Value": "warning"
                            }
                        ],
                        "Rule": "sum by (cluster,namespace, pod) (\n  max by(cluster,namespace, pod) (\n    kube_pod_status_phase{job=\"kube-state-metrics\", phase=~\"Pending|Unknown\"}\n  ) * on(cluster,namespace, pod) group_left(owner_kind) topk by(cluster,namespace, pod) (\n    1, max by(cluster,namespace, pod, owner_kind) (kube_pod_owner{owner_kind!=\"Job\"})\n  )\n) > 0\n",
                        "Template": "集群 {{ $labels.cluster }}/namespace {{ $labels.namespace }}/Pod {{ $labels.pod }}处于NotReady状态超过15分钟"
                    }
                ],
                "Notification": {
                    "RepeatInterval": "5h",
                    "TimeRangeStart": "00:00:00",
                    "Enabled": true,
                    "PhoneNotifyOrder": [
                        1
                    ],
                    "PhoneInnerInterval": 0,
                    "PhoneCircleInterval": 0,
                    "NotifyWay": [
                        "CALL"
                    ],
                    "ReceiverGroups": [
                        1
                    ],
                    "PhoneArriveNotice": true,
                    "PhoneCircleTimes": 0,
                    "Type": "amp",
                    "TimeRangeEnd": "23:59:59"
                },
                "TemplateId": "",
                "Id": "alert-dsdgjsfj"
            }
        ],
        "Total": 1,
        "RequestId": "9446798b-df61-46df-91b7-dshjfdhjkasf"
    }
}
```

