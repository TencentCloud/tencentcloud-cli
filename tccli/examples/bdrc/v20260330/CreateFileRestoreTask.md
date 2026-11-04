**Example 1: 创建文件备份恢复任务**



Input: 

```
tccli bdrc CreateFileRestoreTask --cli-unfold-argument  \
    --BackupId fb-f8jabpvo \
    --TargetResourceId ins-0dl6ai18 \
    --TargetLocation /tmp
```

Output: 
```
{
    "Response": {
        "TaskId": "frt-r9za3tji",
        "RequestId": "7dfb24b7-5b67-43c0-842d-1e184256fec5"
    }
}
```

