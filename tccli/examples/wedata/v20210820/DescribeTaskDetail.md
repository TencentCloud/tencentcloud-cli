**Example 1: 范例**



Input: 

```
tccli wedata DescribeTaskDetail --cli-unfold-argument  \
    --ProjectId 1 \
    --TaskId 20220727140613327
```

Output: 
```
{
    "Response": {
        "RequestId": "0b3a6016-96d1-4832-8376-afb191a21a6a",
        "Data": {
            "TaskId": "20220727140613327",
            "VirtualTaskId": null,
            "VirtualFlag": false,
            "TaskName": "task2",
            "WorkflowId": "34e51bc4-0cd9-11ed-8909-bc97e105ba60",
            "RealWorkflowId": null,
            "WorkflowName": "work1",
            "FolderId": null,
            "FolderName": null,
            "CreateTime": "2022-07-27 14:06:13",
            "LastUpdate": "2022-07-27 17:40:31",
            "Status": "NS",
            "InCharge": "TBDS",
            "StartTime": "2022-09-03 11:00:00",
            "EndTime": "2099-12-31 23:59:59",
            "ExecutionStartTime": null,
            "ExecutionEndTime": null,
            "ProjectId": "1",
            "ProjectIdent": "test_dev_all",
            "ProjectName": "test_dev_all",
            "CycleType": 1,
            "CycleStep": 10,
            "CrontabExpression": null,
            "DelayTime": 10,
            "StartupTime": 0,
            "RetryWait": 1,
            "Retriable": 1,
            "TaskAction": "",
            "TryLimit": 3,
            "RunPriority": 4,
            "TaskType": 35,
            "BrokerIp": "any",
            "ClusterId": null,
            "MinDateTime": null,
            "MaxDateTime": null,
            "SelfDepend": 1,
            "Notes": "",
            "YarnQueue": null,
            "Submit": false,
            "LastSchedulerCommitTime": null,
            "NormalizedJobStartTime": null,
            "SourceServer": null,
            "TargetServer": "11",
            "Creater": "TBDS",
            "DependencyRel": "and",
            "DependencyWorkflow": "yes",
            "DependencyConfigs": null,
            "VirtualTaskStatus": null,
            "Params": null,
            "TaskExt": [
                {
                    "Key": "aa",
                    "Value": "bb"
                },
                {
                    "Key": "bucket",
                    "Value": "wedata-fusion-dev-1257305158"
                },
                {
                    "Key": "python_type",
                    "Value": "python2"
                },
                {
                    "Key": "ftp.file.name",
                    "Value": "https://wedata-fusion-dev-1257305158.cos.ap-nanjing.myqcloud.com/datastudio/project/1/wb555/work1/task2.sh"
                },
                {
                    "Key": "region",
                    "Value": "ap-nanjing"
                },
                {
                    "Key": "extraInfo",
                    "Value": "{}"
                }
            ],
            "UpdateUser": "fe",
            "UpdateTime": "2022-07-27 17:40:31",
            "UpdateUserId": "100022256608",
            "SchedulerDesc": "从2022年09月03日 11:10:00开始，每间隔10分钟执行一次",
            "ResourceGroup": "20220420160541973718",
            "VersionDesc": null
        }
    }
}
```

