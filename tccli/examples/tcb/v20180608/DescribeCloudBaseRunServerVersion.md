**Example 1: 示例**

查询版本信息

Input: 

```
tccli tcb DescribeCloudBaseRunServerVersion --cli-unfold-argument  \
    --EnvId env-sdfd \
    --ServerName server \
    --VersionName ver
```

Output: 
```
{
    "Response": {
        "VersionName": "",
        "Remark": "",
        "DockerfilePath": "",
        "BuildDir": "",
        "Cpu": 0,
        "Mem": 0,
        "MinNum": 0,
        "MaxNum": 0,
        "PolicyType": "",
        "PolicyThreshold": 0,
        "EnvParams": "",
        "CreatedTime": "",
        "UpdatedTime": "",
        "VersionIP": "",
        "VersionPort": 0,
        "Status": "",
        "PackageName": "",
        "PackageVersion": "",
        "UploadType": "",
        "RepoType": "",
        "Repo": "",
        "Branch": "",
        "ServerName": "",
        "IsPublic": true,
        "VpcId": "",
        "SubnetIds": [
            ""
        ],
        "CustomLogs": "",
        "ContainerPort": 0,
        "InitialDelaySeconds": 0,
        "ImageUrl": "",
        "CpuSize": 0,
        "MemSize": 0,
        "HasDockerfile": 0,
        "BaseImage": "",
        "EntryPoint": "",
        "RepoLanguage": "",
        "PolicyDetail": [
            {
                "PolicyType": "",
                "PolicyThreshold": 0
            }
        ],
        "TkeClusterInfo": {
            "ClusterId": "",
            "VpcId": "",
            "VersionClbSubnetId": ""
        },
        "TkeWorkloadType": "",
        "RequestId": ""
    }
}
```

