**Example 1: 获取job执行列表**

获取job执行列表

Input: 

```
tccli wedata ListCodeFileJobs --cli-unfold-argument  \
    --WorkspaceId 17623497097012366 \
    --CodeFileId 794235159865778176 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CodeFileContent": "",
                    "CodeFileId": "794235159865778176",
                    "EndTime": "0",
                    "JobExecution": [
                        {
                            "Content": "SELECT 1;",
                            "EndTime": "",
                            "JobExecutionId": "exec_1",
                            "JobExecutionName": "测试任务执行",
                            "JobId": "job_1",
                            "StartTime": "",
                            "Status": "S",
                            "TimeCost": "0",
                            "WorkspaceId": ""
                        }
                    ],
                    "JobId": "job_1",
                    "JobName": "mockJob任务",
                    "ScriptContentTruncate": false,
                    "StartTime": "0",
                    "Status": "SUCCESS",
                    "TimeCost": "0"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": "13",
            "TotalPageNumber": "0"
        },
        "RequestId": "866afe53-cf23-431c-955c-3f9c632c54b5"
    }
}
```

