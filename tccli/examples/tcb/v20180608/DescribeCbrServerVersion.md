**Example 1: 示例**

查询服务版本的详情

Input: 

```
tccli tcb DescribeCbrServerVersion --cli-unfold-argument  \
    --EnvId env-sdfsf \
    --ServerName server-sdfsf \
    --VersionName version-sdfsfd
```

Output: 
```
{
    "Response": {
        "VersionName": "version",
        "Remark": "",
        "DockerfilePath": "",
        "BuildDir": "",
        "Cpu": 0,
        "Mem": 0,
        "MinNum": 0,
        "MaxNum": 0,
        "EnvParams": "",
        "CreatedTime": "",
        "UpdatedTime": "",
        "VersionIP": "",
        "VersionPort": 0,
        "Status": "",
        "UploadType": "",
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
        "HasDockerfile": 0,
        "BaseImage": "",
        "EntryPoint": "",
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
        "PackageInfo": {
            "PackageName": "",
            "PackageVersion": ""
        },
        "RepoInfo": {
            "Repo": "",
            "RepoType": "",
            "RepoLanguage": "",
            "Branch": ""
        },
        "RequestId": "sfdfdfsdf"
    }
}
```

