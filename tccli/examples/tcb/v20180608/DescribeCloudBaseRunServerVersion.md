**Example 1: 示例**



Input: 

```
tccli tcb DescribeCloudBaseRunServerVersion --cli-unfold-argument  \
    --EnvId lotestapi100004 \
    --ServerName dockerservicename \
    --VersionName adb
```

Output: 
```
{
    "Response": {
        "Branch": "",
        "BuildDir": "",
        "ContainerPort": 80,
        "Cpu": 1,
        "CpuSize": 1,
        "CreatedTime": "2020-11-04 16:44:54",
        "CustomLogs": "/var/logs/data.log",
        "DockerfilePath": "",
        "EnvParams": "{}",
        "ImageUrl": "ccr.ccs.tencentyun.com/cloudbase-apolo-env-test-146d5/hello-world:v2",
        "InitialDelaySeconds": 2,
        "IsPublic": true,
        "MaxNum": 50,
        "Mem": 1,
        "MemSize": 1,
        "MinNum": 0,
        "PackageName": "",
        "PackageVersion": "",
        "PolicyThreshold": 60,
        "PolicyType": "cpu",
        "Remark": "",
        "Repo": "",
        "RepoType": "",
        "RequestId": "5620b49e-a25a-4007-84ef-03c9035c584d",
        "ServerName": "test",
        "Status": "normal",
        "SubnetIds": [
            "subnet-6yny6j0d"
        ],
        "UpdatedTime": "2020-11-04 19:55:22",
        "UploadType": "image",
        "VersionIP": "10.0.192.3",
        "VersionName": "test-010",
        "VersionPort": 80,
        "VpcId": "vpc-rtyzm94a"
    }
}
```

