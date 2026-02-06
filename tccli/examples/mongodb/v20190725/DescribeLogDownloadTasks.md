**Example 1: 日志下载任务查询**

日志下载任务查询

Input: 

```
tccli mongodb DescribeLogDownloadTasks --cli-unfold-argument  \
    --InstanceId cmgo-k2p5su09 \
    --StartTime 2024-03-07 9:22:15 \
    --EndTime 2024-03-07 15:33:15
```

Output: 
```
{
    "Response": {
        "RequestId": "832423fdfsfsd-312jdsf",
        "Tasks": [
            {
                "CreateTime": "2024-03-07 21:01:00",
                "FileSize": 372432,
                "Percent": 100,
                "Status": 2,
                "TaskId": "export-28439fb3-90a6-4ca2-bd2f-ad99e99a14e9",
                "TaskType": 0,
                "UpdateTime": "2024-03-07 21:14:02",
                "Url": ""
            }
        ],
        "TotalCount": 1
    }
}
```

