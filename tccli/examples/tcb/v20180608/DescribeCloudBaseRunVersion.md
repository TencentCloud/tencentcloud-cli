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
        "VersionName": "",
        "Remark": "",
        "DockerfilePath": "",
        "BuildDir": "",
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
        "PolicyDetail": [
            {
                "PolicyType": "",
                "PolicyThreshold": 0
            }
        ],
        "Cpu": 0,
        "Mem": 0,
        "RequestId": ""
    }
}
```

