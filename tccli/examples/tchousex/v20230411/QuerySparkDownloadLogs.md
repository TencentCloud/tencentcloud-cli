**Example 1: QuerySparkDownloadLogs**

查询cls 日志下载任务

Input: 

```
tccli tchousex QuerySparkDownloadLogs --cli-unfold-argument  \
    --TaskId batch-task-12334
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "SparkDownloadLogs": [
            {
                "CreateTime": "2023-01-01",
                "Status": "success",
                "PodName": "batch-task-123-driver",
                "CosPath": "cosn://fil1.log"
            }
        ],
        "RequestId": "ge2344=56gbbfss"
    }
}
```

