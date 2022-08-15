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
                "ApplicationId": "xx",
                "AllIpDone": true,
                "PortMappings": [
                    {
                        "Protocol": "xx",
                        "ServiceName": "xx",
                        "TargetPort": 0,
                        "Port": 0
                    }
                ],
                "Yaml": "xx",
                "LoadBalanceId": "xx",
                "ServicePortMappingList": [
                    {
                        "ExternalIp": "xx",
                        "VpcId": "xx",
                        "PortMappingItemList": [
                            {
                                "Protocol": "xx",
                                "TargetPort": 0,
                                "Port": 0
                            }
                        ],
                        "Yaml": "xx",
                        "LoadBalanceId": "xx",
                        "ServiceName": "xx",
                        "ClusterIp": "xx",
                        "SubnetId": "xx",
                        "Type": "xx",
                        "Ports": [
                            0
                        ]
                    }
                ],
                "VersionName": "xx",
                "ClusterIp": [
                    "xx"
                ],
                "SubnetId": "xx",
                "Type": "xx",
                "Ports": [
                    0
                ],
                "EnableRegistryNextDeploy": 0,
                "FlushAll": true
            },
            "JvmOpts": "xx",
            "SpeedUp": true,
            "ImageTag": "xx",
            "PublicDomain": "xx",
            "StorageConfs": [
                {
                    "StorageVolName": "xx",
                    "StorageVolIp": "xx",
                    "StorageVolPath": "xx"
                }
            ],
            "EnableTracingReport": 1,
            "ExpectedInstances": 1,
            "ImgRepo": "xx",
            "StartupProbe": {
                "Protocol": "xx",
                "TimeoutSeconds": 0,
                "Exec": "xx",
                "InitialDelaySeconds": 0,
                "PeriodSeconds": 0,
                "Path": "xx",
                "Type": "xx",
                "Port": 0
            },
            "OsFlavour": "xx",
            "BatchDeployStatus": "xx",
            "Status": "xx",
            "EnvironmentName": "xx",
            "ImageCommand": "xx",
            "ModifyDate": "xx",
            "Description": "xx",
            "EnablePublicAccess": true,
            "StoppedManually": true,
            "EnvConf": [
                {
                    "Config": "xx",
                    "Secret": "xx",
                    "Type": "xx",
                    "Value": "xx",
                    "Key": "xx"
                }
            ],
            "LastDeploySuccessDate": "xx",
            "JdkVersion": "xx",
            "ApmInstanceId": "xx",
            "Vpc": "xx",
            "EnablePrometheusConf": {
                "Path": "xx",
                "Port": 0
            },
            "EnableTracing": 1,
            "CodingLanguage": "xx",
            "SubnetId": "xx",
            "ApplicationId": "xx",
            "ApplicationName": "xx",
            "Readiness": {
                "Protocol": "xx",
                "TimeoutSeconds": 0,
                "Exec": "xx",
                "InitialDelaySeconds": 0,
                "PeriodSeconds": 0,
                "Path": "xx",
                "Type": "xx",
                "Port": 0
            },
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
            "Liveness": {
                "Protocol": "xx",
                "TimeoutSeconds": 0,
                "Exec": "xx",
                "InitialDelaySeconds": 0,
                "PeriodSeconds": 0,
                "Path": "xx",
                "Type": "xx",
                "Port": 0
            },
            "EnableMetrics": 0,
            "DeployMode": "xx",
            "SecurityGroupIds": [
                "xx"
            ],
            "TcrInstanceId": "xx",
            "CronHorizontalAutoscaler": [
                {
                    "Priority": 0,
                    "Schedules": [
                        {
                            "StartAt": "xx",
                            "TargetReplicas": 0
                        }
                    ],
                    "Enabled": true,
                    "Period": "xx",
                    "Name": "xx"
                }
            ],
            "DeployVersion": "xx",
            "InitPodNum": 0,
            "RepoType": 1,
            "ImageArgs": [
                "xx"
            ],
            "MemorySpec": 0.0,
            "WorkloadInfo": {
                "ApplicationName": "xx",
                "ClusterId": "xx"
            },
            "ImageType": 0,
            "PreStop": "xx",
            "EnvironmentId": "xx",
            "LogConfs": [
                "xx"
            ],
            "PkgName": "xx",
            "StorageMountConfs": [
                {
                    "VolumeName": "xx",
                    "MountPath": "xx"
                }
            ],
            "HorizontalAutoscaler": [
                {
                    "MinReplicas": 0,
                    "Metrics": "xx",
                    "Enabled": true,
                    "Threshold": 0,
                    "MaxReplicas": 0
                }
            ],
            "UnderDeploying": true,
            "LogEnable": 0,
            "EsInfo": {
                "MinAliveInstances": 0,
                "EsStrategy": 0,
                "VersionId": "xx",
                "Threshold": 1,
                "MaxAliveInstances": 0
            },
            "Zones": [
                "xx"
            ],
            "ImgVersion": "xx",
            "VersionId": "xx",
            "LastDeployDate": "xx",
            "SettingConfs": [
                {
                    "ConfigDataName": "xx",
                    "MountedPath": "xx",
                    "SecretDataName": "xx",
                    "Data": [
                        {
                            "Config": "xx",
                            "Secret": "xx",
                            "Type": "xx",
                            "Value": "xx",
                            "Key": "xx"
                        }
                    ]
                }
            ],
            "VersionName": "xx",
            "MinAliveInstances": "xx",
            "EsStrategy": 0,
            "NodeInfos": [
                {
                    "SubnetId": "xx",
                    "Cidr": "xx",
                    "AvailableIpCount": "xx",
                    "Name": "xx",
                    "Zone": "xx"
                }
            ],
            "RepoServer": "xx",
            "PostStart": "xx"
        },
        "RequestId": "xx"
    }
}
```

