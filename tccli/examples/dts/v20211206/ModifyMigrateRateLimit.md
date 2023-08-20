**Example 1: 修改全量导出线程数**

修改全量导出线程数成功

Input: 

```
tccli dts ModifyMigrateRateLimit --cli-unfold-argument  \
    --JobId dts-lfjkazze \
    --DumpThread 12
```

Output: 
```
{
    "Response": {
        "RequestId": "ce7594b5-3fbc-40d8-a514-c35186cef95a"
    }
}
```

