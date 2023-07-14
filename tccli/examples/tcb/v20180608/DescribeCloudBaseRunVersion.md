**Example 1: 示例**

查询云托管版本详情

Input: 

```
tccli tcb DescribeCloudBaseRunVersion --cli-unfold-argument  \
    --EnvId lotestapi100004 \
    --ServerName dockerservicename \
    --VersionName adb
```

Output: 
```
{
    "Response": {
        "VersionName": "abc",
        "Remark": "abc",
        "DockerfilePath": "abc",
        "BuildDir": "abc",
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
        "PolicyDetail": [
            {
                "PolicyType": "abc",
                "PolicyThreshold": 0
            }
        ],
        "Cpu": 0,
        "Mem": 0,
        "RequestId": "abc"
    }
}
```

