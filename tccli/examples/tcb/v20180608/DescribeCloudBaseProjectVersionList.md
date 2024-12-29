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
                "Name": "name",
                "Sam": "sam",
                "Source": {
                    "Type": "type",
                    "Url": "http://url",
                    "Name": "name",
                    "WorkDir": "dir",
                    "CodingPackageName": "projectName",
                    "CodingPackageVersion": "0.0.1",
                    "RawCode": "rawcode",
                    "Branch": "branch",
                    "ProjectId": 0,
                    "ProjectName": "projectName"
                },
                "CreateTime": 0,
                "UpdateTime": 0,
                "Status": "success",
                "Parameters": [
                    {
                        "Key": "key",
                        "Value": "value"
                    }
                ],
                "Type": "type",
                "CIId": "ciid",
                "CDId": "cdid",
                "EnvId": "env-asdf",
                "VersionNum": 0,
                "FailReason": "failed with reason",
                "RcJson": "{\"key\":\"value\"}",
                "AddonConfig": "{\"key\":\"value\"}",
                "Tags": [
                    "tag"
                ],
                "NetworkConfig": "{\"key\":\"value\"}",
                "ExtensionId": "extensionid",
                "FailType": "system",
                "RepoUrl": "http://repourl",
                "AutoDeployOnCodeChange": true,
                "BuildPercent": 0,
                "Uin": "10000101123",
                "BuildFinishTime": "2024-12-26 14:00:00",
                "DeployFinishTime": "2024-12-26 14:05:00",
                "BuildId": "buildid",
                "SourceUrl": "http://sourceurl",
                "FailReasonShort": "failed with something",
                "FirstInitRepo": "http://firstinitrepo"
            }
        ],
        "TotalCount": 1,
        "RequestId": "asdasfas-hfgd-skdj-shaksldiaosu"
    }
}
```

