**Example 1: 单环境下所有应用状态查看**

单环境下所有应用状态查看

Input: 

```
tccli tem DescribeApplicationsStatus --cli-unfold-argument  \
    --SourceChannel 0 \
    --EnvironmentId xx
```

Output: 
```
{
    "Response": {
        "Result": [
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
        "RequestId": "xx"
    }
}
```

