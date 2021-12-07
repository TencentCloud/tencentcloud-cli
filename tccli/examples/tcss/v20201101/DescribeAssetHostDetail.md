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
        "AgentVersion": "2.4.0.107",
        "ContainerCnt": 0,
        "DockerAPIVersion": "",
        "DockerFileSystemDriver": "",
        "DockerGoVersion": "",
        "DockerRootDir": "",
        "DockerVersion": "",
        "Group": "",
        "HostIP": "172.16.48.101",
        "HostName": "",
        "ImageCnt": 0,
        "K8sMasterIP": "",
        "K8sVersion": "",
        "KernelVersion": "",
        "KubeProxyVersion": "",
        "OsName": "",
        "RequestId": "32429538-86bc-44ac-abdb-b1f5ae9c3f50",
        "Status": "online",
        "UUID": "6a19cc22-e989-4c65-9d00-d152af1e932f",
        "UpdateTime": "2021-01-29T06:33:13.814Z"
    }
}
```

