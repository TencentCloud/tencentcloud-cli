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
        "AgentVersion": "5.2.1.105",
        "ClusterAccessedStatus": "AccessedNone",
        "ClusterID": "cls-dfw3e***",
        "ClusterName": "clsfoo***",
        "ContainerCnt": 1,
        "DockerAPIVersion": "1.43",
        "DockerFileSystemDriver": "overlay2",
        "DockerGoVersion": "go1.20.7",
        "DockerRootDir": "/var/lib/docker",
        "DockerVersion": "24.0.6",
        "Group": "root",
        "HostIP": "1.1.1.1",
        "HostName": "机器名称",
        "ImageCnt": 10,
        "InstanceID": "ins-8bc803fd",
        "IsContainerd": false,
        "K8sMasterIP": "10.0.1.92",
        "K8sVersion": "1.0.1",
        "KernelVersion": "3.10.0-1160.102.1.el7.x86_64",
        "KubeProxyVersion": "1.0.1",
        "MachineType": "CVM",
        "OsName": "CentOS Linux release 7.9.2009 (Core)",
        "Project": {
            "ProjectID": 0,
            "ProjectName": "默认项目"
        },
        "PublicIp": "1.1.1.1",
        "RegionID": 1,
        "RequestId": "342475fc-76eb-4199-998f-780f9921a5f2",
        "Status": "ONLINE",
        "Tags": [],
        "UUID": "8bc803fd-d85d-47b8-9e2b-9644674be677",
        "UpdateTime": "2024-10-30 10:26:52",
        "AssetSyncTime": "2024-10-30 10:26:52"
    }
}
```

