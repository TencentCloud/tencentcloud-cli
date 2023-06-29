**Example 1: 查询主机详细信息**

查询主机详细信息

Input: 

```
tccli tcss DescribeAssetHostDetail --cli-unfold-argument  \
    --HostId dskaldjskld
```

Output: 
```
{
    "Response": {
        "UUID": "abc",
        "UpdateTime": "abc",
        "HostName": "abc",
        "Group": "abc",
        "HostIP": "abc",
        "OsName": "abc",
        "AgentVersion": "abc",
        "KernelVersion": "abc",
        "DockerVersion": "abc",
        "DockerAPIVersion": "abc",
        "DockerGoVersion": "abc",
        "DockerFileSystemDriver": "abc",
        "DockerRootDir": "abc",
        "ImageCnt": 1,
        "ContainerCnt": 1,
        "K8sMasterIP": "abc",
        "K8sVersion": "abc",
        "KubeProxyVersion": "abc",
        "Status": "abc",
        "IsContainerd": true,
        "MachineType": "abc",
        "PublicIp": "abc",
        "InstanceID": "abc",
        "RegionID": 0,
        "Project": {
            "ProjectName": "abc",
            "ProjectID": 0
        },
        "Tags": [
            {
                "TagKey": "abc",
                "TagValue": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

