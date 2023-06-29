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
        "HostID": "abc",
        "HostIP": "abc",
        "ContainerName": "abc",
        "Status": "abc",
        "RunAs": "abc",
        "Cmd": "abc",
        "CPUUsage": 1,
        "RamUsage": 1,
        "ImageName": "abc",
        "ImageID": "abc",
        "POD": "abc",
        "K8sMaster": "abc",
        "ProcessCnt": 1,
        "PortCnt": 1,
        "ComponentCnt": 1,
        "AppCnt": 1,
        "WebServiceCnt": 1,
        "Mounts": [
            {
                "Type": "abc",
                "Source": "abc",
                "Destination": "abc",
                "Mode": "abc",
                "RW": true,
                "Propagation": "abc",
                "Name": "abc",
                "Driver": "abc"
            }
        ],
        "Network": {
            "EndpointID": "abc",
            "Mode": "abc",
            "Name": "abc",
            "NetworkID": "abc",
            "Gateway": "abc",
            "Ipv4": "abc",
            "Ipv6": "abc",
            "MAC": "abc"
        },
        "CreateTime": "abc",
        "ImageCreateTime": "abc",
        "ImageSize": 1,
        "HostStatus": "abc",
        "NetStatus": "abc",
        "NetSubStatus": "abc",
        "IsolateSource": "abc",
        "IsolateTime": "abc",
        "NodeID": "abc",
        "NodeName": "abc",
        "NodeSubNetID": "abc",
        "NodeSubNetName": "abc",
        "NodeSubNetCIDR": "abc",
        "PodName": "abc",
        "PodIP": "abc",
        "PodStatus": "abc",
        "ClusterID": "abc",
        "ClusterName": "abc",
        "NodeType": "abc",
        "NodeUniqueID": "abc",
        "PublicIP": "abc",
        "RequestId": "abc"
    }
}
```

