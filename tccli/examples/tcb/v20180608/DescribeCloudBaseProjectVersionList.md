**Example 1: 查询云项目部署版本列表**



Input: 

```
tccli tcb DescribeCloudBaseProjectVersionList --cli-unfold-argument  \
    --EnvId lowcode-abc \
    --PageNum 1 \
    --PageSize 10 \
    --ProjectName project
```

Output: 
```
{
    "Response": {
        "ProjectVersions": [
            {
                "Name": "abc",
                "Sam": "abc",
                "Source": {
                    "Type": "abc",
                    "Url": "abc",
                    "Name": "abc",
                    "WorkDir": "abc",
                    "CodingPackageName": "abc",
                    "CodingPackageVersion": "abc",
                    "RawCode": "abc",
                    "Branch": "abc",
                    "ProjectId": 0,
                    "ProjectName": "abc"
                },
                "CreateTime": 0,
                "UpdateTime": 0,
                "Status": "abc",
                "Parameters": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "Type": "abc",
                "CIId": "abc",
                "CDId": "abc",
                "EnvId": "abc",
                "VersionNum": 0,
                "FailReason": "abc",
                "RcJson": "abc",
                "AddonConfig": "abc",
                "Tags": [
                    "abc"
                ],
                "NetworkConfig": "abc",
                "ExtensionId": "abc",
                "FailType": "abc",
                "RepoUrl": "abc",
                "AutoDeployOnCodeChange": true,
                "BuildPercent": 0,
                "Uin": "abc",
                "BuildFinishTime": "abc",
                "DeployFinishTime": "abc",
                "BuildId": "abc",
                "SourceUrl": "abc",
                "FailReasonShort": "abc",
                "FirstInitRepo": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

