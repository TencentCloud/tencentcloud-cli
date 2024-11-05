**Example 1: 查询配置详情**

查询配置详情

Input: 

```
tccli tem DescribeConfigData --cli-unfold-argument  \
    --EnvironmentId en-xxxxxx \
    --Name abc-xxxx \
    --SourceChannel 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "Name": "abc",
            "CreateTime": "abc",
            "RelatedApplications": [
                {
                    "ApplicationId": "abc",
                    "ApplicationName": "abc",
                    "Description": "abc",
                    "EnvironmentId": "abc",
                    "CreateDate": "2020-09-22 00:00:00",
                    "ModifyDate": "2020-09-22 00:00:00",
                    "Modifier": "abc",
                    "Creator": "abc",
                    "RepoType": 0,
                    "InstanceId": "abc",
                    "RepoName": "abc",
                    "CodingLanguage": "abc",
                    "DeployMode": "abc",
                    "EnvironmentName": "abc",
                    "ActiveVersions": [
                        {
                            "VersionName": "abc",
                            "Status": "abc",
                            "EnableEs": 0,
                            "CurrentInstances": 0,
                            "VersionId": "abc",
                            "LogOutputConf": {
                                "OutputType": "abc",
                                "ClsLogsetName": "abc",
                                "ClsLogTopicId": "abc",
                                "ClsLogsetId": "abc",
                                "ClsLogTopicName": "abc"
                            },
                            "ExpectedInstances": 0,
                            "DeployMode": "abc",
                            "BuildTaskId": "abc",
                            "EnvironmentId": "abc",
                            "EnvironmentName": "abc",
                            "ApplicationId": "abc",
                            "ApplicationName": "abc",
                            "UnderDeploying": true,
                            "BatchDeployStatus": "abc",
                            "Zones": [
                                "abc"
                            ],
                            "NodeInfos": [
                                {
                                    "Name": "abc",
                                    "Zone": "abc",
                                    "SubnetId": "abc",
                                    "AvailableIpCount": "abc",
                                    "Cidr": "abc"
                                }
                            ],
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
                            "CreateDate": "abc",
                            "RegionId": "abc"
                        }
                    ],
                    "EnableTracing": 1,
                    "Tags": [
                        {
                            "TagKey": "abc",
                            "TagValue": "abc"
                        }
                    ],
                    "HasAuthority": true
                }
            ],
            "Data": [
                {
                    "Key": "abc",
                    "Value": "abc",
                    "Type": "abc",
                    "Config": "abc",
                    "Secret": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

