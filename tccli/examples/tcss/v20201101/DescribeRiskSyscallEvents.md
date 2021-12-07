**Example 1: 运行时高危系统调用接口**



Input: 

```
tccli tcss DescribeRiskSyscallEvents --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

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
                "FoundTime": "2020-02-02 13:00:00",
                "LatestFoundTime": "2020-09-22 00:00:00",
                "EventCount": 0,
                "Solution": "解决方案",
                "Description": "xxx事件",
                "SyscallName": "chroot",
                "Status": "EVENT_UNDEAL",
                "EventId": "xxx",
                "NodeName": "VM-0-13-centos",
                "PodName": "pod-name",
                "RuleExist": true,
                "Remark": "xx"
            }
        ],
        "TotalCount": 10,
        "RequestId": "0094843a-3023-1721-f7ed-b23f47ff3252"
    }
}
```

