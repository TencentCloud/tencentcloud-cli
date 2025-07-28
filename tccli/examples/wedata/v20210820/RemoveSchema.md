**Example 1: 移除schema元数据**

移除schema元数据,该接口异步处理删除任务
可以通过GetJobStatus获取删除状态

Input: 

```
tccli wedata RemoveSchema --cli-unfold-argument  \
    --DatasourceId 62112 \
    --DatabaseName default \
    --SchemaName default_schema
```

Output: 
```
{
    "Response": {
        "JobId": "244",
        "RequestId": "cfe9c87e-cc9e-40ba-bd4c-f5f54cf8769f"
    }
}
```

