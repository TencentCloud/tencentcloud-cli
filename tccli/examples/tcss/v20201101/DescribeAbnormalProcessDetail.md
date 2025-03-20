**Example 1: 运行时异常进程事件详细信息**

运行时异常进程事件详细信息

Input: 

```
tccli tcss DescribeAbnormalProcessDetail --cli-unfold-argument  \
    --EventId 5202566
```

Output: 
```
{
    "Response": {
        "AncestorProcessInfo": {
            "ProcessParam": "-port 22",
            "ProcessPath": "/usr/local/bin/sshd",
            "ProcessStartUser": "root",
            "ProcessUserGroup": "root"
        },
        "EventBaseInfo": {
            "ClientIP": "106.55.163.***",
            "ClusterID": "cls-13nfdn****",
            "ClusterName": "demo-dev",
            "ContainerId": "1***5fe59dbd61071f16d6165480d381********",
            "ContainerIsolateOperationSrc": "system",
            "ContainerName": "/adoring_ishizaka",
            "ContainerNetStatus": "NORMAL",
            "ContainerNetSubStatus": "NONE",
            "EventCount": 2,
            "EventId": "10302329",
            "EventName": "异常进程事件-告警",
            "EventType": "FILE_ABNORMAL_READ",
            "FoundTime": "2024-10-21 15:55:45",
            "HostID": "1414-18a1-4775-9e3f-cdfc898********",
            "HostIP": "172.16.0.34",
            "ImageId": "sha256:1413413431fd9255658c128086395d3********",
            "ImageName": "alpine:latest",
            "LatestFoundTime": "2024-10-21 20:57:12",
            "Namespace": "default",
            "NodeID": "d41d8cd98f00******",
            "NodeName": "d41d8cd98f00*****",
            "NodeSubNetCIDR": "fe80::8132:1b51:52******",
            "NodeSubNetID": "sub-fn4nf***",
            "NodeSubNetName": "dev",
            "NodeType": "NORMAL",
            "NodeUniqueID": "fe8dfjf2d2****",
            "PodIP": "1.1.1.1",
            "PodName": "pod-dev",
            "PodStatus": "RUNNING",
            "Status": "EVENT_DEALED",
            "WorkloadType": "StatefulSet"
        },
        "EventDetail": {
            "Description": "检测到疑似反弹shell命令执行",
            "GroupName": "SYSTEM_DEFINED_RULE",
            "MatchRule": {
                "ProcessPath": "/usr/bin",
                "RuleId": "100000000000000000000004",
                "RuleLevel": "HIGH",
                "RuleMode": "RULE_MODE_ALERT"
            },
            "OperationTime": "2024-10-23 17:38:12",
            "Remark": "for dev",
            "RuleId": "124",
            "RuleName": "REVERSE_SHELL",
            "Solution": "排查反弹shell行为及目标地址是否为业务正常需要"
        },
        "ParentProcessInfo": {
            "ProcessId": 330852,
            "ProcessName": "containerd-shim",
            "ProcessParam": "containerd-shim -namespace moby -workdir /data/kubernetes/docker/containerd/daemon/io.containerd.runtime.v1.linux/moby/ /var/run/docker/runtime-runc",
            "ProcessPath": "/usr/bin/containerd-shim",
            "ProcessStartUser": "root",
            "ProcessUserGroup": "root"
        },
        "ProcessInfo": {
            "ProcessAuthority": "-rwxr-xr-x",
            "ProcessId": 2907621,
            "ProcessMd5": "8a5772dee965c8223aebc1225e*****",
            "ProcessName": "xenoncli",
            "ProcessParam": "xenoncli xenon ping",
            "ProcessPath": "/usr/local/bin/xenoncli",
            "ProcessStartUser": "root",
            "ProcessTree": "xenoncli(2907621)|containerd-shim(330852)|containerd(17863)|dockerd(17838)|systemd(1)",
            "ProcessUserGroup": "0"
        },
        "RequestId": "280ebb84-63c5-417e-95bd-e3160f6c8cdc"
    }
}
```

