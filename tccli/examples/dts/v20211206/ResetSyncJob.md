**Example 1: 重置同步任务**

任务结束后重置同步任务信息，生成一个完全初始化的同步任务

Input: 

```
tccli dts ResetSyncJob --cli-unfold-argument  \
    --JobId sync-7r1cz016
```

Output: 
```
{
    "Response": {
        "RequestId": "ead9fdc1-baa8-4a09-aaa1-c2012690c976"
    }
}
```

