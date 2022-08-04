**Example 1: 编辑日志收集配置**

编辑日志收集配置

Input: 

```
tccli tem ModifyLogConfig --cli-unfold-argument  \
    --EnvironmentId xx \
    --Data.TopicId xx \
    --Data.BeginningRegex xx \
    --Data.Name xx \
    --Data.CreateDate xx \
    --Data.LogPath xx \
    --Data.InputType xx \
    --Data.LogType xx \
    --Data.FilePattern xx \
    --Data.ModifyDate xx \
    --Data.LogsetId xx \
    --Name xx
```

Output: 
```
{
    "Response": {
        "RequestId": "81f74023-563c-437d-abf7-8139449ef178",
        "Result": true
    }
}
```

