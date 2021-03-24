**Example 1: 异步导出任务**



Input: 

```
tccli cwp ExportTasks --cli-unfold-argument  \
    --TaskId c44c00fb-ab35-22e5-78e8-9a8a910d96f5
```

Output: 
```
{
    "Response": {
        "Status": "FINISHED",
        "DownloadUrl": "http://yunjing-dev-1256299843.cos.ap-guangzhou.myqcloud.com/1256299843/bruteattack-20200804-824874.csv",
        "RequestId": "f8bcfd50-3a9d-ac4c-ba95-6ed70252453e"
    }
}
```

