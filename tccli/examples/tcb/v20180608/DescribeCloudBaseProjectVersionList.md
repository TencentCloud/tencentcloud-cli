**Example 1: 查询云项目部署版本列表**



Input: 

```
tccli tcb DescribeCloudBaseProjectVersionList --cli-unfold-argument  \
    --EnvId xx \
    --PageNum 1 \
    --PageSize 1 \
    --ProjectName xx \
    --StartTime xx \
    --EndTime xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ProjectVersions": [
            {
                "Status": "xx",
                "UpdateTime": 0,
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
                    "RawCode": "xx",
                    "Type": "xx",
                    "CodingPackageName": "xx"
                },
                "FailReason": "xx",
                "AddonConfig": "xx",
                "VersionNum": 0,
                "ExtensionId": "xx",
                "FailType": "xx",
                "CIId": "xx",
                "Type": "xx",
                "CreateTime": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

