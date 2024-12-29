**Example 1: 单环境下所有应用状态查看**

单环境下所有应用状态查看

Input: 

```
tccli tem DescribeApplicationsStatus --cli-unfold-argument  \
    --SourceChannel 0 \
    --EnvironmentId en-xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "dda3b8c7-b536-4842-92a2-6756688a337e",
        "Result": [
            {
                "VersionName": "bj",
                "VersionId": "revision-jbzmeq7j",
                "Status": "normal",
                "BatchDeployStatus": "",
                "EnableEs": -1,
                "LogOutputConf": null,
                "ExpectedInstances": 1,
                "CurrentInstances": 1,
                "DeployMode": "JAR",
                "BuildTaskId": "build-5enzamz5",
                "EnvironmentId": "en-dpxydml5",
                "EnvironmentName": "bugfix-bj",
                "ApplicationId": "app-5vaz8x85",
                "ApplicationName": "app0925",
                "Zones": [
                    "ap-beijing-3"
                ],
                "NodeInfos": [
                    {
                        "Name": "eklet-subnet-1ebj4rp9-766511",
                        "Zone": "ap-beijing-3",
                        "SubnetId": "subnet-1ebj4rp9",
                        "AvailableIpCount": "232",
                        "Cidr": "10.0.0.0-24"
                    }
                ],
                "PodList": {
                    "Offset": -1,
                    "Limit": -1,
                    "TotalCount": 1,
                    "PodList": [
                        {
                            "Zone": "ap-beijing-3",
                            "NodeInfo": {
                                "Name": "eklet-subnet-1ebj4rp9-766511",
                                "Zone": "ap-beijing-3",
                                "SubnetId": "subnet-1ebj4rp9",
                                "AvailableIpCount": "232",
                                "Cidr": "10.0.0.0-24"
                            },
                            "DeployVersion": "",
                            "RestartCount": 0,
                            "Ready": true,
                            "StartTime": "2024-09-25T03:39:59Z",
                            "ContainerState": "running",
                            "Unhealthy": null,
                            "UnhealthyWarningMsg": "",
                            "VersionId": "revision-jbzmeq7j",
                            "ApplicationName": "app0925",
                            "Status": "Running",
                            "CreateTime": "2024-09-25T03:39:08Z",
                            "Webshell": "https://tkecache.cloud.tencent.com/xxx",
                            "PodId": "app0925-p728w",
                            "PodIp": "10.0.0.7"
                        }
                    ],
                    "RequestId": ""
                },
                "WorkloadInfo": {
                    "ApplicationName": "app0925",
                    "ClusterId": "cls-1trz6x5l",
                    "VersionName": "bj",
                    "ReadyReplicas": 1,
                    "Replicas": 1,
                    "UpdatedReplicas": 1,
                    "UpdatedReadyReplicas": 1,
                    "UpdateRevision": "app0925-868b68987",
                    "CurrentRevision": "app0925-868b68987"
                },
                "CreateDate": null,
                "UnderDeploying": false,
                "RegionId": "8"
            },
            {
                "VersionName": "hello-world",
                "VersionId": "revision-jordnl7j",
                "Status": "normal",
                "BatchDeployStatus": "",
                "EnableEs": -1,
                "LogOutputConf": null,
                "ExpectedInstances": 1,
                "CurrentInstances": 1,
                "DeployMode": "IMAGE",
                "BuildTaskId": "",
                "EnvironmentId": "en-dpxydml5",
                "EnvironmentName": "bugfix-bj",
                "ApplicationId": "app-57477ag5",
                "ApplicationName": "bugfix-test",
                "Zones": [
                    "ap-beijing-3"
                ],
                "NodeInfos": [
                    {
                        "Name": "eklet-subnet-1ebj4rp9-766511",
                        "Zone": "ap-beijing-3",
                        "SubnetId": "subnet-1ebj4rp9",
                        "AvailableIpCount": "232",
                        "Cidr": "10.0.0.0-24"
                    }
                ],
                "PodList": {
                    "Offset": -1,
                    "Limit": -1,
                    "TotalCount": 1,
                    "PodList": [
                        {
                            "Zone": "ap-beijing-3",
                            "NodeInfo": {
                                "Name": "eklet-subnet-1ebj4rp9-766511",
                                "Zone": "ap-beijing-3",
                                "SubnetId": "subnet-1ebj4rp9",
                                "AvailableIpCount": "232",
                                "Cidr": "10.0.0.0-24"
                            },
                            "DeployVersion": "",
                            "RestartCount": 0,
                            "Ready": true,
                            "StartTime": "2024-08-05T08:15:26Z",
                            "ContainerState": "running",
                            "Unhealthy": null,
                            "UnhealthyWarningMsg": "",
                            "VersionId": "revision-jordnl7j",
                            "ApplicationName": "bugfix-test",
                            "Status": "Running",
                            "CreateTime": "2024-08-05T08:14:28Z",
                            "Webshell": "https://tkecache.cloud.tencent.com/xxx",
                            "PodId": "bugfix-test-lvn56",
                            "PodIp": "10.0.0.16"
                        }
                    ],
                    "RequestId": ""
                },
                "WorkloadInfo": {
                    "ApplicationName": "bugfix-test",
                    "ClusterId": "cls-1trz6x5l",
                    "VersionName": "hello-world",
                    "ReadyReplicas": 1,
                    "Replicas": 1,
                    "UpdatedReplicas": 1,
                    "UpdatedReadyReplicas": 1,
                    "UpdateRevision": "bugfix-test-648f6b456d",
                    "CurrentRevision": "bugfix-test-648f6b456d"
                },
                "CreateDate": null,
                "UnderDeploying": false,
                "RegionId": "8"
            }
        ]
    }
}
```

