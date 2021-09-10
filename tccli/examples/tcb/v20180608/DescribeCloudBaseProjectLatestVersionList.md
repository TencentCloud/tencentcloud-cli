**Example 1: 获取云开发项目列表**



Input: 

```
tccli tcb DescribeCloudBaseProjectLatestVersionList --cli-unfold-argument  \
    --EnvId xx \
    --ProjectType xx \
    --PageSize 0 \
    --Tags xx \
    --ProjectName xx \
    --Offset 0 \
    --CiId 12a05f48-3edd-41f4-a8cc-573b500111f3
```

Output: 
```
{
    "Response": {
        "ProjectList": [
            {
                "Status": "xx",
                "UpdateTime": "xx",
                "EnvId": "xx",
                "Name": "xx",
                "Sam": "xx",
                "Tags": [
                    "xx"
                ],
                "RcJson": "xx",
                "CDId": "xx",
                "NetworkConfig": "xx",
                "Parameters": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "Source": {
                    "CodingPackageVersion": "xx",
                    "WorkDir": "xx",
                    "Name": "xx",
                    "Url": "xx",
                    "Type": "xx",
                    "CodingPackageName": "xx"
                },
                "FailReason": "xx",
                "AddonConfig": "xx",
                "VersionNum": 0,
                "CIId": "xx",
                "Type": "xx",
                "CreateTime": "xx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

