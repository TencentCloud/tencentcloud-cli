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
        "VersionName": "xx",
        "Remark": "xx",
        "DockerfilePath": "xx",
        "BuildDir": "xx",
        "MinNum": 0,
        "MaxNum": 0,
        "PolicyType": "xx",
        "PolicyThreshold": 0,
        "EnvParams": "xx",
        "CreatedTime": "xx",
        "UpdatedTime": "xx",
        "VersionIP": "xx",
        "VersionPort": 0,
        "Status": "xx",
        "PackageName": "xx",
        "PackageVersion": "xx",
        "UploadType": "xx",
        "RepoType": "xx",
        "Repo": "xx",
        "Branch": "xx",
        "ServerName": "xx",
        "IsPublic": true,
        "VpcId": "xx",
        "SubnetIds": [
            "xx"
        ],
        "CustomLogs": "xx",
        "ContainerPort": 0,
        "InitialDelaySeconds": 0,
        "ImageUrl": "xx",
        "CpuSize": 0,
        "MemSize": 0,
        "PolicyDetail": [
            {
                "PolicyType": "xx",
                "PolicyThreshold": 0
            }
        ],
        "Cpu": 0,
        "Mem": 0,
        "RequestId": "xx"
    }
}
```

