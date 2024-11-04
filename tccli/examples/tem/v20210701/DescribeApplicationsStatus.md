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
        "Result": [
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
        "RequestId": "abc"
    }
}
```

