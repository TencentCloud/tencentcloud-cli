**Example 1: 恢复暂停中的迁移任务**

任务处于暂停中时、可通过该接口继续任务

Input: 

```
tccli dts ContinueMigrateJob --cli-unfold-argument  \
    --JobId dts-j7bt5sid
```

Output: 
```
{
    "Response": {
        "RequestId": "bab78b9b-ce8a-4645-bfb2-5b03397d6ea0"
    }
}
```

