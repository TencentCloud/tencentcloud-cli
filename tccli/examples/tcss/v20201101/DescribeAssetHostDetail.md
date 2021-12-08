**Example 1: 查询主机详细信息**



Input: 

```
tccli tcss DescribeAssetHostDetail --cli-unfold-argument  \
    --HostId dskaldjskld
```

Output: 
```
{
    "Response": {
        "Group": "xx",
        "OsName": "xx",
        "DockerRootDir": "xx",
        "DockerFileSystemDriver": "xx",
        "Status": "xx",
        "PublicIp": "xx",
        "UpdateTime": "xx",
        "IsContainerd": true,
        "HostName": "xx",
        "KubeProxyVersion": "xx",
        "AgentVersion": "xx",
        "DockerAPIVersion": "xx",
        "DockerGoVersion": "xx",
        "RequestId": "xx",
        "HostIP": "xx",
        "UUID": "xx",
        "KernelVersion": "xx",
        "MachineType": "xx",
        "DockerVersion": "xx",
        "K8sVersion": "xx",
        "K8sMasterIP": "xx",
        "ImageCnt": 1,
        "ContainerCnt": 1
    }
}
```

