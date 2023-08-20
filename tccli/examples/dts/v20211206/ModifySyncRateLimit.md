**Example 1: 修改任务全量导出线程数**

修改任务全量导出线程数成功

Input: 

```
tccli dts ModifySyncRateLimit --cli-unfold-argument  \
    --JobId sync-asasdasa \
    --DumpThread 12 \
    --DumpRps 0 \
    --LoadThread 0 \
    --SinkerThread 0 \
    --LoadRps 0
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

