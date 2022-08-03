**Example 1: 查询配置列表**

查询配置列表

Input: 

```
tccli tem DescribeConfigDataList --cli-unfold-argument  \
    --EnvironmentId xx \
    --ContinueToken xx \
    --Limit 0 \
    --SourceChannel 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "Records": [
                {
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
                            "CodingLanguage": "xx",
                            "Modifier": "xx",
                            "ApplicationId": "xx",
                            "EnvironmentName": "xx"
                        }
                    ],
                    "Data": [
                        {
                            "Value": "xx",
                            "Key": "xx"
                        }
                    ],
                    "Name": "xx",
                    "CreateTime": "xx"
                }
            ],
            "RemainingCount": 0,
            "ContinueToken": "xx"
        },
        "RequestId": "xx"
    }
}
```

