**Example 1: 查询服务管理任务信息**



Input: 

```
tccli tcbr DescribeServerManageTask --cli-unfold-argument  \
    --ServerName xx \
    --EnvId xx \
    --OperatorRemark xx \
    --TaskId 0
```

Output: 
```
{
    "Response": {
        "Task": {
            "Status": "xx",
            "EnvId": "xx",
            "PreVersionName": "xx",
            "ServerName": "xx",
            "PipelineId": 0,
            "ReleaseType": "xx",
            "CreateTime": "xx",
            "ReleaseId": 0,
            "FailReason": "xx",
            "DeployType": "xx",
            "PipelineTaskId": 0,
            "VersionName": "xx",
            "Steps": [
                {
                    "Status": "xx",
                    "CostTime": 0,
                    "Name": "xx",
                    "FailReason": "xx",
                    "StartTime": "xx",
                    "EndTime": "xx"
                }
            ],
            "OperatorRemark": "xx",
            "Id": 0,
            "ChangeType": "xx"
        },
        "RequestId": "xx",
        "IsExist": true
    }
}
```

