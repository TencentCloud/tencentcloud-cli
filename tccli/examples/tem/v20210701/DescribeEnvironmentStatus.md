**Example 1: 获取环境状态**

获取环境状态

Input: 

```
tccli tem DescribeEnvironmentStatus --cli-unfold-argument  \
    --EnvironmentIds en-xxxxxx \
    --SourceChannel 0
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "EnvironmentId": "en-xxxxxx",
                "EnvironmentName": "en-name-xxx",
                "ClusterId": "cls-xxxxxx",
                "ClusterStatus": "running",
                "EnvironmentStartingStatus": {
                    "ApplicationNumNeedToStart": 0,
                    "StartedApplicationNum": 0,
                    "StartFailedApplicationNum": 0
                },
                "EnvironmentStoppingStatus": {
                    "ApplicationNumNeedToStop": 0,
                    "StoppedApplicationNum": 0,
                    "StopFailedApplicationNum": 0
                }
            }
        ],
        "RequestId": "1se3sd-xxx-xxx-xxx"
    }
}
```

