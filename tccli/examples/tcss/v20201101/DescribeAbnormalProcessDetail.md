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
            "ClientIP": "106.55.163.111",
            "ClusterID": "",
            "ClusterName": "",
            "ContainerId": "111411411475fe59dbd61071f16d6165480d381e5fb3663d176d53669b",
            "ContainerIsolateOperationSrc": "",
            "ContainerName": "/adoring_ishizaka",
            "ContainerNetStatus": "NORMAL",
            "ContainerNetSubStatus": "NONE",
            "EventCount": 2,
            "EventId": "10302329",
            "EventName": "异常进程事件-告警",
            "EventType": "FILE_ABNORMAL_READ",
            "FoundTime": "2024-10-21 15:55:45",
            "HostID": "1414-18a1-4775-9e3f-cdfc89845157",
            "HostIP": "172.16.0.34",
            "ImageId": "sha256:1413413431fd9255658c128086395d3fa0aedd5a41ab6b034fd649d1a9260",
            "ImageName": "alpine:latest",
            "LatestFoundTime": "2024-10-21 20:57:12",
            "Namespace": "",
            "NodeID": "",
            "NodeName": "-",
            "NodeSubNetCIDR": "",
            "NodeSubNetID": "",
            "NodeSubNetName": "",
            "NodeType": "NORMAL",
            "NodeUniqueID": "",
            "PodIP": "",
            "PodName": "-",
            "PodStatus": "",
            "Status": "EVENT_DEALED",
            "WorkloadType": ""
        },
        "EventDetail": {
            "Description": "检测到疑似反弹shell命令执行",
            "GroupName": "SYSTEM_DEFINED_RULE",
            "MatchRule": {
                "ProcessPath": "-",
                "RuleId": "100000000000000000000004",
                "RuleLevel": "HIGH",
                "RuleMode": "RULE_MODE_ALERT"
            },
            "OperationTime": "2024-10-23 17:38:12",
            "Remark": "",
            "RuleId": "124",
            "RuleName": "REVERSE_SHELL",
            "Solution": "排查反弹shell行为及目标地址是否为业务正常需要"
        },
        "ParentProcessInfo": {
            "ProcessId": 0,
            "ProcessName": "",
            "ProcessParam": "",
            "ProcessPath": "",
            "ProcessStartUser": "",
            "ProcessUserGroup": ""
        },
        "ProcessInfo": {
            "ProcessAuthority": "-",
            "ProcessId": 0,
            "ProcessMd5": "",
            "ProcessName": "-",
            "ProcessParam": "sh -c \"bash >&1\"",
            "ProcessPath": "-",
            "ProcessStartUser": "",
            "ProcessTree": "-",
            "ProcessUserGroup": ""
        },
        "RequestId": "280ebb84-63c5-417e-95bd-e3160f6c8cdc"
    }
}
```

