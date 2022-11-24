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
        "InstanceID": "xx",
        "RegionID": 0,
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
        "DockerVersion": "xx",
        "KernelVersion": "xx",
        "MachineType": "xx",
        "UUID": "xx",
        "K8sVersion": "xx",
        "K8sMasterIP": "xx",
        "ImageCnt": 1,
        "ContainerCnt": 1,
        "Project": {
            "ProjectName": "xx",
            "ProjectID": 0
        },
        "Tags": [
            {
                "TagKey": "xx",
                "TagValue": "xx"
            }
        ]
    }
}
```

