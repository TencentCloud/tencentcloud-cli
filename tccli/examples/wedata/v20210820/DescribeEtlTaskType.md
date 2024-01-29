**Example 1: 获取数据同步任务类型**

获取数据同步任务类型

Input: 

```
tccli wedata DescribeEtlTaskType --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TypeId": 0,
                "TypeDesc": "abc",
                "CreateTime": "abc",
                "SourceServerType": "abc",
                "TargetServerType": "abc",
                "RunJarName": "abc",
                "KillAble": 0,
                "TypeSort": "abc",
                "InCharge": "abc",
                "BrokerParallelism": 0,
                "TaskParallelism": 0,
                "DoRedoParallelism": 0,
                "DowngradePriorityTries": 0,
                "RetryWait": 0,
                "RetryLimit": 0,
                "DefaultAliveWait": 0,
                "PollingSeconds": 0,
                "ParamList": "abc",
                "FileType": "abc",
                "SelectFilePath": true,
                "ExcludeCommonLib": true,
                "PostHooks": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

