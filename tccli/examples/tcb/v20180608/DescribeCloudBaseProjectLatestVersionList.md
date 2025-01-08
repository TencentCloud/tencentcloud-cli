**Example 1: 获取云开发项目列表**



Input: 

```
tccli tcb DescribeCloudBaseProjectLatestVersionList --cli-unfold-argument  \
    --EnvId lowcode-abc \
    --PageSize 10 \
    --ProjectName project \
    --Offset 0 \
    --CiId 12a05f48-3edd-41f4-a8cc-573b500111f3
```

Output: 
```
{
    "Response": {
        "ProjectList": [
            {
                "EnvId": "lowcode-abc",
                "Name": "lcap-app-web",
                "VersionNum": 1705302500,
                "Status": "building",
                "Type": "framework-oneclick",
                "CIId": "067ae088-3ab8-abcd-87af-38be87e2e165",
                "CDId": "067ae088-3ab8-abcd-87af-38be87e2e165",
                "CreateTime": 1705302595,
                "UpdateTime": 1705302596,
                "Sam": "sam",
                "Source": {
                    "Type": "package_url",
                    "Url": "https://ci-source-124.cos.ap-shanghai.myqcloud.com/lca/app-BaEUKRry/code-1705302590000.zip",
                    "Name": "lcap-app-web",
                    "WorkDir": "/dev/",
                    "RawCode": "rawCode",
                    "Branch": "branch",
                    "ProjectId": 0,
                    "CodingPackageName": "cPackageName",
                    "CodingPackageVersion": "cPackageVersion",
                    "ProjectName": "pName"
                },
                "Parameters": [
                    {
                        "Key": "CLOUDBASE_BUILD_STARTTIME",
                        "Value": "1705302595000"
                    }
                ],
                "FailReason": "failed with something",
                "RcJson": "{\"keyName\": \"valueData\"}",
                "AddonConfig": "{\"keyName\": \"valueData\"}",
                "NetworkConfig": "{\"keyName\": \"valueData\"}",
                "Tags": [
                    "tag1",
                    "tag2"
                ],
                "Uin": "uin",
                "ExtensionId": "extensionId",
                "FailType": "system",
                "BuildFinishTime": "2025-01-01 00:00:00",
                "DeployFinishTime": "2025-01-01 00:00:00",
                "BuildId": "39141118",
                "SourceUrl": "codeurl",
                "FailReasonShort": "fail reason",
                "RepoUrl": "repoUrl",
                "AutoDeployOnCodeChange": false,
                "FirstInitRepo": "false",
                "BuildPercent": 80
            }
        ],
        "RequestId": "da4854bb-9e0e-abcd-a87e-5e452c874086",
        "TotalCount": 1
    }
}
```

