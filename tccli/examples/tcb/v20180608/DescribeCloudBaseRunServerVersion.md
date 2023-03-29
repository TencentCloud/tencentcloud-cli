**Example 1: 示例**

查询版本信息

Input: 

```
tccli tcb DescribeCloudBaseRunServerVersion --cli-unfold-argument  \
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
        "PolicyType": "abc",
        "PolicyThreshold": 0,
        "EnvParams": "abc",
        "CreatedTime": "abc",
        "UpdatedTime": "abc",
        "VersionIP": "abc",
        "VersionPort": 0,
        "Status": "abc",
        "PackageName": "abc",
        "PackageVersion": "abc",
        "UploadType": "abc",
        "RepoType": "abc",
        "Repo": "abc",
        "Branch": "abc",
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
        "CpuSize": 0,
        "MemSize": 0,
        "HasDockerfile": 0,
        "BaseImage": "abc",
        "EntryPoint": "abc",
        "RepoLanguage": "abc",
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
        "RequestId": "abc"
    }
}
```

