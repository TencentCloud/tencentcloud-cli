**Example 1: 运行时反弹shell事件详细信息**



Input: 

```
tccli tcss DescribeReverseShellDetail --cli-unfold-argument  \
    --EventId 100
```

Output: 
```
{
    "Response": {
        "AncestorProcessInfo": {
            "ProcessParam": "bash",
            "ProcessPath": "/usr/bin/bash",
            "ProcessStartUser": "root",
            "ProcessUserGroup": "root"
        },
        "EventBaseInfo": {
            "ClientIP": "43.138.142.111",
            "ClusterID": "",
            "ClusterName": "",
            "ContainerId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe",
            "ContainerIsolateOperationSrc": "",
            "ContainerName": "/fervent_goodall",
            "ContainerNetStatus": "NORMAL",
            "ContainerNetSubStatus": "NONE",
            "EventCount": 1,
            "EventId": "464567",
            "EventName": "反弹shell",
            "EventType": "REVERSE_SHELL_EVENT_TYPE",
            "FoundTime": "2024-10-09 10:17:07",
            "HostID": "45641324-6360-4fd4-bfc7-843162cb8116",
            "HostIP": "10.0.1.233",
            "ImageId": "sha256:345234541324b561b4c16bcb82328cfe5809ab675bb17ab3a16c517c9",
            "ImageName": "centos:7",
            "LatestFoundTime": "2024-10-09 10:17:07",
            "Namespace": "",
            "NodeID": "",
            "NodeName": "k8s-node1",
            "NodeSubNetCIDR": "",
            "NodeSubNetID": "",
            "NodeSubNetName": "",
            "NodeType": "NORMAL",
            "NodeUniqueID": "",
            "PodIP": "",
            "PodName": "--",
            "PodStatus": "",
            "Status": "EVENT_UNDEAL",
            "WorkloadType": ""
        },
        "EventDetail": {
            "Description": "/fervent_goodall容器(ID:b18a9a3726...)内存在疑似反弹shell行为",
            "DstAddress": "175.178.80.251:3387",
            "OperationTime": "1970-01-01 00:00:01",
            "Remark": "",
            "Solution": "清理容器内反弹shell进程，检查容器内服务是否存在漏洞、弱密码等风险"
        },
        "ParentProcessInfo": {
            "ProcessId": 737356,
            "ProcessName": "bash",
            "ProcessParam": "sh -c bash ",
            "ProcessPath": "/usr/bin/bash",
            "ProcessStartUser": "",
            "ProcessUserGroup": ""
        },
        "ProcessInfo": {
            "ProcessAuthority": "-rwxr-xr-x",
            "ProcessId": 737357,
            "ProcessMd5": "81a7701a194c3a1179cfe4a7ac836626",
            "ProcessName": "bash",
            "ProcessParam": "bash -i",
            "ProcessPath": "/usr/bin/bash",
            "ProcessStartUser": "",
            "ProcessTree": "bash(737357)|bash(737356)|bash(733933)|containerd-shim-runc-v2(2178890)|systemd(1)",
            "ProcessUserGroup": "root"
        },
        "RequestId": "a14b6d46-6fa0-48bb-829f-acfa7a58b47a"
    }
}
```

