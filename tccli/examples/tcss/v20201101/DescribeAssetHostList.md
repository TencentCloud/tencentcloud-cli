**Example 1: 查询主机列表**

查询主机列表

Input: 

```
tccli tcss DescribeAssetHostList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "HostID": "abc",
                "HostIP": "abc",
                "HostName": "abc",
                "Group": "abc",
                "DockerVersion": "abc",
                "DockerFileSystemDriver": "abc",
                "ImageCnt": 1,
                "ContainerCnt": 1,
                "Status": "abc",
                "IsContainerd": true,
                "MachineType": "abc",
                "PublicIp": "abc",
                "Uuid": "abc",
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
                "ClusterID": "abc",
                "ClusterName": "abc",
                "ClusterAccessedStatus": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

