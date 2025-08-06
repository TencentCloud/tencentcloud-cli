**Example 1: 下载生命周期任务中文件列表**



Input: 

```
tccli cfs CreateLifecyclePolicyDownloadTask --cli-unfold-argument  \
    --TaskId task-202311gafgagl \
    --Type FileTotalList
```

Output: 
```
{
    "Response": {
        "DownloadAddress": "https://cfs-migrate-xxxxx.cos.ap-chongqi",
        "RequestId": "req-abcdefgh"
    }
}
```

