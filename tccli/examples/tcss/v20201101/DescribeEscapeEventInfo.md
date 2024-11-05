**Example 1: DescribeEscapeEventInfo**

查询容器逃逸事件列表

Input: 

```
tccli tcss DescribeEscapeEventInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "EventSet": [
            {
                "ClusterID": "cls-fjivn***",
                "ClusterName": "dev-set",
                "ContainerId": "9294ea00cf80469f3604e2a38e725bf77c5a3ea522ce23bbf4d4dba8b4e149c9",
                "ContainerIsolateOperationSrc": "system",
                "ContainerName": "/test1",
                "ContainerNetStatus": "NORMAL",
                "ContainerNetSubStatus": "NONE",
                "ContainerStatus": "DESTROYED",
                "Description": "容器（ID: 9294ea00cf...) 中的进程bash对cgroup下的文件notify_on_release进行了修改，通过篡改该文件，可以实现容器逃逸，获得宿主机系统权限。",
                "EventCount": 192,
                "EventId": "33705186",
                "EventName": "利用cgroup机制逃逸",
                "EventType": "ESCAPE_CGROUPS",
                "FoundTime": "2024-08-23 16:41:03",
                "HostID": "3253189e-a107-4892-9bb9-03ad9****",
                "HostIP": "172.16.48.74",
                "ImageId": "sha256:5d0da3dc976460b72c77d94c8a1ad043720b0416bfc16c5*****",
                "ImageName": "centos:8",
                "LatestFoundTime": "2024-08-23 16:41:03",
                "NodeID": "d41d8cd98f00b204******",
                "NodeIP": "172.16.48.74",
                "NodeName": "VM-48-74-centos",
                "NodeType": "NORMAL",
                "NodeUniqueID": "d41d8cd98f00b204e9800****",
                "PodIP": "10.0.0.121",
                "PodName": "dev1",
                "PublicIP": "101.33.227.**",
                "Solution": "检查容器对应镜像是否存在漏洞或木马。修改容器启动参数，以普通权限启动容器。检查容器挂载目录，避免将/sys/fs/cgroup挂载到容器中。",
                "Status": "EVENT_UNDEAL"
            }
        ],
        "RequestId": "53e7bf79-dd62-40f9-be45-5849b1a372af",
        "TotalCount": 1021
    }
}
```

