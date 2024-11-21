**Example 1: 查询容器信息**

查询容器信息

Input: 

```
tccli tcss DescribeAssetContainerDetail --cli-unfold-argument  \
    --ContainerId cndajlhcklanca
```

Output: 
```
{
    "Response": {
        "AppCnt": 0,
        "CPUUsage": 0,
        "ClusterID": "cls-5555555",
        "ClusterName": "集群名称",
        "Cmd": "",
        "ComponentCnt": 0,
        "ContainerName": "容器名称",
        "CreateTime": "2024-10-24 19:36:24",
        "HostID": "8bc803fd-d85d-47b8-9e2b-9644674be677",
        "HostIP": "1.1.1.1",
        "HostStatus": "ONLINE",
        "ImageCreateTime": "0001-01-01 08:05:43",
        "ImageID": "sha256:563af",
        "ImageName": "image:latest",
        "ImageSize": 0,
        "IsolateSource": "",
        "IsolateTime": "1970-01-01 00:00:01",
        "K8sMaster": "",
        "Mounts": [],
        "NetStatus": "NORMAL",
        "NetSubStatus": "NONE",
        "Network": {
            "EndpointID": "",
            "Gateway": "",
            "Ipv4": "",
            "Ipv6": "",
            "MAC": "",
            "Mode": "",
            "Name": "",
            "NetworkID": ""
        },
        "NodeID": "eks-111111",
        "NodeName": "节点名称",
        "NodeSubNetCIDR": "",
        "NodeSubNetID": "",
        "NodeSubNetName": "",
        "NodeType": "NORMAL",
        "NodeUniqueID": "27501aaed5e639693783321219989889",
        "POD": "tcss-aset-11-321",
        "PodIP": "1.1.1.1",
        "PodName": "tcss-asset-124321",
        "PodStatus": "Running",
        "PortCnt": 0,
        "ProcessCnt": 0,
        "PublicIP": "",
        "RamUsage": 0,
        "RequestId": "6954374b-bfcd-4751-8358-3e3682551514",
        "RunAs": "",
        "Status": "RUNNING",
        "WebServiceCnt": 0
    }
}
```

