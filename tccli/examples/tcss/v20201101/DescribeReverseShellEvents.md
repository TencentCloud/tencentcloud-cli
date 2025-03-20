**Example 1: 运行时反弹shell列表**

运行时反弹shell列表

Input: 

```
tccli tcss DescribeReverseShellEvents --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "EventSet": [
            {
                "ClusterID": "cls-dfw3e***",
                "ClusterName": "clsfoo***",
                "ContainerId": "b49a9fd917d30b736e76bff07a81e016bb1ced7bd9428b5d076628c80f8c62fd",
                "ContainerIsolateOperationSrc": "运行时安全/文件查杀",
                "ContainerName": "policy",
                "ContainerNetStatus": "NORMAL",
                "ContainerNetSubStatus": "NONE",
                "ContainerStatus": "RUNNING",
                "Description": "policy1",
                "DstAddress": "10.145.120.27:9000",
                "EventCount": 1,
                "EventId": "5075001",
                "FoundTime": "2024-10-24 08:38:49",
                "HostID": "0c4f6c1d-8215-43e2-8dcf-a4fb1db12f41",
                "HostIP": "10.150.14.152",
                "ImageId": "sha256:8415e883970de94c3131ff24ffaf9943ea81b3eca0c3d8d747b98581730bcdb6",
                "ImageName": "registry-cn-shanghai-vpc.ack.aliyuncs.com/acs/terway:v1.8.13",
                "LatestFoundTime": "2020-10-24 08:38:49",
                "NodeID": "mix-GOmf****",
                "NodeName": "i-node***",
                "NodeType": "NORMAL",
                "NodeUniqueID": "d41d8cd98f00b204e9800998ecf8427e",
                "PProcessName": "socat",
                "PodIP": "10.0.1.92",
                "PodName": "agent-test-2zrp7",
                "ProcessName": "dash",
                "ProcessPath": "/usr/bin/dash",
                "PublicIP": "10.0.1.92",
                "Remark": "myremark***",
                "Solution": "清理容器内反弹shell进程，检查容器内服务是否存在漏洞、弱密码等风险",
                "Status": "EVENT_UNDEAL"
            },
            {
                "ClusterID": "cls-dfw3e***",
                "ClusterName": "clsfoo***",
                "ContainerId": "b15e610a7f62b5873902923dfeee2d3ab642f76bd7f1777b3f628158c5b39586",
                "ContainerIsolateOperationSrc": "运行时安全/文件查杀",
                "ContainerName": "policy",
                "ContainerNetStatus": "NORMAL",
                "ContainerNetSubStatus": "NONE",
                "ContainerStatus": "RUNNING",
                "Description": "policy1",
                "DstAddress": "100.127.196.56:10556",
                "EventCount": 1,
                "EventId": "5067003",
                "FoundTime": "2020-10-24 08:03:10",
                "HostID": "fc472648-37ed-4946-a4c9-d72c75e162c4",
                "HostIP": "10.144.49.213",
                "ImageId": "sha256:41481aae5e2d135b2624fc09aa1875eb84c6472eaa0929f6d827699e67edd041",
                "ImageName": "registry",
                "LatestFoundTime": "2020-10-24 08:03:10",
                "NodeID": "mix-GOmf****",
                "NodeName": "i-node***",
                "NodeType": "NORMAL",
                "NodeUniqueID": "d41d8cd98f00b204e9800998ecf8427e",
                "PProcessName": "socat",
                "PodIP": "10.0.1.92",
                "PodName": "agent-test-2zrp7",
                "ProcessName": "dash",
                "ProcessPath": "/usr/bin/dash",
                "PublicIP": "10.0.1.92",
                "Remark": "myremark***",
                "Solution": "清理容器内反弹shell进程，检查容器内服务是否存在漏洞、弱密码等风险",
                "Status": "EVENT_UNDEAL"
            }
        ],
        "RequestId": "c73a7252-0f68-4203-8b18-52037ab5efd1",
        "TotalCount": 253
    }
}
```

