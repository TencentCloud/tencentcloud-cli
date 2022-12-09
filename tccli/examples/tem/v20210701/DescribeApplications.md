**Example 1: 获取运行服务列表**

获取运行服务列表

Input: 

```
tccli tem DescribeApplications --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Result": {
            "Current": 0,
            "Records": [
                {
                    "ApplicationName": "xx",
                    "EnvironmentId": "xx",
                    "HasAuthority": true,
                    "ModifyDate": "2020-09-22 00:00:00",
                    "Description": "xx",
                    "Creator": "xx",
                    "InstanceId": "xx",
                    "CreateDate": "2020-09-22 00:00:00",
                    "ActiveVersions": [
                        {
                            "Status": "xx",
                            "CurrentInstances": 0,
                            "LogOutputConf": {
                                "ClsLogTopicId": "xx",
                                "ClsLogsetName": "xx",
                                "ClsLogsetId": "xx",
                                "ClsLogTopicName": "xx",
                                "OutputType": "xx"
                            },
                            "EnableEs": 0,
                            "PodList": {
                                "TotalCount": 0,
                                "Limit": 0,
                                "RequestId": "xx",
                                "PodList": [
                                    {
                                        "Webshell": "xx",
                                        "Status": "xx",
                                        "RestartCount": 0,
                                        "StartTime": "xx",
                                        "Zone": "xx",
                                        "PodId": "xx",
                                        "NodeInfo": {
                                            "SubnetId": "xx",
                                            "Cidr": "xx",
                                            "AvailableIpCount": "xx",
                                            "Name": "xx",
                                            "Zone": "xx"
                                        },
                                        "VersionId": "xx",
                                        "UnhealthyWarningMsg": "xx",
                                        "DeployVersion": "xx",
                                        "PodIp": "xx",
                                        "ContainerState": "xx",
                                        "Ready": true,
                                        "ApplicationName": "xx",
                                        "CreateTime": "xx",
                                        "Unhealthy": true
                                    }
                                ],
                                "Offset": 0
                            },
                            "EnvironmentId": "xx",
                            "CreateDate": "xx",
                            "BuildTaskId": "xx",
                            "DeployMode": "xx",
                            "WorkloadInfo": {
                                "ApplicationName": "xx",
                                "UpdateRevision": "xx",
                                "UpdatedReadyReplicas": 0,
                                "Replicas": 0,
                                "ClusterId": "xx",
                                "UpdatedReplicas": 0,
                                "VersionName": "xx",
                                "CurrentRevision": "xx",
                                "ReadyReplicas": 0
                            },
                            "Zones": [
                                "xx"
                            ],
                            "VersionId": "xx",
                            "UnderDeploying": true,
                            "BatchDeployStatus": "xx",
                            "VersionName": "xx",
                            "ExpectedInstances": 0,
                            "NodeInfos": [
                                {
                                    "SubnetId": "xx",
                                    "Cidr": "xx",
                                    "AvailableIpCount": "xx",
                                    "Name": "xx",
                                    "Zone": "xx"
                                }
                            ],
                            "ApplicationId": "xx",
                            "EnvironmentName": "xx",
                            "ApplicationName": "xx"
                        }
                    ],
                    "DeployMode": "xx",
                    "RepoType": 0,
                    "RepoName": "xx",
                    "EnableTracing": 1,
                    "Tags": [
                        {
                            "TagKey": "xx",
                            "TagValue": "xx"
                        }
                    ],
                    "Modifier": "xx",
                    "ApplicationId": "xx",
                    "CodingLanguage": "xx",
                    "EnvironmentName": "xx"
                }
            ],
            "Total": 0,
            "Pages": 0,
            "Size": 0
        },
        "RequestId": "xx"
    }
}
```

