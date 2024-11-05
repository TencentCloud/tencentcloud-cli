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
                    "ApplicationId": "app-5vaz8d85",
                    "ApplicationName": "pk-test-internet",
                    "Description": "",
                    "EnvironmentId": "",
                    "CreateDate": "2024-10-16 14:17:08",
                    "ModifyDate": "2024-10-23 20:17:34",
                    "Modifier": "100019051593",
                    "Creator": "100019051593",
                    "RepoType": 3,
                    "InstanceId": "",
                    "RepoName": "",
                    "EnvironmentName": "",
                    "CodingLanguage": "JAVA",
                    "DeployMode": "",
                    "ActiveVersions": [
                        {
                            "VersionName": "20241023161452",
                            "VersionId": "revision-5n3oveqj",
                            "Status": "",
                            "BatchDeployStatus": "",
                            "EnableEs": -1,
                            "LogOutputConf": null,
                            "ExpectedInstances": null,
                            "CurrentInstances": 0,
                            "DeployMode": "JAR",
                            "BuildTaskId": "",
                            "EnvironmentId": "en-259d2b6j",
                            "EnvironmentName": "pk-test-12",
                            "ApplicationId": "app-5vaz8d85",
                            "ApplicationName": "pk-test-internet",
                            "Zones": [],
                            "NodeInfos": [],
                            "PodList": null,
                            "WorkloadInfo": null,
                            "CreateDate": "2024-10-23 20:17:34",
                            "UnderDeploying": null,
                            "RegionId": "1"
                        }
                    ],
                    "EnableTracing": 0,
                    "Tags": [],
                    "HasAuthority": true
                }
            ],
            "Total": 0,
            "Size": 0,
            "Pages": 0,
            "Current": 0
        },
        "RequestId": "67796ca7-0b76-4281-a280-c9811cd8ce62"
    }
}
```

