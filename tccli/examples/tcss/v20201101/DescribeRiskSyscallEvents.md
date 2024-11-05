**Example 1: 运行时高危系统调用接口**

运行时高危系统调用接口

Input: 

```
tccli tcss DescribeRiskSyscallEvents --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EventSet": [
            {
                "ProcessName": "bash",
                "ProcessPath": "/home/work/",
                "ImageId": "81abdbc1427b1983b63a2e7bf48ab156a9a22",
                "ContainerId": "81abdbc1427b1983b63a2e7bf48ab156a9a22",
                "ImageName": "镜像名",
                "ContainerName": "/condescending_allen",
                "FoundTime": "2020-2-2 13:00:00",
                "Solution": "解决方案",
                "Description": "事件描述",
                "SyscallName": "chroot",
                "Status": "EVENT_UNDEAL",
                "EventId": "1",
                "NodeName": "VM-0-13-centos",
                "PodName": "pod-name",
                "Remark": "Remark",
                "RuleExist": true,
                "EventCount": 1,
                "LatestFoundTime": "2020-2-2 13:00:00",
                "ContainerNetStatus": "NORMAL",
                "ContainerNetSubStatus": "NONE",
                "ContainerIsolateOperationSrc": "RiskSyscall",
                "ContainerStatus": "RUNNING",
                "NodeType": "NORMAL",
                "ClusterID": "cls-dfw3e***",
                "PodIP": "10.0.1****",
                "NodeUniqueID": "d41d8cd98f00b204e9800998ecf8****",
                "PublicIP": "10.0.1****",
                "NodeID": "node-ins1a",
                "HostID": "27253917-572f-4eb5-9a55-99cc3a7a****",
                "HostIP": "10.4.4****",
                "ClusterName": "clsfoo***"
            }
        ],
        "RequestId": "48d997cd-353a-4457-929f-dc9183161462",
        "TotalCount": 0
    }
}
```

