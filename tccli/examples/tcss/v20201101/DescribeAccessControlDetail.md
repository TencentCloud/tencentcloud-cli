**Example 1: 运行时访问控制事件详细信息**

运行时访问控制事件详细信息

Input: 

```
tccli tcss DescribeAccessControlDetail --cli-unfold-argument  \
    --EventId 5202566
```

Output: 
```
{
    "Response": {
        "AncestorProcessInfo": {
            "ProcessParam": "/usr/bin/containerd-shim-runc-v2 -namespace moby -address /run/containerd/containerd.sock",
            "ProcessPath": "/usr/bin/containerd-shim-runc-v2",
            "ProcessStartUser": "0",
            "ProcessUserGroup": "0"
        },
        "EventBaseInfo": {
            "ClientIP": "175.178.113.111",
            "ClusterID": "cls-demo1",
            "ClusterName": "web-demo",
            "ContainerId": "75D3326A-9B9C-4275-895A-16FDA1*****",
            "ContainerIsolateOperationSrc": "ContainerIsolateOperationSrc",
            "ContainerName": "/k8s_xenon_mysql-tce-cwp-mysql-2_sso_c9fdfba4-e31a-46bc-a43a-****",
            "ContainerNetStatus": "NORMAL",
            "ContainerNetSubStatus": "NONE",
            "EventCount": 130,
            "EventId": "5124493",
            "EventName": "高危系统调用",
            "EventType": "RISK_SYSCALL_EVENT_TYPE",
            "FoundTime": "2024-10-23 00:05:17",
            "HostID": "11141114-66fd-4171-93eb-2f4fc36ef1e1",
            "HostIP": "10.0.0.105",
            "ImageId": "sha256:11141114e95dce36e8455cf657e1e54d74bb8fac6111411141114",
            "ImageName": "registry.tce.com/service-vendors/mysql-xenon:8.0.32-20240524-155426-11141114.rhel.amd64",
            "LatestFoundTime": "2024-10-23 17:02:47",
            "Namespace": "default",
            "NodeID": "pod-dj4xjf***",
            "NodeName": "tcs-10-0-0-105",
            "NodeSubNetCIDR": "fe80::8132:1b51:5********",
            "NodeSubNetID": "subnet-dfj4***",
            "NodeSubNetName": "default",
            "NodeType": "NORMAL",
            "NodeUniqueID": "node-4jfjfgdnvnd****",
            "PodIP": "10.0.0.11",
            "PodName": "demonset",
            "PodStatus": "running",
            "Status": "EVENT_UNDEAL",
            "WorkloadType": "StatefulSet"
        },
        "EventDetail": {
            "Description": "检测到系统命令被篡改",
            "MatchRule": {
                "ProcessPath": "/home/yunjing_testing_x86/events_trigger_x86",
                "RuleId": "200000000000000000000002",
                "RuleMode": "RULE_MODE_ALERT",
                "TargetFilePath": "/home/yunjing_testing_x86/GCONV_PATH=./pwnkit.so:."
            },
            "OperationTime": "1970-01-01 00:00:01",
            "Remark": "demoset",
            "RuleId": "222222222222222222222222",
            "RuleName": "系统策略",
            "Solution": "排查是否为正常业务需要的系统命令替换"
        },
        "ParentProcessInfo": {
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
        "RequestId": "a8db49cf-2c9a-492c-96e0-a87dcf75be23",
        "TamperedFileInfo": {
            "FileCreateTime": "2024-10-11 11:02:58",
            "FileDiff": "UNKNOW",
            "FileName": "pwnkit.so:.",
            "FilePath": "/home/yunjing_testing_x86/GCONV_PATH=./pwnkit.so:.",
            "FileSize": 24,
            "FileType": "UNKNOWN",
            "LatestTamperedFileMTime": "2024-10-11 11:02:58",
            "NewFile": "default.txt"
        }
    }
}
```

