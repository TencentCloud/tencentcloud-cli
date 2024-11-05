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
                "HostID": "223e6323-1db6-42cf-8094-200916841684",
                "HostIP": "10.0.0.11",
                "HostName": "ins-1684ad1f2",
                "Group": "staffs",
                "DockerVersion": "1.0.0",
                "DockerFileSystemDriver": "ZFS",
                "ImageCnt": 1,
                "ContainerCnt": 1,
                "Status": "ONLINE",
                "IsContainerd": true,
                "MachineType": "CVM",
                "PublicIp": "112.46.12.11",
                "Uuid": "223e6323-1db6-42cf-8094-200916841684",
                "InstanceID": "ins-1684ad1f2",
                "RegionID": 1,
                "Project": {
                    "ProjectName": "ap-beijing",
                    "ProjectID": 0
                },
                "Tags": [
                    {
                        "TagKey": "adone",
                        "TagValue": "mark"
                    }
                ],
                "ClusterID": "csbd-cawfdfafd",
                "ClusterName": "cls-test1",
                "ClusterAccessedStatus": "1",
                "ChargeCoresCnt": 1,
                "DefendStatus": "running",
                "CoresCnt": 1
            }
        ],
        "TotalCount": 1,
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe"
    }
}
```

