**Example 1: 服务基本信息查看**

服务基本信息查看

Input: 

```
tccli tem DescribeApplicationInfo --cli-unfold-argument  \
    --SourceChannel 0 \
    --ApplicationId app-xxxxxx \
    --EnvironmentId en-xxxxxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "VersionId": "abc",
            "ApplicationId": "abc",
            "DeployMode": "abc",
            "JdkVersion": "abc",
            "Description": "abc",
            "DeployVersion": "abc",
            "PublishMode": "abc",
            "JvmOpts": "abc",
            "InitPodNum": 0,
            "CpuSpec": 0,
            "MemorySpec": 0,
            "ImgRepo": "abc",
            "ImgName": "abc",
            "ImgVersion": "abc",
            "EsInfo": {
                "MinAliveInstances": 0,
                "MaxAliveInstances": 0,
                "EsStrategy": 0,
                "VersionId": "abc",
                "Threshold": 1
            },
            "EnvConf": [
                {
                    "Key": "abc",
                    "Value": "abc",
                    "Type": "abc",
                    "Config": "abc",
                    "Secret": "abc"
                }
            ],
            "StorageConfs": [
                {
                    "StorageVolName": "abc",
                    "StorageVolPath": "abc",
                    "StorageVolIp": "abc"
                }
            ],
            "Status": "abc",
            "Vpc": "abc",
            "SubnetId": "abc",
            "CreateDate": "abc",
            "ModifyDate": "abc",
            "StorageMountConfs": [
                {
                    "VolumeName": "abc",
                    "MountPath": "abc"
                }
            ],
            "VersionName": "abc",
            "LogOutputConf": {
                "OutputType": "abc",
                "ClsLogsetName": "abc",
                "ClsLogTopicId": "abc",
                "ClsLogsetId": "abc",
                "ClsLogTopicName": "abc"
            },
            "ApplicationName": "abc",
            "ApplicationDescription": "abc",
            "EnvironmentName": "abc",
            "EnvironmentId": "abc",
            "PublicDomain": "abc",
            "EnablePublicAccess": true,
            "CurrentInstances": 0,
            "ExpectedInstances": 0,
            "CodingLanguage": "abc",
            "PkgName": "abc",
            "EsEnable": 0,
            "EsStrategy": 0,
            "ImageTag": "abc",
            "LogEnable": 0,
            "MinAliveInstances": "abc",
            "SecurityGroupIds": [
                "abc"
            ],
            "ImageCommand": "abc",
            "ImageArgs": [
                "abc"
            ],
            "UseRegistryDefaultConfig": true,
            "Service": {
                "Name": "abc",
                "Ports": [
                    0
                ],
                "Yaml": "abc",
                "ApplicationName": "abc",
                "VersionName": "abc",
                "ClusterIp": [
                    "abc"
                ],
                "ExternalIp": "abc",
                "Type": "abc",
                "SubnetId": "abc",
                "LoadBalanceId": "abc",
                "PortMappings": [
                    {
                        "Port": 0,
                        "TargetPort": 0,
                        "Protocol": "abc",
                        "ServiceName": "abc"
                    }
                ],
                "ServicePortMappingList": [
                    {
                        "Type": "abc",
                        "ServiceName": "abc",
                        "ClusterIp": "abc",
                        "ExternalIp": "abc",
                        "SubnetId": "abc",
                        "VpcId": "abc",
                        "LoadBalanceId": "abc",
                        "Yaml": "abc",
                        "Ports": [
                            0
                        ],
                        "PortMappingItemList": [
                            {
                                "Port": 0,
                                "TargetPort": 0,
                                "Protocol": "abc"
                            }
                        ],
                        "ExternalDomain": "abc"
                    }
                ],
                "FlushAll": true,
                "EnableRegistryNextDeploy": 0,
                "ApplicationId": "abc",
                "AllIpDone": true,
                "ExternalDomain": "abc"
            },
            "SettingConfs": [
                {
                    "ConfigDataName": "abc",
                    "MountedPath": "abc",
                    "Data": [
                        {
                            "Key": "abc",
                            "Value": "abc",
                            "Type": "abc",
                            "Config": "abc",
                            "Secret": "abc"
                        }
                    ],
                    "SecretDataName": "abc"
                }
            ],
            "LogConfs": [
                "abc"
            ],
            "PostStart": "abc",
            "PreStop": "abc",
            "Liveness": {
                "Type": "abc",
                "Protocol": "abc",
                "Path": "abc",
                "Exec": "abc",
                "Port": 0,
                "InitialDelaySeconds": 0,
                "TimeoutSeconds": 0,
                "PeriodSeconds": 0
            },
            "Readiness": {
                "Type": "abc",
                "Protocol": "abc",
                "Path": "abc",
                "Exec": "abc",
                "Port": 0,
                "InitialDelaySeconds": 0,
                "TimeoutSeconds": 0,
                "PeriodSeconds": 0
            },
            "HorizontalAutoscaler": [
                {
                    "MinReplicas": 0,
                    "MaxReplicas": 0,
                    "Metrics": "abc",
                    "Threshold": 0,
                    "Enabled": true,
                    "DoubleThreshold": 0
                }
            ],
            "CronHorizontalAutoscaler": [
                {
                    "Name": "abc",
                    "Period": "abc",
                    "Schedules": [
                        {
                            "StartAt": "abc",
                            "TargetReplicas": 0
                        }
                    ],
                    "Enabled": true,
                    "Priority": 0
                }
            ],
            "Zones": [
                "abc"
            ],
            "LastDeployDate": "abc",
            "LastDeploySuccessDate": "abc",
            "NodeInfos": [
                {
                    "Name": "abc",
                    "Zone": "abc",
                    "SubnetId": "abc",
                    "AvailableIpCount": "abc",
                    "Cidr": "abc"
                }
            ],
            "ImageType": 0,
            "EnableTracing": 1,
            "EnableTracingReport": 1,
            "RepoType": 1,
            "BatchDeployStatus": "abc",
            "ApmInstanceId": "abc",
            "WorkloadInfo": {
                "ClusterId": "abc",
                "ApplicationName": "abc",
                "VersionName": "abc",
                "ReadyReplicas": 0,
                "Replicas": 0,
                "UpdatedReplicas": 0,
                "UpdatedReadyReplicas": 0,
                "UpdateRevision": "abc",
                "CurrentRevision": "abc"
            },
            "SpeedUp": true,
            "StartupProbe": {
                "Type": "abc",
                "Protocol": "abc",
                "Path": "abc",
                "Exec": "abc",
                "Port": 0,
                "InitialDelaySeconds": 0,
                "TimeoutSeconds": 0,
                "PeriodSeconds": 0
            },
            "OsFlavour": "abc",
            "RepoServer": "abc",
            "UnderDeploying": true,
            "EnablePrometheusConf": {
                "Port": 0,
                "Path": "abc"
            },
            "StoppedManually": true,
            "TcrInstanceId": "abc",
            "EnableMetrics": 0,
            "AppId": "abc",
            "SubAccountUin": "abc",
            "Uin": "abc",
            "Region": "abc",
            "GroupId": "abc",
            "EnableRegistry": 0,
            "AutoscalerList": [
                {
                    "MinReplicas": 0,
                    "MaxReplicas": 0,
                    "HorizontalAutoscaler": [
                        {
                            "MinReplicas": 0,
                            "MaxReplicas": 0,
                            "Metrics": "abc",
                            "Threshold": 0,
                            "Enabled": true,
                            "DoubleThreshold": 0
                        }
                    ],
                    "CronHorizontalAutoscaler": [
                        {
                            "Name": "abc",
                            "Period": "abc",
                            "Schedules": [
                                {
                                    "StartAt": "abc",
                                    "TargetReplicas": 0
                                }
                            ],
                            "Enabled": true,
                            "Priority": 0
                        }
                    ],
                    "AutoscalerId": "abc",
                    "AutoscalerName": "abc",
                    "Description": "abc",
                    "CreateDate": "abc",
                    "ModifyDate": "abc",
                    "EnableDate": "abc",
                    "Enabled": true
                }
            ],
            "Modifier": "abc",
            "Creator": "abc",
            "DeployStrategyConf": {
                "TotalBatchCount": 0,
                "BetaBatchNum": 0,
                "DeployStrategyType": 0,
                "BatchInterval": 0,
                "MinAvailable": 0,
                "Force": true
            },
            "PodList": {
                "Offset": 0,
                "Limit": 0,
                "TotalCount": 0,
                "RequestId": "abc",
                "PodList": [
                    {
                        "Webshell": "abc",
                        "PodId": "abc",
                        "Status": "abc",
                        "CreateTime": "abc",
                        "PodIp": "abc",
                        "Zone": "abc",
                        "DeployVersion": "abc",
                        "RestartCount": 0,
                        "Ready": true,
                        "ContainerState": "abc",
                        "NodeInfo": {
                            "Name": "abc",
                            "Zone": "abc",
                            "SubnetId": "abc",
                            "AvailableIpCount": "abc",
                            "Cidr": "abc"
                        },
                        "StartTime": "abc",
                        "Unhealthy": true,
                        "UnhealthyWarningMsg": "abc",
                        "VersionId": "abc",
                        "ApplicationName": "abc"
                    }
                ]
            },
            "ConfEdited": true,
            "Tags": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ],
            "PreStopEncoded": "abc",
            "PostStartEncoded": "abc"
        },
        "RequestId": "abc"
    }
}
```

