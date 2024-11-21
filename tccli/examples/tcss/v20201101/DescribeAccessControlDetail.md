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
            "ClientIP": "43.138.142.111",
            "ClusterID": "",
            "ClusterName": "",
            "ContainerId": "111411141114758f9ec06e76011da529da15bafdc83f2012d95ffa6382",
            "ContainerIsolateOperationSrc": "",
            "ContainerName": "/sweet_darwin",
            "ContainerNetStatus": "NORMAL",
            "ContainerNetSubStatus": "NONE",
            "EventCount": 1,
            "EventId": "5202566",
            "EventName": "访问控制-告警",
            "EventType": "ACCESS_CONTROL_ALERT",
            "FoundTime": "2024-10-11 11:03:00",
            "HostID": "11141114-6360-4fd4-bfc7-843162cb8116",
            "HostIP": "10.0.1.233",
            "ImageId": "sha256:11141114111403bb561b4c16bcb82328cfe5809ab675bb17ab3a16c517c9",
            "ImageName": "centos:7",
            "LatestFoundTime": "2024-10-11 11:03:00",
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
            "Description": "检测到系统命令被篡改",
            "MatchRule": {
                "ProcessPath": "/home/yunjing_testing_x86/events_trigger_x86",
                "RuleId": "200000000000000000000002",
                "RuleMode": "RULE_MODE_ALERT",
                "TargetFilePath": "/home/yunjing_testing_x86/GCONV_PATH=./pwnkit.so:."
            },
            "OperationTime": "1970-01-01 00:00:01",
            "Remark": "",
            "RuleId": "222222222222222222222222",
            "RuleName": "系统策略",
            "Solution": "排查是否为正常业务需要的系统命令替换"
        },
        "ParentProcessInfo": {
            "ProcessParam": "",
            "ProcessPath": "",
            "ProcessStartUser": "",
            "ProcessUserGroup": ""
        },
        "ProcessInfo": {
            "ProcessAuthority": "-rwxr-xr-x",
            "ProcessId": 2252097,
            "ProcessMd5": "",
            "ProcessName": "",
            "ProcessParam": "./events_trigger_x86 tamper_sys",
            "ProcessPath": "/home/yunjing_testing_x86/events_trigger_x86",
            "ProcessStartUser": "",
            "ProcessTree": "events_trigger_x86(2252097)|bash(2247285)|containerd-shim-runc-v2(2247257)|systemd(1)",
            "ProcessUserGroup": "0"
        },
        "RequestId": "a8db49cf-2c9a-492c-96e0-a87dcf75be23",
        "TamperedFileInfo": {
            "FileCreateTime": "2024-10-11 11:02:58",
            "FileDiff": "",
            "FileName": "pwnkit.so:.",
            "FilePath": "/home/yunjing_testing_x86/GCONV_PATH=./pwnkit.so:.",
            "FileSize": 24,
            "FileType": "UNKNOWN",
            "LatestTamperedFileMTime": "2024-10-11 11:02:58",
            "NewFile": ""
        }
    }
}
```

