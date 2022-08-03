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
            "Records": [
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
            "Total": 0,
            "Pages": 0,
            "Size": 0
        },
        "RequestId": "xx"
    }
}
```

