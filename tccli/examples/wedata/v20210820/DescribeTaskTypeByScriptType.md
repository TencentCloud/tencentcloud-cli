**Example 1: 根据脚本类型获取任务类型**

编排空间导入任务用

Input: 

```
tccli wedata DescribeTaskTypeByScriptType --cli-unfold-argument  \
    --ProjectId abc \
    --ScriptType abc
```

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
                "TaskTypeExtension": [
                    {
                        "TaskTypeExtKey": "abc",
                        "TaskTypeExtValue": {
                            "TypeId": 0,
                            "PropName": "abc",
                            "PropLabel": "abc",
                            "DefaultFlag": 0,
                            "VisibleFlag": 0,
                            "PropDesc": "abc",
                            "RankId": 0,
                            "InputType": "abc",
                            "ValueType": "abc",
                            "DefaultValue": "abc",
                            "CandidateValues": "abc",
                            "IsMandatory": 0,
                            "MaxValue": 0,
                            "MinValue": 0,
                            "ConfLevel": 0,
                            "CandidateTexts": "abc",
                            "CopyKey": 0,
                            "Regex": "abc",
                            "Tip": "abc",
                            "Candidates": [
                                {
                                    "Value": "abc",
                                    "ValueDesc": "abc"
                                }
                            ]
                        }
                    }
                ],
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

