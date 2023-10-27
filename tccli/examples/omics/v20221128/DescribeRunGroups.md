**Example 1: 查询任务批次列表**

查询任务批次列表。

Input: 

```
tccli omics DescribeRunGroups --cli-unfold-argument  \
    --ProjectId prj-peaceful-pink-bird-631828 \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "dfc17a50-4ff2-45b8-959d-86ab346b3d8c",
        "RunGroups": [
            {
                "ApplicationId": "app-sweet-cerulean-frog-569111",
                "ApplicationName": "base64",
                "ApplicationType": "WDL",
                "CreateTime": "2023-03-15T20:52:56+08:00",
                "Description": "",
                "EnvironmentId": "env-05d0g0w2",
                "EnvironmentName": "提交任务环境",
                "ErrorMessage": "",
                "ExecutionTime": {
                    "EndTime": "2023-03-15T20:53:23+08:00",
                    "StartTime": "2023-03-15T20:53:13+08:00",
                    "SubmitTime": "2023-03-15T20:52:56+08:00"
                },
                "Input": "omics/100000/project/prj-peaceful-pink-bird-631828/run-group/run-ashamed-turquoise-rooster-131773/inputs.json",
                "Name": "cloudapi-test",
                "Option": {
                    "FailureMode": "",
                    "UseCallCache": false,
                    "UseErrorOnHold": false,
                    "UseRelativeOutputPaths": true,
                    "FinalWorkflowOutputsDir": "cos://bucket-10000/output"
                },
                "ProjectId": "prj-peaceful-pink-bird-631828",
                "ProjectName": "run test",
                "RunGroupId": "run-ashamed-turquoise-rooster-131773",
                "RunStatusCounts": [
                    {
                        "Count": 1,
                        "Status": "SUCCESS"
                    }
                ],
                "Status": "COMPLETE",
                "TableId": "",
                "TotalRun": 1,
                "UpdateTime": "2023-03-15T20:53:51+08:00"
            },
            {
                "ApplicationId": "app-sweet-cerulean-frog-569111",
                "ApplicationName": "base64",
                "ApplicationType": "WDL",
                "CreateTime": "2023-03-15T20:21:34+08:00",
                "Description": "测试描述",
                "EnvironmentId": "env-05d0g0w2",
                "EnvironmentName": "提交任务环境",
                "ErrorMessage": "",
                "ExecutionTime": {
                    "EndTime": "2023-03-15T20:22:01+08:00",
                    "StartTime": "2023-03-15T20:21:48+08:00",
                    "SubmitTime": "2023-03-15T20:21:34+08:00"
                },
                "Input": "omics/100000/project/prj-peaceful-pink-bird-631828/run-group/run-hilarious-aqua-herring-857343/inputs.json",
                "Name": "base64-20230315202115-0",
                "Option": {
                    "FailureMode": "",
                    "UseCallCache": false,
                    "UseErrorOnHold": false,
                    "UseRelativeOutputPaths": true,
                    "FinalWorkflowOutputsDir": "cos://bucket-10000/output"
                },
                "ProjectId": "prj-peaceful-pink-bird-631828",
                "ProjectName": "run test",
                "RunGroupId": "run-hilarious-aqua-herring-857343",
                "RunStatusCounts": [
                    {
                        "Count": 1,
                        "Status": "SUCCESS"
                    }
                ],
                "Status": "COMPLETE",
                "TableId": "",
                "TotalRun": 1,
                "UpdateTime": "2023-03-15T20:22:28+08:00"
            }
        ],
        "TotalCount": 108
    }
}
```

