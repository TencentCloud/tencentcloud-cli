**Example 1: DescribeEscapeEventDetail**

 查询容器逃逸事件详情

Input: 

```
tccli tcss DescribeEscapeEventDetail --cli-unfold-argument  \
    --EventId dsfhuyh2r
```

Output: 
```
{
    "Response": {
        "AncestorProcessInfo": {
            "ProcessParam": "/usr/lib/systemd/systemd --switched-root --system --deserialize 18 ",
            "ProcessPath": "systemd",
            "ProcessStartUser": "root",
            "ProcessUserGroup": "root"
        },
        "EventBaseInfo": {
            "ClientIP": "159.75.90.111",
            "ClusterID": "cls-sdfw3f3",
            "ClusterName": "web-cluster",
            "ContainerId": "a960d85856c7a77cb504b638c56f59a28057",
            "ContainerIsolateOperationSrc": "",
            "ContainerName": "node1",
            "ContainerNetStatus": "NORMAL",
            "ContainerNetSubStatus": "NONE",
            "EventCount": 1,
            "EventId": "12486",
            "EventName": "敏感路径挂载",
            "EventType": "MOUNT_SENSITIVE_PTAH",
            "FoundTime": "2024-10-23 17:13:51",
            "HostID": "3b6b1bbc-1c7a-47e2-9ca8-e9c27ec9d068",
            "HostIP": "172.17.1.6",
            "ImageId": "sha256:b760a4831f5aab71c711f7537a107b751d0d0ce90dd32d8b358df3c5da385426",
            "ImageName": "-",
            "LatestFoundTime": "2024-10-23 17:13:51",
            "Namespace": "default",
            "NodeID": "web-node1",
            "NodeName": "VM-1-6-tencentos",
            "NodeSubNetCIDR": "172.16.0.0/24",
            "NodeSubNetID": "",
            "NodeSubNetName": "",
            "NodeType": "NORMAL",
            "NodeUniqueID": "",
            "PodIP": "",
            "PodName": "kube-system/cilium-m2gkw",
            "PodStatus": "",
            "Status": "EVENT_UNDEAL",
            "WorkloadType": ""
        },
        "EventDetail": {
            "Description": "容器（ID:5893711bb2...）挂载了敏感目录/lib/modules,/proc/sys/net,/proc/sys/kernel，存在容器逃逸的风险，当攻击者攻破容器后，可通过篡改该目录下的敏感文件，从而实现容器逃逸，获得宿主机系统的控制权限，威胁宿主机上其它容器及内网的安全。",
            "OperationTime": "1970-01-01 00:00:01",
            "Remark": "",
            "Solution": "修改挂载路径，只将必须的路径挂载到容器中，避免挂载敏感路径。"
        },
        "ParentProcessInfo": {
            "ProcessParam": "/usr/local/bin/containerd-shim-runc-v2 -namespace k8s.io -id 613d6792485871ca66ab6dc4d1c24e827e1ff4ae6aff87b187e40059cd3ba3b9 -address /run/containerd/containerd.sock ",
            "ProcessPath": "containerd-shim-runc-v2",
            "ProcessStartUser": "root",
            "ProcessUserGroup": "root"
        },
        "ProcessInfo": {
            "ProcessAuthority": "",
            "ProcessId": 2743103,
            "ProcessMd5": "81a7701a194c3a1179cfe4a7ac836626",
            "ProcessName": "runc",
            "ProcessParam": "cilium-agent --config-dir=/tmp/cilium/config-map",
            "ProcessPath": "/opt/containerd/bin/runc",
            "ProcessStartUser": "root",
            "ProcessTree": "runc(2743103)|containerd-shim-runc-v2(289436)|systemd(1)",
            "ProcessUserGroup": "root"
        },
        "RequestId": "c544fc31-7576-43aa-a4f3-b4c40656f67a"
    }
}
```

