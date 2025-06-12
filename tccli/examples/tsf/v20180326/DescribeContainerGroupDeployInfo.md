**Example 1: DescribeContainerGroupDeployInfo**



Input: 

```
tccli tsf DescribeContainerGroupDeployInfo --cli-unfold-argument  \
    --GroupId group-gyqpkzda
```

Output: 
```
{
    "Response": {
        "Result": {
            "GroupId": "group-gyqpkzda",
            "GroupName": "group-test",
            "InstanceNum": 0,
            "CurrentNum": 0,
            "Server": "ccr.tencent.com",
            "Reponame": "tsf_1038293xxxxx/nginx",
            "TagName": "latest",
            "CpuRequest": "0.5",
            "CpuLimit": "1",
            "MemRequest": "64",
            "MemLimit": "512",
            "AccessType": 0,
            "ProtocolPorts": [
                {
                    "Protocol": "tcp",
                    "Port": 8080,
                    "TargetPort": 8080,
                    "NodePort": 0,
                    "Name": "tcp-8080"
                }
            ],
            "UpdateType": 0,
            "UpdateIvl": 0,
            "JvmOpts": "-Xmx1024m -Xms128m",
            "SubnetId": "subnet-gyqpkzda",
            "AgentCpuRequest": "0.1",
            "AgentCpuLimit": "0.2",
            "AgentMemRequest": "32",
            "AgentMemLimit": "128",
            "IstioCpuRequest": "0.1",
            "IstioCpuLimit": "0.2",
            "IstioMemRequest": "32",
            "IstioMemLimit": "128",
            "Envs": [
                {
                    "Name": "host",
                    "Value": "metadata.host",
                    "ValueFrom": {
                        "FieldRef": {
                            "FieldPath": "metadata.host"
                        },
                        "ResourceFieldRef": {
                            "Resource": "resource"
                        }
                    }
                }
            ],
            "HealthCheckSettings": {
                "LivenessProbe": {
                    "ActionType": "Port",
                    "InitialDelaySeconds": 60,
                    "TimeoutSeconds": 30,
                    "PeriodSeconds": 30,
                    "SuccessThreshold": 1,
                    "FailureThreshold": 3,
                    "Scheme": "tcp",
                    "Port": 8080,
                    "Path": "/health",
                    "Command": [
                        "sh health.sh"
                    ],
                    "Type": "TCP"
                },
                "ReadinessProbe": {
                    "ActionType": "Port",
                    "InitialDelaySeconds": 180,
                    "TimeoutSeconds": 30,
                    "PeriodSeconds": 30,
                    "SuccessThreshold": 1,
                    "FailureThreshold": 3,
                    "Scheme": "tcp",
                    "Port": 8080,
                    "Path": "/health",
                    "Command": [
                        "sh health.sh"
                    ],
                    "Type": "TCP"
                }
            },
            "DeployAgent": true,
            "Alias": "group-alias",
            "DisableService": true,
            "HeadlessService": true,
            "TcrRepoInfo": {
                "Region": "ap-guangzhou",
                "RegistryId": "reg-gyqpkzda",
                "RegistryName": "presonal-registry",
                "Namespace": "default",
                "RepoName": "nginx"
            },
            "VolumeInfos": [
                {
                    "VolumeType": "HOST",
                    "VolumeName": "host",
                    "VolumeConfig": "host",
                    "ConfigMapOptions": [
                        {
                            "Key": "host",
                            "Path": "/host",
                            "Mode": "host"
                        }
                    ],
                    "EmptyDirOption": {
                        "EnableMemory": true,
                        "StorageCapacity": 0,
                        "StorageUnit": "sunit",
                        "SizeLimit": "64"
                    }
                }
            ],
            "VolumeMountInfos": [
                {
                    "VolumeMountName": "mount-name",
                    "VolumeMountPath": "/config",
                    "VolumeMountSubPath": "/conf",
                    "ReadOrWrite": "777"
                }
            ],
            "KubeInjectEnable": true,
            "RepoType": "tcr",
            "WarmupSetting": {
                "Enabled": true,
                "WarmupTime": 1,
                "Curvature": 1,
                "EnabledProtection": true
            },
            "GatewayConfig": {
                "Name": "gateway-config-test"
            },
            "ContainerName": "group-name-279128-28nsu82",
            "AdditionalContainerList": [
                {
                    "ContainerName": "agent",
                    "TagName": "v1",
                    "RepoName": "agent",
                    "RepoType": "tcr",
                    "TcrRepoInfo": {
                        "Region": "ap-guangzhou",
                        "RegistryId": "reg-gyqpkzda",
                        "RegistryName": "agent",
                        "Namespace": "default",
                        "RepoName": "agent"
                    },
                    "Server": "ccr.tencent.com",
                    "SecretName": "default-secret-name",
                    "JvmOpts": "-Xmx64m -Xms32m",
                    "CpuLimit": "1",
                    "CpuRequest": "0.1",
                    "MemRequest": "32",
                    "MemLimit": "128",
                    "HealthCheckSettings": {
                        "ReadinessProbe": {
                            "InitialDelaySeconds": 10,
                            "PeriodSeconds": 10,
                            "Port": 8000,
                            "ActionType": "tcp",
                            "SuccessThreshold": 3,
                            "Type": "TCP",
                            "TimeoutSeconds": 3,
                            "FailureThreshold": 3
                        },
                        "LivenessProbe": {
                            "ActionType": "tcp",
                            "InitialDelaySeconds": 180,
                            "TimeoutSeconds": 1,
                            "PeriodSeconds": 1,
                            "SuccessThreshold": 1,
                            "FailureThreshold": 1,
                            "Scheme": "http",
                            "Port": 1,
                            "Path": "/health",
                            "Command": [
                                "sh health.sh"
                            ],
                            "Type": "TCP"
                        }
                    },
                    "Envs": [
                        {
                            "Name": "host",
                            "Value": "metadata.host",
                            "ValueFrom": {
                                "FieldRef": {
                                    "FieldPath": "metadata.host"
                                },
                                "ResourceFieldRef": {
                                    "Resource": "metadata.host"
                                }
                            }
                        }
                    ],
                    "UserEnvs": [
                        {
                            "Name": "consul_ip",
                            "Value": "10.23.12.3"
                        }
                    ],
                    "VolumeMountInfoList": [
                        {
                            "VolumeMountName": "host",
                            "VolumeMountPath": "/host",
                            "VolumeMountSubPath": "/config",
                            "ReadOrWrite": "777"
                        }
                    ]
                }
            ],
            "InternalContainerList": [
                {
                    "ContainerName": "internal-container-test",
                    "TagName": "v1",
                    "RepoName": "nginx",
                    "RepoType": "tcr",
                    "TcrRepoInfo": {
                        "Region": "ap-guangzhou",
                        "RegistryId": "reg-6a79x94v",
                        "RegistryName": "nginx",
                        "Namespace": "default",
                        "RepoName": "nginx"
                    },
                    "Server": "ccr.ccs.tencent.com",
                    "SecretName": "default-secretName",
                    "JvmOpts": "-Xmx64m -Xms32m",
                    "CpuLimit": "1",
                    "CpuRequest": "0.1",
                    "MemRequest": "32",
                    "MemLimit": "128",
                    "HealthCheckSettings": {
                        "ReadinessProbe": {
                            "InitialDelaySeconds": 10,
                            "PeriodSeconds": 10,
                            "Port": 8000,
                            "ActionType": "tcp",
                            "SuccessThreshold": 3,
                            "Type": "TCP",
                            "TimeoutSeconds": 3,
                            "FailureThreshold": 3
                        },
                        "LivenessProbe": {
                            "ActionType": "tcp",
                            "InitialDelaySeconds": 180,
                            "TimeoutSeconds": 1,
                            "PeriodSeconds": 1,
                            "SuccessThreshold": 1,
                            "FailureThreshold": 1,
                            "Scheme": "http",
                            "Port": 1,
                            "Path": "/health",
                            "Command": [
                                "sh health.sh"
                            ],
                            "Type": "TCP"
                        }
                    },
                    "VolumeMountInfoList": [
                        {
                            "VolumeMountName": "host",
                            "VolumeMountPath": "/host",
                            "VolumeMountSubPath": "/config",
                            "ReadOrWrite": "777"
                        }
                    ]
                }
            ]
        },
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

