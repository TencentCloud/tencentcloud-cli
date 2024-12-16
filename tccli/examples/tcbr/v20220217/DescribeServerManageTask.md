**Example 1: 查询服务管理任务信息**



Input: 

```
tccli tcbr DescribeServerManageTask --cli-unfold-argument  \
    --EnvId prod-2g59lad002c864a6 \
    --ServerName golang-h7yv \
    --TaskId 1000
```

Output: 
```
{
    "Response": {
        "IsExist": false,
        "RequestId": "f72cf9c7-e477-443e-98f5-19703abbd2af",
        "Task": {
            "ChangeType": "",
            "CreateTime": "",
            "DeployType": "",
            "EnvId": "",
            "FailReason": "",
            "Id": 0,
            "OperatorRemark": "",
            "PipelineId": 0,
            "PipelineTaskId": 0,
            "PreVersionName": "",
            "ReleaseId": 0,
            "ReleaseType": "",
            "ServerName": "",
            "Status": "",
            "Steps": [],
            "VersionName": ""
        }
    }
}
```

