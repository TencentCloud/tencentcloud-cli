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
        "RequestId": "b86d4065-771d-485c-9130-8914fe5fd1bc",
        "Result": {
            "AppId": "1305738457",
            "SubAccountUin": "100000799529",
            "Uin": "100019051593",
            "Region": "ap-shanghai",
            "VersionId": "revision-jorxnl6j",
            "VersionName": "20241202165113",
            "ApplicationId": "app-5vaz8x85",
            "Vpc": "vpc-e3ay8qku",
            "SubnetId": "subnet-kctzw7nj,subnet-8indzsuv,subnet-qau65gm1",
            "DeployMode": "JAR",
            "JdkVersion": "KONA:11",
            "Description": "",
            "DeployVersion": "20241202165113",
            "GroupId": "group-job6vv75",
            "PublishMode": "",
            "InitPodNum": 3,
            "CpuSpec": 1,
            "MemorySpec": 2,
            "ImgRepo": "",
            "ImgName": "tem-100019051593-sfuw/app0925",
            "ImgVersion": "20241202165113",
            "EsInfo": null,
            "EnvConf": [
                {
                    "Key": "TEM_APM_TOKEN",
                    "Value": "DBaxEudGGxxOFmAYNBuq",
                    "Type": "reserved",
                    "Config": "",
                    "Secret": ""
                },
                {
                    "Key": "TEM_APM_COLLECTOR_SKYWALKING",
                    "Value": "pl.ap-shanghai.apm.tencentcs.com:11800",
                    "Type": "reserved",
                    "Config": "",
                    "Secret": ""
                },
                {
                    "Key": "TEM_APM_COLLECTOR_JAEGER",
                    "Value": "pl.ap-shanghai.apm.tencentcs.com:14250",
                    "Type": "reserved",
                    "Config": "",
                    "Secret": ""
                },
                {
                    "Key": "TEM_APM_COLLECTOR_OPENTELEMETRY",
                    "Value": "pl.ap-shanghai.apm.tencentcs.com:4317",
                    "Type": "reserved",
                    "Config": "",
                    "Secret": ""
                },
                {
                    "Key": "TEM_APM_INSTANCE_ID",
                    "Value": "apm-JcXK7eNzw",
                    "Type": "reserved",
                    "Config": "",
                    "Secret": ""
                },
                {
                    "Key": "PROMETHEUS_INSTANCE_ID",
                    "Value": "prom-hdiellob",
                    "Type": "reserved",
                    "Config": "",
                    "Secret": ""
                },
                {
                    "Key": "PROMETHEUS_TOKEN",
                    "Value": ";F1Lh7zVs-LFhT&+3dRqUA5bhdl",
                    "Type": "reserved",
                    "Config": "",
                    "Secret": ""
                },
                {
                    "Key": "PROMETHEUS_REMOTE_WRITE_URL",
                    "Value": "http://10.0.30.147:9090/api/v1/prom/write",
                    "Type": "reserved",
                    "Config": "",
                    "Secret": ""
                },
                {
                    "Key": "PROMETHEUS_REMOTE_READ_URL",
                    "Value": "http://10.0.30.147:9090/api/v1/read",
                    "Type": "reserved",
                    "Config": "",
                    "Secret": ""
                },
                {
                    "Key": "PROMETHEUS_PUSH_GATEWAY_ADDR",
                    "Value": "10.0.30.147:9090",
                    "Type": "reserved",
                    "Config": "",
                    "Secret": ""
                },
                {
                    "Key": "PROMETHEUS_HTTP_API",
                    "Value": "http://10.0.30.147:9090/api/v1",
                    "Type": "reserved",
                    "Config": "",
                    "Secret": ""
                },
                {
                    "Key": "PROMETHEUS_GRAFANA_ADDR",
                    "Value": "",
                    "Type": "reserved",
                    "Config": "",
                    "Secret": ""
                }
            ],
            "SettingConfs": [
                {
                    "ConfigDataName": "pk-test-1",
                    "SecretDataName": "",
                    "MountedPath": "/data",
                    "Data": [
                        {
                            "Key": "name",
                            "Value": "value",
                            "Type": "",
                            "Config": "",
                            "Secret": ""
                        }
                    ]
                }
            ],
            "LogConfs": [],
            "LogOutputConf": null,
            "PostStart": "/bin/sh\n-c\ncurl localhost:8080/postStart",
            "PostStartEncoded": "",
            "PreStop": "/bin/sh\n-c\nwget --server-response --spider -S --no-verbose --header=\"Content-Type:application/json\" --post-data='{\"serverName\":\"api-basic\"}' \"http://localhost:9900/actuator/stopmsg\"\nsleep 30s",
            "PreStopEncoded": "",
            "StorageConfs": [],
            "StorageMountConfs": [],
            "JvmOpts": "-Xms128m -XX:MetaspaceSize=128m",
            "Service": {
                "PortMappings": [],
                "LoadBalanceId": "",
                "SubnetId": "",
                "Type": "",
                "Name": "",
                "ApplicationName": "app0925",
                "ClusterIp": [],
                "ExternalIp": "",
                "ExternalDomain": "",
                "VersionName": "",
                "Ports": [],
                "Yaml": "",
                "ApplicationId": "app-5vaz8x85",
                "ServicePortMappingList": [
                    {
                        "Type": "CLUSTER",
                        "ServiceName": "k8s-svc-test",
                        "ClusterIp": "172.16.56.122",
                        "ExternalIp": "",
                        "ExternalDomain": "",
                        "SubnetId": "",
                        "VpcId": "",
                        "LoadBalanceId": "",
                        "Yaml": "apiVersion: xxxx",
                        "Ports": [
                            8080
                        ],
                        "PortMappingItemList": [
                            {
                                "Port": 8080,
                                "TargetPort": 8080,
                                "Protocol": "TCP"
                            }
                        ]
                    },
                    {
                        "Type": "CLUSTER",
                        "ServiceName": "pk-svc",
                        "ClusterIp": "172.16.52.35",
                        "ExternalIp": "",
                        "ExternalDomain": "",
                        "SubnetId": "",
                        "VpcId": "",
                        "LoadBalanceId": "",
                        "Yaml": "apiVersion: xxxx",
                        "Ports": [
                            8080
                        ],
                        "PortMappingItemList": [
                            {
                                "Port": 8080,
                                "TargetPort": 8080,
                                "Protocol": "TCP"
                            }
                        ]
                    }
                ],
                "FlushAll": false,
                "EnableRegistryNextDeploy": 0,
                "AllIpDone": true
            },
            "Liveness": null,
            "Readiness": null,
            "StartupProbe": null,
            "EsEnable": null,
            "EnableTracing": 0,
            "EnableRegistry": 0,
            "EnableTracingReport": 0,
            "EnableMetrics": 0,
            "EnablePrometheusConf": null,
            "ApmInstanceId": "",
            "LogEnable": null,
            "RepoType": 3,
            "CreateDate": "2024-09-25 11:36:11",
            "ModifyDate": "2024-12-20 17:00:16",
            "MinAliveInstances": "",
            "ImageTag": "20241202165113",
            "SecurityGroupIds": [
                "sg-1zwhplpi"
            ],
            "EsStrategy": null,
            "AutoscalerList": [
                {
                    "AutoscalerId": "scaler-3j2o6ypg",
                    "AutoscalerName": "elastic-test",
                    "MinReplicas": 0,
                    "MaxReplicas": 4,
                    "CreateDate": "2024-12-05 11:10:19",
                    "ModifyDate": "2024-12-20 17:00:23",
                    "EnableDate": "2024-12-20 17:00:23",
                    "Description": "",
                    "Enabled": true,
                    "HorizontalAutoscaler": [
                        {
                            "MinReplicas": 0,
                            "MaxReplicas": 4,
                            "Metrics": "CPU",
                            "Threshold": 0,
                            "DoubleThreshold": 60,
                            "Enabled": true
                        }
                    ],
                    "CronHorizontalAutoscaler": []
                },
                {
                    "AutoscalerId": "scaler-b5q33njo",
                    "AutoscalerName": "pk-test-clb",
                    "MinReplicas": 0,
                    "MaxReplicas": 4,
                    "CreateDate": "2024-10-25 16:36:10",
                    "ModifyDate": "2024-11-29 10:35:52",
                    "EnableDate": "2024-11-29 10:35:52",
                    "Description": "",
                    "Enabled": false,
                    "HorizontalAutoscaler": [
                        {
                            "MinReplicas": 0,
                            "MaxReplicas": 4,
                            "Metrics": "CPU",
                            "Threshold": 0,
                            "DoubleThreshold": 50,
                            "Enabled": true
                        }
                    ],
                    "CronHorizontalAutoscaler": [
                        {
                            "Name": "pk-test",
                            "Period": "* * *",
                            "Schedules": [
                                {
                                    "StartAt": "02:00",
                                    "TargetReplicas": 1
                                }
                            ],
                            "Enabled": false,
                            "Priority": 0
                        }
                    ]
                },
                {
                    "AutoscalerId": "scaler-ojr3nlj9",
                    "AutoscalerName": "pk-test-1",
                    "MinReplicas": 1,
                    "MaxReplicas": 3,
                    "CreateDate": "2024-12-19 23:38:45",
                    "ModifyDate": "2024-12-19 23:38:45",
                    "EnableDate": null,
                    "Description": "",
                    "Enabled": false,
                    "HorizontalAutoscaler": [
                        {
                            "MinReplicas": 1,
                            "MaxReplicas": 3,
                            "Metrics": "CPU",
                            "Threshold": 0,
                            "DoubleThreshold": 50,
                            "Enabled": true
                        }
                    ],
                    "CronHorizontalAutoscaler": [
                        {
                            "Name": "policy-test",
                            "Period": "* * *",
                            "Schedules": [
                                {
                                    "StartAt": "00:00",
                                    "TargetReplicas": 1
                                }
                            ],
                            "Enabled": true,
                            "Priority": 0
                        }
                    ]
                }
            ],
            "ApplicationName": "app0925",
            "ApplicationDescription": "preStop-test",
            "EnvironmentName": "tt",
            "EnvironmentId": "en-dpxydze5",
            "RepoServer": "tem-sh-custom-registry-prd-01.tencentcloudcr.com",
            "PublicDomain": "",
            "EnablePublicAccess": null,
            "Modifier": "100019051593",
            "Creator": "100019051593",
            "CurrentInstances": 1,
            "ExpectedInstances": 3,
            "Status": "abnormal",
            "UnderDeploying": true,
            "BatchDeployStatus": "",
            "CodingLanguage": "JAVA",
            "ImageType": 1,
            "ImageCommand": "",
            "ImageArgs": null,
            "UseRegistryDefaultConfig": false,
            "DeployStrategyConf": null,
            "Zones": [
                "ap-shanghai-2"
            ],
            "LastDeployDate": "2024-12-20 17:00:17",
            "LastDeploySuccessDate": "2024-12-20 17:00:17",
            "NodeInfos": [
                {
                    "Name": "eklet-subnet-kctzw7nj-711231",
                    "Zone": "ap-shanghai-2",
                    "SubnetId": "subnet-kctzw7nj",
                    "AvailableIpCount": "243",
                    "Cidr": "10.0.10.0-24"
                },
                {
                    "Name": "eklet-subnet-8indzsuv-457482",
                    "Zone": "ap-shanghai-2",
                    "SubnetId": "subnet-8indzsuv",
                    "AvailableIpCount": "226",
                    "Cidr": "10.0.30.0-24"
                },
                {
                    "Name": "eklet-subnet-qau65gm1-638453",
                    "Zone": "ap-shanghai-2",
                    "SubnetId": "subnet-qau65gm1",
                    "AvailableIpCount": "246",
                    "Cidr": "10.0.20.0-24"
                }
            ],
            "WorkloadInfo": {
                "ApplicationName": "app0925",
                "ClusterId": "cls-kotuimb9",
                "VersionName": "20241202165113",
                "ReadyReplicas": 1,
                "Replicas": 3,
                "UpdatedReplicas": 2,
                "UpdatedReadyReplicas": 0,
                "UpdateRevision": "app0925-574b65c5f7",
                "CurrentRevision": "app0925-77969b5b49"
            },
            "PodList": {
                "Offset": 0,
                "Limit": 3,
                "TotalCount": 3,
                "PodList": [
                    {
                        "Zone": "ap-shanghai-2",
                        "NodeInfo": {
                            "Name": "eklet-subnet-kctzw7nj-711231",
                            "Zone": "ap-shanghai-2",
                            "SubnetId": "subnet-kctzw7nj",
                            "AvailableIpCount": "243",
                            "Cidr": "10.0.10.0-24"
                        },
                        "DeployVersion": "",
                        "RestartCount": 0,
                        "Ready": false,
                        "StartTime": "2024-12-20T09:01:01Z",
                        "ContainerState": "waiting",
                        "Unhealthy": null,
                        "UnhealthyWarningMsg": "",
                        "VersionId": "revision-jorxnl6j",
                        "ApplicationName": "app0925",
                        "Status": "CrashLoopBackOff",
                        "CreateTime": "2024-12-20T09:00:23Z",
                        "PodIp": "10.0.10.220",
                        "Webshell": "https://tkecache.cloud.tencent.com/xxxx",
                        "PodId": "app0925-4sbct"
                    },
                    {
                        "Zone": "ap-shanghai-2",
                        "NodeInfo": {
                            "Name": "eklet-subnet-qau65gm1-638453",
                            "Zone": "ap-shanghai-2",
                            "SubnetId": "subnet-qau65gm1",
                            "AvailableIpCount": "246",
                            "Cidr": "10.0.20.0-24"
                        },
                        "DeployVersion": "",
                        "RestartCount": 0,
                        "Ready": false,
                        "StartTime": "2024-12-20T09:01:11Z",
                        "ContainerState": "waiting",
                        "Unhealthy": null,
                        "UnhealthyWarningMsg": "",
                        "VersionId": "revision-jorxnl6j",
                        "ApplicationName": "app0925",
                        "Status": "CrashLoopBackOff",
                        "CreateTime": "2024-12-20T09:00:23Z",
                        "PodIp": "10.0.20.37",
                        "Webshell": "https://tkecache.cloud.tencent.com/xxxx",
                        "PodId": "app0925-s4vpj"
                    },
                    {
                        "Zone": "ap-shanghai-2",
                        "NodeInfo": {
                            "Name": "eklet-subnet-8indzsuv-457482",
                            "Zone": "ap-shanghai-2",
                            "SubnetId": "subnet-8indzsuv",
                            "AvailableIpCount": "226",
                            "Cidr": "10.0.30.0-24"
                        },
                        "DeployVersion": "",
                        "RestartCount": 0,
                        "Ready": true,
                        "StartTime": "2024-12-19T03:12:44Z",
                        "ContainerState": "running",
                        "Unhealthy": null,
                        "UnhealthyWarningMsg": "",
                        "VersionId": "revision-57moqvm5",
                        "ApplicationName": "app0925",
                        "Status": "Running",
                        "CreateTime": "2024-12-19T03:11:32Z",
                        "PodIp": "10.0.30.158",
                        "Webshell": "https://tkecache.cloud.tencent.com/qcloud/xxxx",
                        "PodId": "app0925-jt5bn"
                    }
                ],
                "RequestId": "csdse233-xxx-xxx-xxx"
            },
            "ConfEdited": null,
            "SpeedUp": true,
            "OsFlavour": "ALPINE",
            "StoppedManually": false,
            "TcrInstanceId": "tcr-d8g5il2x",
            "Tags": [],
            "PkgName": "tem/pkg/1305738457/app-5vaz8x85/1733129495394/K8sEventDemo-1.0.jar",
            "HorizontalAutoscaler": [],
            "CronHorizontalAutoscaler": []
        }
    }
}
```

