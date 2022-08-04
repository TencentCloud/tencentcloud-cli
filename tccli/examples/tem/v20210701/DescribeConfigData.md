**Example 1: 查询配置详情**

查询配置详情

Input: 

```
tccli tem DescribeConfigData --cli-unfold-argument  \
    --EnvironmentId xx \
    --Name xx \
    --SourceChannel 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "RelatedApplications": [
                {
                    "ApplicationName": "xx",
                    "EnvironmentId": "xx",
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
                            "EnvironmentId": "xx",
                            "BuildTaskId": "xx",
                            "DeployMode": "xx",
                            "VersionId": "xx",
                            "UnderDeploying": true,
                            "VersionName": "xx",
                            "ExpectedInstances": 0,
                            "ApplicationId": "xx",
                            "EnvironmentName": "xx",
                            "ApplicationName": "xx"
                        }
                    ],
                    "DeployMode": "xx",
                    "RepoType": 0,
                    "RepoName": "xx",
                    "EnableTracing": 1,
                    "CodingLanguage": "xx",
                    "Modifier": "xx",
                    "ApplicationId": "xx",
                    "EnvironmentName": "xx"
                }
            ],
            "Data": [
                {
                    "Config": "xx",
                    "Secret": "xx",
                    "Type": "xx",
                    "Value": "xx",
                    "Key": "xx"
                }
            ],
            "Name": "xx",
            "CreateTime": "xx"
        },
        "RequestId": "xx"
    }
}
```

