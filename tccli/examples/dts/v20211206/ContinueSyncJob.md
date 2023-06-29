**Example 1: 暂停一个同步任务**

同步任务出于已暂停状态时、可通过这个接口恢复任务

Input: 

```
tccli dts ContinueSyncJob --cli-unfold-argument  \
    --JobId sync-7r1cz016
```

Output: 
```
{
    "Response": {
        "RequestId": "31197c38-7764-49f6-845c-edbc5aa9294e"
    }
}
```

