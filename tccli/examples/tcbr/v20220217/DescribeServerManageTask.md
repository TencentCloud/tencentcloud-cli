**Example 1: 查询服务管理任务信息**



Input: 

```
tccli tcbr DescribeServerManageTask --cli-unfold-argument  \
    --EnvId abc \
    --ServerName abc \
    --TaskId 0 \
    --OperatorRemark abc
```

Output: 
```
{
    "Response": {
        "IsExist": true,
        "Task": {
            "Id": 0,
            "EnvId": "abc",
            "ServerName": "abc",
            "CreateTime": "abc",
            "ChangeType": "abc",
            "ReleaseType": "abc",
            "DeployType": "abc",
            "PreVersionName": "abc",
            "VersionName": "abc",
            "PipelineId": 0,
            "PipelineTaskId": 0,
            "ReleaseId": 0,
            "Status": "abc",
            "Steps": [
                {
                    "Name": "abc",
                    "Status": "abc",
                    "StartTime": "abc",
                    "EndTime": "abc",
                    "CostTime": 0,
                    "FailReason": "abc"
                }
            ],
            "FailReason": "abc",
            "OperatorRemark": "abc"
        },
        "RequestId": "abc"
    }
}
```

