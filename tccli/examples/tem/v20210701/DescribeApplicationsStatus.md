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
        "RequestId": "xx"
    }
}
```

