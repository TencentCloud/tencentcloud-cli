**Example 1: 运行时高危系统调用事件详细信息**

运行时高危系统调用事件详细信息

Input: 

```
tccli tcss DescribeRiskSyscallDetail --cli-unfold-argument  \
    --EventId ad134-cdadfa
```

Output: 
```
{
    "Response": {
        "AncestorProcessInfo": {
            "ProcessParam": "containerd --config /var/run/docker/containerd/containerd.toml --log-level warn",
            "ProcessPath": "/usr/bin/containerd",
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
            "Description": "sergid会导致运行进程的账号权限变更，可能带来安全风险",
            "OperationTime": "1970-01-01 00:00:01",
            "Remark": "user config",
            "Solution": "使用存在潜在风险的系统调用，可能导致容器逃逸。建议对于不常用的系统调用，禁止容器使用，并及时更新宿主机的系统漏洞",
            "SyscallName": "chroot"
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
        "RequestId": "d1dd6ed1-0424-4dc8-a3e1-*******"
    }
}
```

