**Example 1: 服务基本信息查看**

服务基本信息查看

Input: 

```
tccli tem DescribeApplicationInfo --cli-unfold-argument  \
    --SourceChannel 0 \
    --ApplicationId xx \
    --EnvironmentId xx
```

Output: 
```
{
    "Response": {
        "Result": {
            "CurrentInstances": 1,
            "ImgName": "xx",
            "Service": {
                "ApplicationName": "xx",
                "ExternalIp": "xx",
                "Name": "xx",
                "PortMappings": [
                    {
                        "Protocol": "xx",
                        "TargetPort": 0,
                        "Port": 0
                    }
                ],
                "Yaml": "xx",
                "LoadBalanceId": "xx",
                "VersionName": "xx",
                "ClusterIp": [
                    "xx"
                ],
                "SubnetId": "xx",
                "Type": "xx",
                "Ports": [
                    0
                ]
            },
            "JvmOpts": "xx",
            "ImageTag": "xx",
            "PublicDomain": "xx",
            "StorageConfs": [
                {
                    "StorageVolName": "xx",
                    "StorageVolIp": "xx",
                    "StorageVolPath": "xx"
                }
            ],
            "ExpectedInstances": 1,
            "ImgRepo": "xx",
            "EnvConf": [
                {
                    "Value": "xx",
                    "Key": "xx"
                }
            ],
            "Status": "xx",
            "EnvironmentName": "xx",
            "ImageCommand": "xx",
            "ModifyDate": "xx",
            "Description": "xx",
            "EnablePublicAccess": true,
            "JdkVersion": "xx",
            "Vpc": "xx",
            "SubnetId": "xx",
            "CodingLanguage": "xx",
            "ApplicationId": true,
            "ApplicationName": "xx",
            "LogOutputConf": {
                "ClsLogTopicId": "xx",
                "ClsLogsetName": "xx",
                "ClsLogsetId": "xx",
                "ClsLogTopicName": "xx",
                "OutputType": "xx"
            },
            "UseRegistryDefaultConfig": true,
            "ApplicationDescription": "xx",
            "PublishMode": "xx",
            "CpuSpec": 0.0,
            "EsEnable": 0,
            "CreateDate": "xx",
            "DeployMode": "xx",
            "SecurityGroupIds": [
                "xx"
            ],
            "DeployVersion": "xx",
            "InitPodNum": 0,
            "ImageArgs": [
                "xx"
            ],
            "MemorySpec": 0.0,
            "EnvironmentId": "xx",
            "PkgName": "xx",
            "StorageMountConfs": [
                {
                    "VolumeName": "xx",
                    "MountPath": "xx"
                }
            ],
            "LogEnable": 0,
            "EsInfo": {
                "MinAliveInstances": 0,
                "EsStrategy": 0,
                "VersionId": "xx",
                "Threshold": 1,
                "MaxAliveInstances": 0
            },
            "ImgVersion": "xx",
            "VersionId": "xx",
            "SettingConfs": [
                {
                    "ConfigDataName": "xx",
                    "MountedPath": "xx",
                    "Data": [
                        {
                            "Value": "xx",
                            "Key": "xx"
                        }
                    ]
                }
            ],
            "VersionName": "xx",
            "MinAliveInstances": 0,
            "EsStrategy": 0
        },
        "RequestId": "xx"
    }
}
```

