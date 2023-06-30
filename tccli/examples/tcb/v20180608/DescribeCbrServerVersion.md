**Example 1: 示例**

查询服务版本的详情

Input: 

```
tccli tcb DescribeCbrServerVersion --cli-unfold-argument  \
    --EnvId abc \
    --ServerName abc \
    --VersionName abc
```

Output: 
```
{
    "Response": {
        "VersionName": "abc",
        "Remark": "abc",
        "DockerfilePath": "abc",
        "BuildDir": "abc",
        "Cpu": 0,
        "Mem": 0,
        "MinNum": 0,
        "MaxNum": 0,
        "EnvParams": "abc",
        "CreatedTime": "abc",
        "UpdatedTime": "abc",
        "VersionIP": "abc",
        "VersionPort": 0,
        "Status": "abc",
        "UploadType": "abc",
        "ServerName": "abc",
        "IsPublic": true,
        "VpcId": "abc",
        "SubnetIds": [
            "abc"
        ],
        "CustomLogs": "abc",
        "ContainerPort": 0,
        "InitialDelaySeconds": 0,
        "ImageUrl": "abc",
        "HasDockerfile": 0,
        "BaseImage": "abc",
        "EntryPoint": "abc",
        "PolicyDetail": [
            {
                "PolicyType": "abc",
                "PolicyThreshold": 0
            }
        ],
        "TkeClusterInfo": {
            "ClusterId": "abc",
            "VpcId": "abc",
            "VersionClbSubnetId": "abc"
        },
        "TkeWorkloadType": "abc",
        "PackageInfo": {
            "PackageName": "abc",
            "PackageVersion": "abc"
        },
        "RepoInfo": {
            "Repo": "abc",
            "RepoType": "abc",
            "RepoLanguage": "abc",
            "Branch": "abc"
        },
        "RequestId": "abc"
    }
}
```

