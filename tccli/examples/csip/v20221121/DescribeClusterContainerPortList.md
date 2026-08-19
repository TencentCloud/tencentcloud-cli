**Example 1: 查询容器关联端口列表示例**



Input: 

```
tccli csip DescribeClusterContainerPortList --cli-unfold-argument  \
    --ContainerId abc123def456
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "List": [
            {
                "ProcessName": "nginx",
                "ContainerPort": 80,
                "RunAs": "root",
                "ContainerPID": 1,
                "HostInnerIP": "10.0.1.15",
                "HostPublicIP": "203.0.113.10",
                "PublicPort": 30080,
                "ProtocolType": "TCP"
            }
        ],
        "RequestId": "5cd96106-1d72-466c-9bcf-9876543210ab"
    }
}
```

