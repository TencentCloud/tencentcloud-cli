**Example 1: 示例**



Input: 

```
tccli tcb DescribeCloudBaseRunServerVersion --cli-unfold-argument  \
    --ServerName dockerservicename \
    --EnvId lotestapi100004 \
    --VersionName adb
```

Output: 
```
{
    "Response": {
        "TkeClusterInfo": {
            "VpcId": "xx",
            "ClusterId": "xx",
            "VersionClbSubnetId": "xx"
        },
        "UpdatedTime": "xx",
        "MaxNum": 50,
        "EnvParams": "xx",
        "PackageName": "xx",
        "BaseImage": "xx",
        "TkeWorkloadType": "xx",
        "RepoLanguage": "xx",
        "Branch": "xx",
        "CreatedTime": "xx",
        "Status": "xx",
        "VpcId": "xx",
        "BuildDir": "xx",
        "VersionPort": 80,
        "Mem": 1,
        "UploadType": "xx",
        "InitialDelaySeconds": 2,
        "CustomLogs": "xx",
        "Repo": "xx",
        "MinNum": 0,
        "DockerfilePath": "xx",
        "EntryPoint": "xx",
        "ContainerPort": 80,
        "Remark": "xx",
        "VersionIP": "xx",
        "ServerName": "xx",
        "RepoType": "xx",
        "RequestId": "xx",
        "MemSize": 0.0,
        "PackageVersion": "xx",
        "Cpu": 1,
        "HasDockerfile": 0,
        "CpuSize": 0.0,
        "PolicyThreshold": 0.0,
        "SubnetIds": [
            "subnet-6yny6j0d"
        ],
        "IsPublic": true,
        "PolicyType": "xx",
        "PolicyDetail": [
            {
                "PolicyThreshold": 0,
                "PolicyType": "xx"
            }
        ],
        "VersionName": "xx",
        "ImageUrl": "xx"
    }
}
```

